from datetime import datetime
from app import db


class User(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    document = db.Column(db.String(20), unique=True, nullable=False)
    full_name = db.Column(db.String(120), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    phone = db.Column(db.String(20), nullable=False)
    address = db.Column(db.String(200))
    is_active = db.Column(db.Boolean, default=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    vehicles = db.relationship("Vehicle", backref="owner", lazy=True)
    payments = db.relationship("Payment", backref="user", lazy=True)

    def __repr__(self):
        return f"<User {self.full_name}>"


class Cell(db.Model):
    __tablename__ = "cells"

    id = db.Column(db.Integer, primary_key=True)
    number = db.Column(db.String(10), unique=True, nullable=False)
    cell_type = db.Column(db.String(20), nullable=False)  # car, motorcycle, truck
    status = db.Column(db.String(20), default="available")  # available, occupied
    floor = db.Column(db.Integer, default=1)
    monthly_fee = db.Column(db.Float, nullable=False)

    vehicles = db.relationship("Vehicle", backref="cell", lazy=True)

    def __repr__(self):
        return f"<Cell {self.number}>"


class Vehicle(db.Model):
    __tablename__ = "vehicles"

    id = db.Column(db.Integer, primary_key=True)
    plate = db.Column(db.String(10), unique=True, nullable=False)
    brand = db.Column(db.String(60), nullable=False)
    model = db.Column(db.String(60), nullable=False)
    year = db.Column(db.Integer)
    color = db.Column(db.String(40))
    vehicle_type = db.Column(db.String(20), nullable=False)  # car, motorcycle, truck
    is_active = db.Column(db.Boolean, default=True)
    registered_at = db.Column(db.DateTime, default=datetime.utcnow)

    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    cell_id = db.Column(db.Integer, db.ForeignKey("cells.id"), nullable=True)

    movements = db.relationship("Movement", backref="vehicle", lazy=True)
    incidents = db.relationship("Incident", backref="vehicle", lazy=True)

    def __repr__(self):
        return f"<Vehicle {self.plate}>"


class Movement(db.Model):
    __tablename__ = "movements"

    id = db.Column(db.Integer, primary_key=True)
    movement_type = db.Column(db.String(10), nullable=False)  # entry, exit
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)
    notes = db.Column(db.String(255))

    vehicle_id = db.Column(db.Integer, db.ForeignKey("vehicles.id"), nullable=False)

    def __repr__(self):
        return f"<Movement {self.movement_type} - {self.vehicle_id}>"


class Payment(db.Model):
    __tablename__ = "payments"

    id = db.Column(db.Integer, primary_key=True)
    amount = db.Column(db.Float, nullable=False)
    payment_date = db.Column(db.DateTime, default=datetime.utcnow)
    period_month = db.Column(db.Integer, nullable=False)
    period_year = db.Column(db.Integer, nullable=False)
    status = db.Column(db.String(20), default="paid")  # paid, pending, overdue
    payment_method = db.Column(db.String(30))  # cash, transfer, card

    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    vehicle_id = db.Column(db.Integer, db.ForeignKey("vehicles.id"), nullable=True)

    def __repr__(self):
        return f"<Payment {self.amount} - {self.user_id}>"


class Incident(db.Model):
    __tablename__ = "incidents"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
    severity = db.Column(db.String(20), default="low")  # low, medium, high
    status = db.Column(db.String(20), default="open")  # open, resolved, closed
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    resolved_at = db.Column(db.DateTime, nullable=True)

    vehicle_id = db.Column(db.Integer, db.ForeignKey("vehicles.id"), nullable=False)

    def __repr__(self):
        return f"<Incident {self.title}>"
