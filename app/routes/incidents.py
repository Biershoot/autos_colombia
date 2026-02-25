from flask import Blueprint, render_template, request, redirect, url_for, flash
from app.models import Incident, Vehicle
from app import db
from datetime import datetime

incidents_bp = Blueprint("incidents", __name__)


@incidents_bp.route("/")
def index():
    page = request.args.get("page", 1, type=int)
    status = request.args.get("status", "")
    severity = request.args.get("severity", "")

    query = db.session.query(Incident, Vehicle).join(
        Vehicle, Incident.vehicle_id == Vehicle.id
    )
    if status:
        query = query.filter(Incident.status == status)
    if severity:
        query = query.filter(Incident.severity == severity)

    incidents = query.order_by(Incident.created_at.desc()).paginate(
        page=page, per_page=15
    )
    return render_template(
        "incidents/index.html",
        incidents=incidents,
        status=status,
        severity=severity,
    )


@incidents_bp.route("/new", methods=["GET", "POST"])
def new():
    if request.method == "POST":
        incident = Incident(
            title=request.form.get("title"),
            description=request.form.get("description"),
            severity=request.form.get("severity"),
            vehicle_id=request.form.get("vehicle_id"),
        )
        db.session.add(incident)
        db.session.commit()
        flash("Novedad registrada exitosamente.", "success")
        return redirect(url_for("incidents.index"))

    vehicles = Vehicle.query.filter_by(is_active=True).order_by(Vehicle.plate).all()
    return render_template("incidents/new.html", vehicles=vehicles)


@incidents_bp.route("/<int:incident_id>/resolve", methods=["POST"])
def resolve(incident_id):
    incident = Incident.query.get_or_404(incident_id)
    incident.status = "resolved"
    incident.resolved_at = datetime.utcnow()
    db.session.commit()
    flash("Novedad marcada como resuelta.", "success")
    return redirect(url_for("incidents.index"))


@incidents_bp.route("/<int:incident_id>")
def detail(incident_id):
    incident = Incident.query.get_or_404(incident_id)
    return render_template("incidents/detail.html", incident=incident)
