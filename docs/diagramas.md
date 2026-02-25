# Diagramas del Sistema — Parqueadero Autos Colombia
## Guía para StarUML y Figma

---

## 1. Arquitectura del Sistema (StarUML — Deployment Diagram)

```
┌─────────────────────────────────────────────────────┐
│                  CLIENTE (Navegador Web)              │
│         Chrome / Firefox / Edge — Bootstrap 5         │
└──────────────────────┬──────────────────────────────┘
                       │ HTTP/HTTPS
                       ▼
┌─────────────────────────────────────────────────────┐
│              SERVIDOR DE APLICACIÓN                   │
│                  Python 3.10+                         │
│  ┌────────────────────────────────────────────────┐  │
│  │           Flask Framework (MVC)                 │  │
│  │  ┌─────────────┐  ┌──────────────────────────┐ │  │
│  │  │  Templates   │  │  Blueprints (Controllers) │ │  │
│  │  │  (Jinja2)    │  │  - main, vehicles, users │ │  │
│  │  │  HTML + CSS  │  │  - cells, payments       │ │  │
│  │  └─────────────┘  │  - incidents, movements  │ │  │
│  │                   └──────────────────────────┘ │  │
│  │  ┌──────────────────────────────────────────┐  │  │
│  │  │     SQLAlchemy ORM (Models)               │  │  │
│  │  │  User | Vehicle | Cell | Movement        │  │  │
│  │  │  Payment | Incident                       │  │  │
│  │  └──────────────────────────────────────────┘  │  │
│  └────────────────────────────────────────────────┘  │
└──────────────────────┬──────────────────────────────┘
                       │ SQLAlchemy
                       ▼
┌─────────────────────────────────────────────────────┐
│              CAPA DE DATOS                            │
│              SQLite (desarrollo)                      │
│           PostgreSQL (producción)                     │
│                                                       │
│  Tablas: users, vehicles, cells, movements,           │
│          payments, incidents                          │
└─────────────────────────────────────────────────────┘
```

---

## 2. Diagrama de Paquetes (StarUML — Package Diagram)

```
autos_colombia/
├── «package» app/
│   ├── «package» routes/
│   │   ├── main.py
│   │   ├── vehicles.py
│   │   ├── users.py
│   │   ├── cells.py
│   │   ├── payments.py
│   │   ├── incidents.py
│   │   └── movements.py
│   ├── «package» templates/
│   │   ├── base.html
│   │   ├── index.html
│   │   ├── «package» vehicles/
│   │   ├── «package» users/
│   │   ├── «package» cells/
│   │   ├── «package» payments/
│   │   ├── «package» incidents/
│   │   └── «package» movements/
│   ├── «package» static/
│   │   ├── css/
│   │   └── js/
│   ├── __init__.py  (App Factory)
│   └── models.py
├── «package» database/
│   ├── schema.sql
│   └── seed.sql
├── «package» docs/
├── config.py
└── run.py
```

---

## 3. Diagrama de Clases (StarUML — Class Diagram)

### Clases del Dominio

```
┌──────────────────────────────────┐
│              User                │
├──────────────────────────────────┤
│ - id: Integer (PK)               │
│ - document: String [unique]      │
│ - full_name: String              │
│ - email: String [unique]         │
│ - phone: String                  │
│ - address: String                │
│ - is_active: Boolean             │
│ - created_at: DateTime           │
├──────────────────────────────────┤
│ + get_active_vehicles(): List    │
│ + get_payments(): List           │
└──────────────┬───────────────────┘
               │ 1
               │ owns
               │ *
┌──────────────▼───────────────────┐
│            Vehicle               │
├──────────────────────────────────┤
│ - id: Integer (PK)               │
│ - plate: String [unique]         │
│ - brand: String                  │
│ - model: String                  │
│ - year: Integer                  │
│ - color: String                  │
│ - vehicle_type: String           │
│ - is_active: Boolean             │
│ - registered_at: DateTime        │
│ - user_id: Integer (FK)          │
│ - cell_id: Integer (FK)          │
├──────────────────────────────────┤
│ + get_last_movement(): Movement  │
│ + is_inside(): Boolean           │
└───┬────────────────────┬─────────┘
    │ *                  │ *
    │ records            │ has
    │ 1                  │ 1
┌───▼──────────────┐  ┌──▼──────────────────────────┐
│    Movement      │  │          Cell                │
├──────────────────┤  ├─────────────────────────────┤
│ - id: Integer    │  │ - id: Integer (PK)           │
│ - movement_type  │  │ - number: String [unique]    │
│ - timestamp      │  │ - cell_type: String          │
│ - notes: String  │  │ - status: String             │
│ - vehicle_id     │  │ - floor: Integer             │
└──────────────────┘  │ - monthly_fee: Float         │
                      └─────────────────────────────┘

┌──────────────────────────────────┐
│           Payment                │
├──────────────────────────────────┤
│ - id: Integer (PK)               │
│ - amount: Float                  │
│ - payment_date: DateTime         │
│ - period_month: Integer          │
│ - period_year: Integer           │
│ - status: String                 │
│ - payment_method: String         │
│ - user_id: Integer (FK)          │
│ - vehicle_id: Integer (FK)       │
└──────────────────────────────────┘

┌──────────────────────────────────┐
│           Incident               │
├──────────────────────────────────┤
│ - id: Integer (PK)               │
│ - title: String                  │
│ - description: Text              │
│ - severity: String               │
│ - status: String                 │
│ - created_at: DateTime           │
│ - resolved_at: DateTime          │
│ - vehicle_id: Integer (FK)       │
├──────────────────────────────────┤
│ + resolve(): void                │
└──────────────────────────────────┘
```

---

## 4. Diagrama de Casos de Uso (StarUML — Use Case Diagram)

### Actores:
- **Operador**: Registra entradas, salidas y novedades
- **Administrador**: Acceso total al sistema
- **Sistema**: Realiza validaciones automáticas

### Casos de Uso Principales:

```
┌─────────────────────────────────────────────────────────┐
│              Sistema Parqueadero Autos Colombia          │
│                                                         │
│   (Registrar Entrada)    ◄── include ─── (Validar Placa)│
│   (Registrar Salida)     ◄── include ─── (Validar Placa)│
│   (Ver Movimientos)                                      │
│                                                         │
│   (Registrar Usuario)                                    │
│   (Editar Usuario)                                       │
│   (Desactivar Usuario)                                   │
│                                                         │
│   (Registrar Vehículo)   ◄── include ─── (Asignar Celda)│
│   (Editar Vehículo)                                      │
│                                                         │
│   (Ver Celdas)                                           │
│   (Crear Celda)                                          │
│   (Editar Celda)                                         │
│                                                         │
│   (Registrar Pago)       ◄── include ─── (Validar Período)│
│   (Ver Pagos)                                            │
│                                                         │
│   (Registrar Novedad)                                    │
│   (Resolver Novedad)                                     │
│                                                         │
│   (Ver Dashboard)                                        │
└──────────────┬──────────────────────────┬───────────────┘
               │                          │
        ┌──────┴──────┐           ┌───────┴──────┐
        │  Operador   │           │Administrador │
        └─────────────┘           └──────────────┘
```

---

## 5. Modelo Entidad-Relación (MER)

```
USERS ──< VEHICLES >── CELLS
  │           │
  │           ├──< MOVEMENTS
  │           ├──< INCIDENTS
  └──< PAYMENTS >── VEHICLES
```

### Entidades y Atributos:

**USERS**: {_id_, document, full_name, email, phone, address, is_active, created_at}  
**CELLS**: {_id_, number, cell_type, status, floor, monthly_fee}  
**VEHICLES**: {_id_, plate, brand, model, year, color, vehicle_type, is_active, registered_at, #user_id, #cell_id}  
**MOVEMENTS**: {_id_, movement_type, timestamp, notes, #vehicle_id}  
**PAYMENTS**: {_id_, amount, payment_date, period_month, period_year, status, payment_method, #user_id, #vehicle_id}  
**INCIDENTS**: {_id_, title, description, severity, status, created_at, resolved_at, #vehicle_id}  

### Cardinalidades:
- USERS (1,N) — VEHICLES: Un usuario puede tener varios vehículos
- CELLS (1,1) — VEHICLES: Una celda puede tener máximo un vehículo activo
- VEHICLES (1,N) — MOVEMENTS: Un vehículo puede tener muchos movimientos
- VEHICLES (1,N) — INCIDENTS: Un vehículo puede tener muchas novedades
- USERS (1,N) — PAYMENTS: Un usuario puede tener muchos pagos
- VEHICLES (0,N) — PAYMENTS: Un pago puede estar asociado a un vehículo

---

## 6. Modelo Relacional (MR)

```
users        (_id_, document, full_name, email, phone, address, is_active, created_at)
cells        (_id_, number, cell_type, status, floor, monthly_fee)
vehicles     (_id_, plate, brand, model, year, color, vehicle_type, is_active,
              registered_at, user_id→users.id, cell_id→cells.id)
movements    (_id_, movement_type, timestamp, notes, vehicle_id→vehicles.id)
payments     (_id_, amount, payment_date, period_month, period_year, status,
              payment_method, user_id→users.id, vehicle_id→vehicles.id)
incidents    (_id_, title, description, severity, status, created_at, resolved_at,
              vehicle_id→vehicles.id)
```

---

## 7. Mockups (Figma) — Descripción de Pantallas

### Pantalla 1: Dashboard
- Topbar con título y fecha
- Sidebar con navegación
- 4 tarjetas KPI superiores: Vehículos, Usuarios, Celdas disponibles, Recaudo
- 3 contadores: Entradas hoy, Salidas hoy, Novedades abiertas
- Tabla de últimos 10 movimientos
- Panel de acciones rápidas

### Pantalla 2: Registro de Entrada/Salida
- Formulario centrado
- Toggle visual Entrada/Salida con botones de radio estilizados en verde/rojo
- Campo grande de placa con letra mayúscula automática
- Tabla inferior con vehículos activos (clic para autocompletar placa)
- Botón "Registrar" prominente

### Pantalla 3: Lista de Movimientos
- Barra de filtros (tipo, placa)
- Tabla con badge de color: verde para entradas, rojo para salidas
- Paginación

### Pantalla 4: Lista de Celdas
- Resumen estadístico (3 tarjetas)
- Filtros por tipo, estado, piso
- Grid de tarjetas pequeñas representando las celdas
- Colores: verde = disponible, amarillo = ocupada
- Cada tarjeta muestra número, tipo, piso y tarifa

### Pantalla 5: Registro de Pago
- Selector de usuario con autocompletado de vehículos
- Al seleccionar vehículo, pre-pobla el monto
- Campos de período (mes/año), método de pago
- Validación en tiempo real
