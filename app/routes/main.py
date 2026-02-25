from flask import Blueprint, render_template
from app.models import Vehicle, User, Cell, Movement, Payment, Incident
from app import db
from datetime import datetime, timedelta
from sqlalchemy import func

main_bp = Blueprint("main", __name__)


@main_bp.route("/")
def index():
    total_vehicles = Vehicle.query.filter_by(is_active=True).count()
    total_users = User.query.filter_by(is_active=True).count()
    available_cells = Cell.query.filter_by(status="available").count()
    occupied_cells = Cell.query.filter_by(status="occupied").count()

    today_start = datetime.utcnow().replace(hour=0, minute=0, second=0, microsecond=0)
    today_entries = Movement.query.filter(
        Movement.movement_type == "entry",
        Movement.timestamp >= today_start,
    ).count()
    today_exits = Movement.query.filter(
        Movement.movement_type == "exit",
        Movement.timestamp >= today_start,
    ).count()

    recent_movements = (
        db.session.query(Movement, Vehicle)
        .join(Vehicle, Movement.vehicle_id == Vehicle.id)
        .order_by(Movement.timestamp.desc())
        .limit(10)
        .all()
    )

    open_incidents = Incident.query.filter_by(status="open").count()

    month_now = datetime.utcnow().month
    year_now = datetime.utcnow().year
    monthly_revenue = (
        db.session.query(func.sum(Payment.amount))
        .filter_by(period_month=month_now, period_year=year_now, status="paid")
        .scalar()
        or 0
    )

    return render_template(
        "index.html",
        total_vehicles=total_vehicles,
        total_users=total_users,
        available_cells=available_cells,
        occupied_cells=occupied_cells,
        today_entries=today_entries,
        today_exits=today_exits,
        recent_movements=recent_movements,
        open_incidents=open_incidents,
        monthly_revenue=monthly_revenue,
    )
