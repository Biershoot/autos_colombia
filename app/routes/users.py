from flask import Blueprint, render_template, request, redirect, url_for, flash
from app.models import User
from app import db

users_bp = Blueprint("users", __name__)


@users_bp.route("/")
def index():
    page = request.args.get("page", 1, type=int)
    search = request.args.get("search", "")
    query = User.query.filter_by(is_active=True)
    if search:
        query = query.filter(
            User.full_name.ilike(f"%{search}%")
            | User.document.ilike(f"%{search}%")
            | User.email.ilike(f"%{search}%")
        )
    users = query.order_by(User.full_name).paginate(page=page, per_page=15)
    return render_template("users/index.html", users=users, search=search)


@users_bp.route("/new", methods=["GET", "POST"])
def new():
    if request.method == "POST":
        document = request.form.get("document", "").strip()
        email = request.form.get("email", "").strip().lower()

        if User.query.filter_by(document=document).first():
            flash("Ya existe un usuario con ese número de documento.", "danger")
            return redirect(url_for("users.new"))
        if User.query.filter_by(email=email).first():
            flash("Ya existe un usuario con ese correo electrónico.", "danger")
            return redirect(url_for("users.new"))

        user = User(
            document=document,
            full_name=request.form.get("full_name"),
            email=email,
            phone=request.form.get("phone"),
            address=request.form.get("address"),
        )
        db.session.add(user)
        db.session.commit()
        flash("Usuario registrado exitosamente.", "success")
        return redirect(url_for("users.index"))

    return render_template("users/new.html")


@users_bp.route("/<int:user_id>")
def detail(user_id):
    user = User.query.get_or_404(user_id)
    return render_template("users/detail.html", user=user)


@users_bp.route("/<int:user_id>/edit", methods=["GET", "POST"])
def edit(user_id):
    user = User.query.get_or_404(user_id)
    if request.method == "POST":
        email = request.form.get("email", "").strip().lower()
        existing = User.query.filter_by(email=email).first()
        if existing and existing.id != user.id:
            flash("Ya existe otro usuario con ese correo electrónico.", "danger")
            return redirect(url_for("users.edit", user_id=user_id))

        user.full_name = request.form.get("full_name")
        user.email = email
        user.phone = request.form.get("phone")
        user.address = request.form.get("address")
        db.session.commit()
        flash("Usuario actualizado exitosamente.", "success")
        return redirect(url_for("users.detail", user_id=user_id))

    return render_template("users/edit.html", user=user)


@users_bp.route("/<int:user_id>/deactivate", methods=["POST"])
def deactivate(user_id):
    user = User.query.get_or_404(user_id)
    user.is_active = False
    db.session.commit()
    flash("Usuario desactivado.", "info")
    return redirect(url_for("users.index"))
