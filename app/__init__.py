from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import Config

db = SQLAlchemy()


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)

    from app.routes.main import main_bp
    from app.routes.vehicles import vehicles_bp
    from app.routes.users import users_bp
    from app.routes.cells import cells_bp
    from app.routes.payments import payments_bp
    from app.routes.incidents import incidents_bp
    from app.routes.movements import movements_bp

    app.register_blueprint(main_bp)
    app.register_blueprint(vehicles_bp, url_prefix="/vehicles")
    app.register_blueprint(users_bp, url_prefix="/users")
    app.register_blueprint(cells_bp, url_prefix="/cells")
    app.register_blueprint(payments_bp, url_prefix="/payments")
    app.register_blueprint(incidents_bp, url_prefix="/incidents")
    app.register_blueprint(movements_bp, url_prefix="/movements")

    with app.app_context():
        db.create_all()
        _seed_cells(app)

    return app


def _seed_cells(app):
    from app.models import Cell

    if Cell.query.count() == 0:
        cells = []
        fees = {"car": 150000, "motorcycle": 80000, "truck": 200000}
        types = [("car", 30), ("motorcycle", 20), ("truck", 10)]
        cell_num = 1
        for floor in range(1, 4):
            for vtype, count in types:
                for _ in range(count // 3):
                    cells.append(
                        Cell(
                            number=f"{floor}{str(cell_num).zfill(3)}",
                            cell_type=vtype,
                            floor=floor,
                            monthly_fee=fees[vtype],
                        )
                    )
                    cell_num += 1
        db.session.bulk_save_objects(cells)
        db.session.commit()
