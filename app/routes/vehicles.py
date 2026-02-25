from flask import Blueprint, render_template, request, redirect, url_for, flash
from app.models import Vehicle, User, Cell
from app import db

vehicles_bp = Blueprint("vehicles", __name__)


@vehicles_bp.route("/")
def index():
    page = request.args.get("page", 1, type=int)
    search = request.args.get("search", "")
    query = Vehicle.query.filter_by(is_active=True)
    if search:
        query = query.filter(
            Vehicle.plate.ilike(f"%{search}%")
            | Vehicle.brand.ilike(f"%{search}%")
            | Vehicle.model.ilike(f"%{search}%")
        )
    vehicles = query.order_by(Vehicle.plate).paginate(page=page, per_page=15)
    return render_template("vehicles/index.html", vehicles=vehicles, search=search)


@vehicles_bp.route("/new", methods=["GET", "POST"])
def new():
    if request.method == "POST":
        plate = request.form.get("plate", "").upper().strip()
        existing = Vehicle.query.filter_by(plate=plate).first()
        if existing:
            flash(f"Ya existe un vehículo con la placa {plate}.", "danger")
            return redirect(url_for("vehicles.new"))

        cell_id = request.form.get("cell_id") or None
        if cell_id:
            cell = Cell.query.get(cell_id)
            if cell and cell.status == "occupied":
                flash("La celda seleccionada ya está ocupada.", "danger")
                return redirect(url_for("vehicles.new"))
            if cell:
                cell.status = "occupied"

        vehicle = Vehicle(
            plate=plate,
            brand=request.form.get("brand"),
            model=request.form.get("model"),
            year=request.form.get("year") or None,
            color=request.form.get("color"),
            vehicle_type=request.form.get("vehicle_type"),
            user_id=request.form.get("user_id"),
            cell_id=cell_id,
        )
        db.session.add(vehicle)
        db.session.commit()
        flash("Vehículo registrado exitosamente.", "success")
        return redirect(url_for("vehicles.index"))

    users = User.query.filter_by(is_active=True).order_by(User.full_name).all()
    cells = Cell.query.filter_by(status="available").order_by(Cell.number).all()
    return render_template("vehicles/new.html", users=users, cells=cells)


@vehicles_bp.route("/<int:vehicle_id>")
def detail(vehicle_id):
    vehicle = Vehicle.query.get_or_404(vehicle_id)
    return render_template("vehicles/detail.html", vehicle=vehicle)


@vehicles_bp.route("/<int:vehicle_id>/edit", methods=["GET", "POST"])
def edit(vehicle_id):
    vehicle = Vehicle.query.get_or_404(vehicle_id)
    if request.method == "POST":
        old_cell_id = vehicle.cell_id
        new_cell_id = request.form.get("cell_id") or None

        if old_cell_id and str(old_cell_id) != str(new_cell_id):
            old_cell = Cell.query.get(old_cell_id)
            if old_cell:
                old_cell.status = "available"

        if new_cell_id and str(new_cell_id) != str(old_cell_id):
            new_cell = Cell.query.get(new_cell_id)
            if new_cell and new_cell.status == "occupied":
                flash("La celda seleccionada ya está ocupada.", "danger")
                return redirect(url_for("vehicles.edit", vehicle_id=vehicle_id))
            if new_cell:
                new_cell.status = "occupied"

        vehicle.brand = request.form.get("brand")
        vehicle.model = request.form.get("model")
        vehicle.year = request.form.get("year") or None
        vehicle.color = request.form.get("color")
        vehicle.vehicle_type = request.form.get("vehicle_type")
        vehicle.cell_id = new_cell_id
        db.session.commit()
        flash("Vehículo actualizado exitosamente.", "success")
        return redirect(url_for("vehicles.detail", vehicle_id=vehicle_id))

    users = User.query.filter_by(is_active=True).order_by(User.full_name).all()
    cells = Cell.query.filter(
        (Cell.status == "available") | (Cell.id == vehicle.cell_id)
    ).order_by(Cell.number).all()
    return render_template("vehicles/edit.html", vehicle=vehicle, users=users, cells=cells)


@vehicles_bp.route("/<int:vehicle_id>/deactivate", methods=["POST"])
def deactivate(vehicle_id):
    vehicle = Vehicle.query.get_or_404(vehicle_id)
    if vehicle.cell_id:
        cell = Cell.query.get(vehicle.cell_id)
        if cell:
            cell.status = "available"
        vehicle.cell_id = None
    vehicle.is_active = False
    db.session.commit()
    flash("Vehículo desactivado.", "info")
    return redirect(url_for("vehicles.index"))
