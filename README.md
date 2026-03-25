# 🏢 Parqueadero Autos Colombia

![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=flat&logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-3.0-000000?style=flat&logo=flask&logoColor=white)
![Bootstrap](https://img.shields.io/badge/Bootstrap-5-7952B3?style=flat&logo=bootstrap&logoColor=white)
![SQLite](https://img.shields.io/badge/SQLite-003B57?style=flat&logo=sqlite&logoColor=white)
![License](https://img.shields.io/badge/Uso-Académico-orange?style=flat)

Sistema web de gestión operativa para parqueaderos con servicio de mensualidad, desarrollado en **3 iteraciones** como proyecto de la asignatura **Ingeniería de Software y Datos**.

---

## Descripción

El parqueadero **Autos Colombia** opera bajo un modelo de mensualidad fija: cada cliente registra sus vehículos y se le asigna una celda dentro de las instalaciones. El sistema reemplaza los registros manuales en papel con una aplicación web centralizada que cubre toda la operación diaria.

---

## Funcionalidades

| Módulo | Descripción |
|--------|-------------|
| 📊 **Dashboard** | KPIs en tiempo real: vehículos activos, usuarios, celdas disponibles y recaudo mensual |
| 🚗 **Entradas y Salidas** | Registro de movimientos con validaciones (no doble entrada, no salida sin entrada) |
| 👤 **Usuarios** | CRUD de clientes con historial de vehículos y pagos asociados |
| 🅿️ **Celdas** | Panel visual en grid con estado disponible/ocupada, filtros por piso y tipo |
| 🚙 **Vehículos** | Registro completo con asignación de celda disponible |
| 💰 **Pagos** | Mensualidades con auto-cálculo de tarifa vía AJAX y prevención de duplicados |
| ⚠️ **Novedades** | Registro y seguimiento de incidentes por vehículo con niveles de severidad |

---

## Stack Tecnológico

| Capa | Tecnología |
|------|-----------|
| Backend | Python 3.10+ · Flask 3.0 · Flask-WTF |
| ORM | SQLAlchemy 3.1 |
| Base de datos | SQLite (desarrollo) · PostgreSQL (producción) |
| Frontend | Jinja2 · Bootstrap 5 · Bootstrap Icons |
| Arquitectura | MVC — Blueprints + Models + Templates |

---

## Instalación y Ejecución

**Requisito:** Python 3.10 o superior

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

> La base de datos SQLite se crea automáticamente en `database/autos_colombia.db` con celdas preconfiguradas en 3 pisos × 3 tipos (carro, moto, camión).

### Cargar datos de prueba

```bash
python -c "
from app import create_app, db
app = create_app()
with app.app_context():
    with open('database/seed.sql') as f:
        from sqlalchemy import text
        for stmt in f.read().split(';'):
            stmt = stmt.strip()
            if stmt:
                try: db.session.execute(text(stmt))
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
│   ├── __init__.py          # App factory · registro de blueprints · seed de celdas
│   ├── models.py            # User · Vehicle · Cell · Movement · Payment · Incident
│   ├── routes/
│   │   ├── main.py          # Dashboard
│   │   ├── movements.py     # Entradas y salidas
│   │   ├── users.py         # Usuarios
│   │   ├── cells.py         # Celdas
│   │   ├── vehicles.py      # Vehículos
│   │   ├── payments.py      # Pagos + endpoint AJAX /get_vehicles/<id>
│   │   └── incidents.py     # Novedades
│   └── templates/           # Templates Jinja2 organizados por módulo
├── database/
│   ├── schema.sql           # DDL completo con índices
│   └── seed.sql             # Datos de prueba
├── docs/                    # Documentación académica
├── config.py
├── run.py
└── requirements.txt
```

---

## Documentación Académica

La carpeta `docs/` contiene todos los artefactos de análisis y diseño del proyecto organizados por iteración.

### Iteración 1 — Entradas, Salidas y Dashboard
| Archivo | Contenido |
|---------|-----------|
| `requerimientos.md` | RF-01 a RF-09 · RNF-01 a RNF-08 |
| `historias_de_usuario.md` | HU-01 a HU-09 con criterios de aceptación |

### Iteración 2 — Usuarios y Celdas
| Archivo | Contenido |
|---------|-----------|
| `requerimientos_it2.md` | RF-10 a RF-18 · RNF-09 a RNF-15 |
| `historias_it2.md` | HU-10 a HU-17 con criterios de aceptación |
| `plan_de_pruebas_it2.md` | 20 casos de prueba con matriz de trazabilidad |
| `informe_iteracion2.html` | Informe completo listo para exportar a PDF |

### Iteración 3 — Gestión de Pagos
| Archivo | Contenido |
|---------|-----------|
| `requerimientos_it3.md` | RF-19 a RF-25 · RNF-16 a RNF-21 |
| `historias_it3.md` | HU-18 a HU-23 con criterios de aceptación |
| `plan_de_pruebas_it3.md` | 12 casos de prueba con matriz de trazabilidad |
| `informe_iteracion3.html` | Informe completo listo para exportar a PDF |

### Resumen del Proyecto

| Iteración | Módulos | Historias | Puntos |
|-----------|---------|:---------:|:------:|
| It1 | Movimientos · Dashboard · Vehículos · Novedades | HU-01–09 | 22 |
| It2 | Usuarios · Celdas | HU-10–17 | 18 |
| It3 | Pagos | HU-18–23 | 12 |
| **Total** | **7 módulos** | **23** | **52** |

### Generar informes PDF

1. Abrir `docs/informe_iteracion2.html` o `docs/informe_iteracion3.html` en **Google Chrome**
2. `Ctrl + P` → **Guardar como PDF**
3. Activar **"Gráficos de fondo"** · Desmarcar **"Encabezados y pies de página"**
