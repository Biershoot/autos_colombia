# 🏢 Parqueadero Autos Colombia

Sistema web de gestión operativa para parqueaderos con servicio de mensualidad. Desarrollado como proyecto académico en la asignatura de **Ingeniería de Software y Datos**, completando las 3 iteraciones del ciclo de desarrollo.

---

## ¿Qué hace el sistema?

El parqueadero **Autos Colombia** opera bajo un modelo de mensualidad fija: cada cliente registra sus vehículos y se le asigna una celda dentro de las instalaciones. El sistema reemplaza los registros manuales en papel con una interfaz web que centraliza toda la operación diaria.

| Módulo | Descripción |
|--------|-------------|
| 📊 **Dashboard** | Métricas en tiempo real: vehículos, usuarios, celdas, recaudo mensual |
| 🚗 **Entradas y Salidas** | Registro de movimientos con validaciones de doble entrada/salida |
| 👤 **Usuarios** | CRUD de clientes con historial de vehículos y pagos |
| 🅿️ **Celdas** | Vista visual en grid con estado disponible/ocupada por piso |
| 🚙 **Vehículos** | Registro con asignación automática de celda disponible |
| 💰 **Pagos** | Mensualidades con auto-cálculo de tarifa vía AJAX |
| ⚠️ **Novedades** | Registro y seguimiento de incidentes por vehículo |

---

## Stack Tecnológico

| Capa | Tecnología |
|------|-----------|
| Backend | Python 3.10+ · Flask 3.0 |
| ORM | SQLAlchemy 3.1 |
| Formularios | Flask-WTF · WTForms |
| Base de datos | SQLite (desarrollo) · PostgreSQL (producción) |
| Frontend | Jinja2 · Bootstrap 5 · Bootstrap Icons |
| Arquitectura | MVC — Blueprints + Models + Templates |

---

## Instalación

**Requisitos:** Python 3.10 o superior

```bash
# 1. Clonar el repositorio
git clone https://github.com/Biershoot/autos_colombia.git
cd autos_colombia

# 2. Instalar dependencias
pip install -r requirements.txt

# 3. Ejecutar
python run.py
```

Abrir en el navegador: **http://localhost:5000**

La base de datos SQLite se crea automáticamente con celdas preconfiguradas (3 pisos × 3 tipos).

### Cargar datos de prueba (opcional)

```bash
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
print('Datos de prueba cargados.')
"
```

---

## Estructura del Proyecto

```
autos_colombia/
├── app/
│   ├── __init__.py          # App factory + registro de blueprints + seed de celdas
│   ├── models.py            # Modelos SQLAlchemy: User, Vehicle, Cell, Movement, Payment, Incident
│   ├── routes/
│   │   ├── main.py          # Dashboard con métricas
│   │   ├── movements.py     # Entradas y salidas
│   │   ├── vehicles.py      # Gestión de vehículos
│   │   ├── users.py         # Gestión de usuarios
│   │   ├── cells.py         # Gestión de celdas
│   │   ├── payments.py      # Gestión de pagos (incluye endpoint AJAX)
│   │   └── incidents.py     # Gestión de novedades
│   └── templates/           # Templates Jinja2 por módulo
├── database/
│   ├── schema.sql           # DDL — modelo físico de base de datos
│   └── seed.sql             # Datos de prueba
├── docs/                    # Documentación académica por iteración
│   ├── requerimientos.md         # It1: RF-01 a RF-09, RNF-01 a RNF-08
│   ├── historias_de_usuario.md   # It1: HU-01 a HU-09
│   ├── diagramas.md              # It1: UML, MER, MR, Casos de Uso
│   ├── requerimientos_it2.md     # It2: RF-10 a RF-18, RNF-09 a RNF-15
│   ├── historias_it2.md          # It2: HU-10 a HU-17
│   ├── diagramas_it2.md          # It2: Casos de uso, secuencia, componentes, mockups
│   ├── plan_de_pruebas_it2.md    # It2: 20 casos de prueba
│   ├── requerimientos_it3.md     # It3: RF-19 a RF-25, RNF-16 a RNF-21
│   ├── historias_it3.md          # It3: HU-18 a HU-23
│   ├── diagramas_it3.md          # It3: Casos de uso, secuencia, componentes, mockups
│   ├── plan_de_pruebas_it3.md    # It3: 12 casos de prueba
│   ├── informe_iteracion2.html   # Informe completo It2 (abrir en Chrome → PDF)
│   └── informe_iteracion3.html   # Informe completo It3 (abrir en Chrome → PDF)
├── config.py
├── run.py
└── requirements.txt
```

---

## Iteraciones del Proyecto

| Iteración | Módulos | Historias | Puntos |
|-----------|---------|-----------|--------|
| **It1** — Entradas/Salidas | Movimientos · Dashboard · Vehículos · Novedades | HU-01 a HU-09 | 22 |
| **It2** — Usuarios y Celdas | Gestión de Usuarios · Gestión de Celdas | HU-10 a HU-17 | 18 |
| **It3** — Pagos | Gestión de Pagos (con AJAX) | HU-18 a HU-23 | 12 |
| **Total** | 7 módulos | 23 historias | **52 puntos** |

---

## Generar informes PDF

Los informes de cada iteración están en `docs/` como archivos HTML. Para convertirlos a PDF:

1. Abrir el archivo en **Google Chrome**
2. `Ctrl + P` → **Guardar como PDF**
3. Activar **"Gráficos de fondo"** · Desmarcar **"Encabezados y pies de página"**
