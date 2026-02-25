from flask import Blueprint, render_template, request, redirect, url_for, flash
from app.models import Cell
from app import db

cells_bp = Blueprint("cells", __name__)


@cells_bp.route("/")
def index():
    cell_type = request.args.get("type", "")
    status = request.args.get("status", "")
    floor = request.args.get("floor", "")

    query = Cell.query
    if cell_type:
        query = query.filter_by(cell_type=cell_type)
    if status:
        query = query.filter_by(status=status)
    if floor:
        query = query.filter_by(floor=floor)

    cells = query.order_by(Cell.number).all()

    stats = {
        "total": Cell.query.count(),
        "available": Cell.query.filter_by(status="available").count(),
        "occupied": Cell.query.filter_by(status="occupied").count(),
    }
    return render_template(
        "cells/index.html",
        cells=cells,
        stats=stats,
        cell_type=cell_type,
        status=status,
        floor=floor,
    )


@cells_bp.route("/new", methods=["GET", "POST"])
def new():
    if request.method == "POST":
        number = request.form.get("number", "").strip().upper()
        if Cell.query.filter_by(number=number).first():
            flash(f"Ya existe una celda con el número {number}.", "danger")
            return redirect(url_for("cells.new"))

        cell = Cell(
            number=number,
            cell_type=request.form.get("cell_type"),
            floor=request.form.get("floor", 1),
            monthly_fee=request.form.get("monthly_fee"),
        )
        db.session.add(cell)
        db.session.commit()
        flash("Celda creada exitosamente.", "success")
        return redirect(url_for("cells.index"))

    return render_template("cells/new.html")


@cells_bp.route("/<int:cell_id>/edit", methods=["GET", "POST"])
def edit(cell_id):
    cell = Cell.query.get_or_404(cell_id)
    if request.method == "POST":
        cell.cell_type = request.form.get("cell_type")
        cell.floor = request.form.get("floor", 1)
        cell.monthly_fee = request.form.get("monthly_fee")
        db.session.commit()
        flash("Celda actualizada exitosamente.", "success")
        return redirect(url_for("cells.index"))

    return render_template("cells/edit.html", cell=cell)
