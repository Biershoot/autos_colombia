# Parqueadero Autos Colombia

**Autos Colombia** es un sistema web de gestión operativa para parqueaderos que prestan el servicio por mensualidad. Fue desarrollado como proyecto académico en el marco de la asignatura de Ingeniería de Software y Datos, cubriendo la Iteración 1 del ciclo de desarrollo.

El sistema permite administrar de forma centralizada las operaciones diarias del parqueadero: el registro de entradas y salidas de vehículos, la gestión de clientes, el control de celdas disponibles, el seguimiento de pagos mensuales y el reporte de novedades o incidentes sobre los vehículos. Todo esto a través de una interfaz web moderna, intuitiva y responsiva, construida con Flask y Bootstrap 5.

### Contexto del Negocio

El parqueadero **Autos Colombia** opera bajo un modelo de mensualidad fija, donde cada cliente registra uno o más vehículos y se le asigna una celda específica dentro de las instalaciones. El sistema reemplaza los registros manuales en papel, ofreciendo un control en tiempo real del flujo vehicular, la ocupación del parqueadero y el estado de cartera de cada cliente.

## Funcionalidades

- **Entradas y Salidas**: Registro de movimientos de vehículos con validaciones
- **Vehículos**: CRUD completo con asignación de celdas
- **Usuarios**: Gestión de clientes con historial de vehículos y pagos
- **Celdas**: Vista visual del estado del parqueadero por piso
- **Pagos**: Registro de mensualidades con auto-cálculo de tarifa
- **Novedades**: Registro y seguimiento de incidentes por vehículo
- **Dashboard**: Métricas en tiempo real

## Instalación y Ejecución

### Requisitos
- Python 3.10 o superior

### Pasos

```bash
# 1. Instalar dependencias
pip install -r requirements.txt

# 2. Ejecutar la aplicación
python run.py
```

Abrir el navegador en: **http://localhost:5000**

La base de datos SQLite se crea automáticamente en `database/autos_colombia.db`
con celdas preconfiguradas.

### Cargar datos de prueba (opcional)

```bash
# En Windows PowerShell o CMD
python -c "
from app import create_app, db
from app.models import *
app = create_app()
with app.app_context():
    with open('database/seed.sql') as f:
        from sqlalchemy import text
        for stmt in f.read().split(';'):
            stmt = stmt.strip()
            if stmt:
                try:
                    db.session.execute(text(stmt))
                except: pass
        db.session.commit()
print('Datos de prueba cargados')
"
```

## Estructura del Proyecto

```
autos_colombia/
├── app/
│   ├── __init__.py          # App factory
│   ├── models.py            # Modelos SQLAlchemy
│   ├── routes/              # Blueprints (controladores)
│   │   ├── main.py          # Dashboard
│   │   ├── movements.py     # Entradas/Salidas
│   │   ├── vehicles.py      # Vehículos
│   │   ├── users.py         # Usuarios
│   │   ├── cells.py         # Celdas
│   │   ├── payments.py      # Pagos
│   │   └── incidents.py     # Novedades
│   └── templates/           # Jinja2 HTML templates
├── database/
│   ├── schema.sql           # Modelo físico SQL
│   └── seed.sql             # Datos de prueba
├── docs/
│   ├── requerimientos.md    # RF y RNF
│   ├── historias_de_usuario.md
│   └── diagramas.md         # MER, MR, Clases, Casos de Uso
├── config.py
├── run.py
└── requirements.txt
```

## Tecnologías

| Componente | Tecnología |
|------------|-----------|
| Backend    | Python 3 + Flask |
| ORM        | SQLAlchemy |
| Base de Datos | SQLite (dev) / PostgreSQL (prod) |
| Frontend   | Jinja2 + Bootstrap 5 |
| Iconos     | Bootstrap Icons |

## Documentación Académica

Ver la carpeta `/docs/` para:
- Requerimientos funcionales y no funcionales
- Historias de usuario con criterios de aceptación
- Descripción de diagramas (UML, MER, MR)
- Modelo físico de base de datos (`database/schema.sql`)
