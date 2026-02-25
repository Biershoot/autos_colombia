from flask import Blueprint, render_template, request, redirect, url_for, flash
from app.models import Payment, User, Vehicle
from app import db
from datetime import datetime

payments_bp = Blueprint("payments", __name__)


@payments_bp.route("/")
def index():
    page = request.args.get("page", 1, type=int)
    status = request.args.get("status", "")
    month = request.args.get("month", "")
    year = request.args.get("year", str(datetime.utcnow().year))

    query = db.session.query(Payment, User).join(User, Payment.user_id == User.id)
    if status:
        query = query.filter(Payment.status == status)
    if month:
        query = query.filter(Payment.period_month == int(month))
    if year:
        query = query.filter(Payment.period_year == int(year))

    payments = query.order_by(Payment.payment_date.desc()).paginate(
        page=page, per_page=15
    )
    return render_template(
        "payments/index.html",
        payments=payments,
        status=status,
        month=month,
        year=year,
    )


@payments_bp.route("/new", methods=["GET", "POST"])
def new():
    if request.method == "POST":
        user_id = request.form.get("user_id")
        vehicle_id = request.form.get("vehicle_id") or None
        amount = request.form.get("amount")
        period_month = request.form.get("period_month")
        period_year = request.form.get("period_year")
        payment_method = request.form.get("payment_method")

        existing = Payment.query.filter_by(
            user_id=user_id,
            vehicle_id=vehicle_id,
            period_month=period_month,
            period_year=period_year,
            status="paid",
        ).first()
        if existing:
            flash("Ya existe un pago registrado para ese vehículo en ese período.", "warning")
            return redirect(url_for("payments.new"))

        payment = Payment(
            user_id=user_id,
            vehicle_id=vehicle_id,
            amount=amount,
            period_month=int(period_month),
            period_year=int(period_year),
            payment_method=payment_method,
            status="paid",
        )
        db.session.add(payment)
        db.session.commit()
        flash("Pago registrado exitosamente.", "success")
        return redirect(url_for("payments.index"))

    users = User.query.filter_by(is_active=True).order_by(User.full_name).all()
    now = datetime.utcnow()
    return render_template(
        "payments/new.html",
        users=users,
        current_month=now.month,
        current_year=now.year,
    )


@payments_bp.route("/get_vehicles/<int:user_id>")
def get_vehicles(user_id):
    vehicles = Vehicle.query.filter_by(user_id=user_id, is_active=True).all()
    from flask import jsonify
    return jsonify(
        [{"id": v.id, "plate": v.plate, "fee": v.cell.monthly_fee if v.cell else 0} for v in vehicles]
    )
