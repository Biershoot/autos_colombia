from flask import Blueprint, render_template, request, redirect, url_for, flash
from app.models import Movement, Vehicle, Cell
from app import db
from datetime import datetime

movements_bp = Blueprint("movements", __name__)


@movements_bp.route("/")
def index():
    page = request.args.get("page", 1, type=int)
    movement_type = request.args.get("type", "")
    plate = request.args.get("plate", "")

    query = db.session.query(Movement, Vehicle).join(
        Vehicle, Movement.vehicle_id == Vehicle.id
    )
    if movement_type:
        query = query.filter(Movement.movement_type == movement_type)
    if plate:
        query = query.filter(Vehicle.plate.ilike(f"%{plate}%"))

    movements = query.order_by(Movement.timestamp.desc()).paginate(
        page=page, per_page=20
    )
    return render_template(
        "movements/index.html",
        movements=movements,
        movement_type=movement_type,
        plate=plate,
    )


@movements_bp.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        plate = request.form.get("plate", "").upper().strip()
        movement_type = request.form.get("movement_type")
        notes = request.form.get("notes", "")

        vehicle = Vehicle.query.filter_by(plate=plate, is_active=True).first()
        if not vehicle:
            flash(f"No se encontró un vehículo activo con placa {plate}.", "danger")
            return redirect(url_for("movements.register"))

        if movement_type == "entry":
            last_move = (
                Movement.query.filter_by(vehicle_id=vehicle.id)
                .order_by(Movement.timestamp.desc())
                .first()
            )
            if last_move and last_move.movement_type == "entry":
                flash(
                    "El vehículo ya tiene una entrada registrada sin salida.", "warning"
                )
                return redirect(url_for("movements.register"))

            if vehicle.cell_id:
                cell = Cell.query.get(vehicle.cell_id)
                if cell:
                    cell.status = "occupied"

        elif movement_type == "exit":
            last_move = (
                Movement.query.filter_by(vehicle_id=vehicle.id)
                .order_by(Movement.timestamp.desc())
                .first()
            )
            if last_move and last_move.movement_type == "exit":
                flash(
                    "El vehículo ya tiene una salida registrada. Debe registrar entrada primero.",
                    "warning",
                )
                return redirect(url_for("movements.register"))

            if vehicle.cell_id:
                cell = Cell.query.get(vehicle.cell_id)
                if cell:
                    cell.status = "available"

        movement = Movement(
            vehicle_id=vehicle.id,
            movement_type=movement_type,
            notes=notes,
        )
        db.session.add(movement)
        db.session.commit()

        action = "entrada" if movement_type == "entry" else "salida"
        flash(
            f"Se registró la {action} del vehículo {plate} correctamente.", "success"
        )
        return redirect(url_for("movements.index"))

    vehicles = Vehicle.query.filter_by(is_active=True).order_by(Vehicle.plate).all()
    return render_template("movements/register.html", vehicles=vehicles)
