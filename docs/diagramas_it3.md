# Diagramas — Iteración 3
## Parqueadero Autos Colombia

---

# PARTE 1: DIAGRAMA DE CASOS DE USO — ITERACIÓN 3

## Guía de construcción en StarUML

---

## Caso de Uso: Gestión de Pagos (CU-04)

### Actores involucrados:
- **Administrador** — Registra pagos y consulta el historial
- **Sistema** — Ejecuta auto-cálculo AJAX y validaciones automáticas

### Diagrama textual:

```
┌──────────────────────────────────────────────────────────────────┐
│              Sistema — Gestión de Pagos                           │
│                                                                   │
│   (Registrar Pago Mensual)  ◄──include── (Validar Período Único) │
│                             ◄──include── (Auto-calcular Tarifa)  │
│                                                                   │
│   (Consultar Historial de Pagos)                                  │
│                                                                   │
│   (Filtrar Pagos por Estado/Período)                              │
│       ◄──include── (Consultar Historial de Pagos)                 │
│                                                                   │
│   (Ver Recaudo Mensual en Dashboard)                             │
│                                                                   │
│   (Cargar Vehículos por Usuario) [AJAX]                          │
│       ◄──include── (Registrar Pago Mensual)                       │
│                                                                   │
└──────────────────────────────────┬───────────────────────────────┘
                                   │
                            ┌──────┴──────┐
                            │Administrador│
                            └─────────────┘
```

### Instrucciones para StarUML:

**Paso 1 — Crear el diagrama:**
- Abrir StarUML → Model Explorer → Add Diagram → Use Case Diagram
- Nombrar: "CU-04 Gestión de Pagos"

**Paso 2 — Agregar actores:**
- Actor: "Administrador"
- Actor: "Sistema"

**Paso 3 — Agregar el límite del sistema:**
- System Boundary → "Sistema Parqueadero — Módulo de Pagos"

**Paso 4 — Agregar casos de uso:**
| Nombre del Caso de Uso              | Actor principal        |
|-------------------------------------|------------------------|
| Registrar Pago Mensual              | Administrador          |
| Validar Período Único               | Sistema                |
| Auto-calcular Tarifa (AJAX)         | Sistema                |
| Cargar Vehículos por Usuario (AJAX) | Sistema                |
| Consultar Historial de Pagos        | Administrador          |
| Filtrar Pagos por Estado/Período    | Administrador          |
| Ver Recaudo Mensual en Dashboard    | Administrador          |

**Paso 5 — Agregar relaciones:**
| Origen                              | Destino                         | Tipo        |
|-------------------------------------|---------------------------------|-------------|
| Administrador                       | Registrar Pago Mensual          | Association |
| Registrar Pago Mensual              | Validar Período Único           | «include»   |
| Registrar Pago Mensual              | Auto-calcular Tarifa            | «include»   |
| Registrar Pago Mensual              | Cargar Vehículos por Usuario    | «include»   |
| Administrador                       | Consultar Historial de Pagos    | Association |
| Administrador                       | Filtrar Pagos por Estado/Período| Association |
| Filtrar Pagos por Estado/Período    | Consultar Historial de Pagos    | «include»   |
| Administrador                       | Ver Recaudo Mensual en Dashboard| Association |

---

---

# PARTE 2: DIAGRAMAS DE SECUENCIA ACTUALIZADOS — ITERACIONES 1, 2 Y 3

---

## DS-08 — Registrar Pago Mensual (Iteración 3)

### Participantes (lifelines):
- `:Administrador`
- `:PaymentsController` — Blueprint `payments.py`
- `:PaymentForm` — WTForms
- `:Payment` — Modelo SQLAlchemy
- `:Vehicle` — Modelo SQLAlchemy
- `:Database`

### Secuencia:

```
Administrador   PaymentsCtrl   PaymentForm    Vehicle       Payment      Database
      │               │               │            │              │             │
      │── GET /new ───►               │            │              │             │
      │◄── render form (usuarios) ────│            │              │             │
      │                               │            │              │             │
      │── [AJAX] GET /get_vehicles/<uid>►          │              │             │
      │               │── query(user_id) ──────────►              │             │
      │               │               │            │── SELECT ───────────────── ►│
      │               │               │            │◄── vehicles list ──────────  │
      │               │◄── [{plate, fee}] ─────────│              │             │
      │◄── JSON vehicles list ────────│            │              │             │
      │  (auto-fill monto) ← JS front │            │              │             │
      │                               │            │              │             │
      │── POST /new ──────────────────►            │              │             │
      │   (user, vehicle, month, year, amount, method)            │             │
      │               │── validate ───►            │              │             │
      │               │◄── valid:True │            │              │             │
      │               │               │            │              │             │
      │               │── check duplicado ─────────────────────── ►             │
      │               │               │            │              │── SELECT ───►│
      │               │               │            │              │◄── result ── │
      │               │◄── exists? ───────────────────────────────│             │
      │               │               │            │              │             │
      │   [Alt: pago duplicado]        │            │              │             │
      │◄── flash error ───────────────│            │              │             │
      │                               │            │              │             │
      │   [Normal: período disponible] │            │              │             │
      │               │── Payment(data, status='paid') ──────────►              │
      │               │── db.session.add() ────────────────────── ►             │
      │               │── db.commit() ──────────────────────────────────────────►│
      │◄── redirect /payments + flash success ───────────────────────────────    │
```

---

## DS-09 — Consultar Historial de Pagos con Filtros (Iteración 3)

### Participantes: `:Administrador`, `:PaymentsController`, `:Payment`, `:Database`

### Secuencia:

```
Administrador   PaymentsCtrl    Payment        Database
      │               │               │             │
      │── GET /payments/?status=paid&month=3&year=2026 ──►        │
      │               │               │             │
      │               │── query(filters) ──────────►              │
      │               │               │── SELECT WHERE ... ───────►│
      │               │               │◄── filtered list ──────── │
      │               │◄── payments [] ────────────│             │
      │               │── paginate(page, per_page) │             │
      │◄── render template (tabla paginada) ────────────────────   │
```

---

## DS-10 — Auto-calcular Tarifa (AJAX) (Iteración 3)

### Participantes: `:Administrador`, `:PaymentsController`, `:Vehicle`, `:Cell`, `:Database`

### Secuencia:

```
Administrador (JS)  PaymentsCtrl    Vehicle        Cell         Database
      │                   │               │             │              │
      │── fetch(/get_vehicles/<uid>) ──── ►             │              │
      │                   │── query vehicles(user_id) ──►              │
      │                   │               │── JOIN cells ──────────────►│
      │                   │               │◄── [{plate, fee}] ──────── │
      │                   │◄── vehicles + fees ────────│             │
      │                   │── return JSON([{plate, fee}]) ────────────  │
      │◄── JSON response ─│               │             │              │
      │  vehicleSelect.onChange → amountField.value = fee             │
```

---

## Resumen de todos los diagramas de secuencia del proyecto

| ID    | Nombre                                 | Iteración | Módulo               |
|-------|----------------------------------------|-----------|----------------------|
| DS-01 | Registrar Entrada de Vehículo          | 1         | Movimientos          |
| DS-02 | Registrar Salida de Vehículo           | 1         | Movimientos          |
| DS-03 | Registrar Nuevo Usuario                | 2         | Usuarios             |
| DS-04 | Editar Usuario                         | 2         | Usuarios             |
| DS-05 | Desactivar Usuario                     | 2         | Usuarios             |
| DS-06 | Crear Celda                            | 2         | Celdas               |
| DS-07 | Editar Celda                           | 2         | Celdas               |
| DS-08 | Registrar Pago Mensual                 | 3         | Pagos                |
| DS-09 | Consultar Historial con Filtros        | 3         | Pagos                |
| DS-10 | Auto-calcular Tarifa (AJAX)            | 3         | Pagos                |

---

---

# PARTE 3: DIAGRAMA DE COMPONENTES ACTUALIZADO — ITERACIONES 1, 2 Y 3

## Guía de construcción en StarUML

---

## DC-02 — Diagrama de Componentes Completo del Sistema (3 Iteraciones)

### Instrucciones StarUML:

1. Model Explorer → Add Diagram → Component Diagram
2. Nombrar: "DC-02 Componentes del Sistema — It1+It2+It3"

### Arquitectura completa:

```
┌──────────────────────────────────────────────────────────────────────────────┐
│                        «subsystem»                                            │
│                   Parqueadero Autos Colombia                                  │
│                                                                               │
│  ┌──────────────────────────────────────────────────────────────────────┐    │
│  │               «layer» Capa de Presentación (Templates Jinja2)        │    │
│  │                                                                        │    │
│  │  ┌───────────┐  ┌───────────┐  ┌─────────────┐  ┌─────────────────┐  │    │
│  │  │ base.html │  │index.html │  │users/       │  │cells/           │  │    │
│  │  │(Bootstrap)│  │(Dashboard)│  │templates/   │  │templates/       │  │    │
│  │  └───────────┘  └───────────┘  └─────────────┘  └─────────────────┘  │    │
│  │  ┌─────────────────┐  ┌──────────────────┐  ┌────────────────────┐   │    │
│  │  │vehicles/        │  │payments/         │  │movements/          │   │    │
│  │  │templates/       │  │templates/  [IT3] │  │incidents/templates │   │    │
│  │  └─────────────────┘  └──────────────────┘  └────────────────────┘   │    │
│  └──────────────────────────────────────┬─────────────────────────────────┘   │
│                                         │ uses                                │
│  ┌──────────────────────────────────────▼─────────────────────────────────┐   │
│  │               «layer» Capa de Control (Flask Blueprints)               │   │
│  │                                                                         │   │
│  │  ┌────────────┐  ┌────────────┐  ┌────────────┐  ┌──────────────────┐  │   │
│  │  │ «comp»     │  │ «comp»     │  │ «comp»     │  │ «comp»           │  │   │
│  │  │ main.py    │  │ users.py   │  │ cells.py   │  │ payments.py[IT3] │  │   │
│  │  │ (Dashboard)│  │ [IT2]      │  │ [IT2]      │  │                  │  │   │
│  │  └────────────┘  └────────────┘  └────────────┘  └──────────────────┘  │   │
│  │  ┌────────────┐  ┌────────────┐  ┌────────────┐                         │   │
│  │  │ «comp»     │  │ «comp»     │  │ «comp»     │                         │   │
│  │  │vehicles.py │  │movements.py│  │incidents.py│                         │   │
│  │  │ [IT1]      │  │ [IT1]      │  │ [IT1]      │                         │   │
│  │  └────────────┘  └────────────┘  └────────────┘                         │   │
│  └──────────────────────────────────────┬─────────────────────────────────┘   │
│                                         │ uses                                │
│  ┌──────────────────────────────────────▼─────────────────────────────────┐   │
│  │               «layer» Capa de Modelo (SQLAlchemy ORM)                  │   │
│  │                                                                         │   │
│  │  ┌──────────┐  ┌──────────┐  ┌──────────┐  ┌──────────────────────┐   │   │
│  │  │  «comp»  │  │  «comp»  │  │  «comp»  │  │       «comp»         │   │   │
│  │  │   User   │  │ Vehicle  │  │   Cell   │  │  Payment  [IT3]      │   │   │
│  │  │  [IT2]   │  │  [IT1]   │  │  [IT2]   │  │                      │   │   │
│  │  └──────────┘  └──────────┘  └──────────┘  └──────────────────────┘   │   │
│  │  ┌──────────┐  ┌──────────┐                                             │   │
│  │  │  «comp»  │  │  «comp»  │                                             │   │
│  │  │ Movement │  │ Incident │                                             │   │
│  │  │  [IT1]   │  │  [IT1]   │                                             │   │
│  │  └──────────┘  └──────────┘                                             │   │
│  └──────────────────────────────────────┬─────────────────────────────────┘   │
│                                         │ persists                            │
│  ┌──────────────────────────────────────▼─────────────────────────────────┐   │
│  │               «layer» Capa de Datos                                    │   │
│  │  ┌──────────────────────────┐  ┌──────────────────────────────────┐   │   │
│  │  │  SQLite (desarrollo)     │  │  PostgreSQL (producción)         │   │   │
│  │  │  autos_colombia.db       │  │  DATABASE_URL env var            │   │   │
│  │  └──────────────────────────┘  └──────────────────────────────────┘   │   │
│  └─────────────────────────────────────────────────────────────────────────┘   │
└──────────────────────────────────────────────────────────────────────────────┘
```

### Interfaces actualizadas (incluye Iteración 3):

| Componente Proveedor | Interfaz                | Componente Consumidor      |
|----------------------|-------------------------|----------------------------|
| users.py             | «interface» IUsuarios   | main.py (Dashboard)        |
| cells.py             | «interface» ICeldas     | main.py (Dashboard)        |
| cells.py             | «interface» ICeldas     | vehicles.py                |
| vehicles.py          | «interface» IVehiculos  | movements.py               |
| vehicles.py          | «interface» IVehiculos  | incidents.py               |
| vehicles.py          | «interface» IVehiculos  | payments.py                |
| users.py             | «interface» IUsuarios   | payments.py                |
| payments.py          | «interface» IPagos      | main.py (Dashboard)        |
| payments.py          | «interface» IPagos AJAX | payments.py (get_vehicles) |

---

---

# PARTE 4: MOCKUPS — ITERACIÓN 3

## Guía de diseño en Figma

---

## M-11 — Pantalla: Lista de Pagos (Historial)

### Especificaciones de diseño:

```
┌───────────────────────────────────────────────────────────────────────────┐
│ TOPBAR: [≡ Autos Colombia]                       [Operador logueado]      │
├──────┬────────────────────────────────────────────────────────────────────┤
│      │  Gestión de Pagos                           [+ Nuevo Pago]         │
│  S   │  ──────────────────────────────────────────────────────────────── │
│  I   │  Estado: [Todos ▼]   Mes: [Todos ▼]   Año: [2026 ▼]  [Filtrar]   │
│  D   │                                                                    │
│  E   │  ┌──────────────────────────────────────────────────────────────┐ │
│  B   │  │ Usuario    │ Placa   │ Período    │ Monto    │ Método │Estado │ │
│  A   │  ├──────────────────────────────────────────────────────────────┤ │
│  R   │  │ C. Pérez   │ ABC-123 │ Mar. 2026  │$150,000  │Efectivo│✅Pag.│ │
│      │  │ M. López   │ DEF-456 │ Mar. 2026  │$80,000   │Transf. │✅Pag.│ │
│      │  │ J. García  │ GHI-789 │ Feb. 2026  │$200,000  │Tarjeta │🟡Pend│ │
│      │  └──────────────────────────────────────────────────────────────┘ │
│      │  [← 1 2 3 →]   Mostrando 1-20 de 87 pagos                        │
└──────┴────────────────────────────────────────────────────────────────────┘
```

**Especificaciones de badges de estado:**
- Pagado: `badge bg-success` (#198754) texto blanco
- Pendiente: `badge bg-warning` (#ffc107) texto oscuro
- Vencido: `badge bg-danger` (#dc3545) texto blanco

---

## M-12 — Pantalla: Registrar Nuevo Pago

### Especificaciones de diseño:

```
┌───────────────────────────────────────────────────────────────────────────┐
│ TOPBAR                                                                    │
├──────┬────────────────────────────────────────────────────────────────────┤
│      │  Nuevo Pago                                                        │
│  S   │  ──────────────────────────────────────────────────────────────── │
│  I   │  ┌──────────────────────────────────────────────────────────────┐ │
│  D   │  │  ① Seleccionar Cliente                                        │ │
│  E   │  │  Usuario *                                                     │ │
│  B   │  │  [Carlos Pérez — Doc: 10234567                         ▼]     │ │
│  A   │  │                                                                │ │
│  R   │  │  ② Seleccionar Vehículo (carga automáticamente)               │ │
│      │  │  Vehículo *                                                    │ │
│      │  │  [ABC-123 — Toyota Corolla — Tarifa: $150,000          ▼]     │ │
│      │  │                                                                │ │
│      │  │  ③ Período y Pago                                             │ │
│      │  │  Mes *              │  Año *          │  Monto (COP) *        │ │
│      │  │  [Marzo      ▼]     │  [2026    ▼]    │  [$  150,000      ]   │ │
│      │  │                     │                 │  ⚡ Auto-calculado     │ │
│      │  │  Método de Pago *                                              │ │
│      │  │  ○ Efectivo   ○ Transferencia   ○ Tarjeta                     │ │
│      │  │                                                                │ │
│      │  │         [Cancelar]              [Registrar Pago]              │ │
│      │  └──────────────────────────────────────────────────────────────┘ │
└──────┴────────────────────────────────────────────────────────────────────┘
```

**Notas de UX:**
- El selector de vehículo está deshabilitado hasta que se seleccione un usuario.
- El ícono ⚡ indica que el monto fue auto-calculado desde la tarifa de celda.
- Si el vehículo no tiene celda asignada, el monto queda en blanco para ingreso manual.
- El formulario de radio buttons para método de pago usa Bootstrap `btn-group` estilizado.
- Los campos obligatorios están marcados con asterisco rojo `*`.

---

## M-13 — Dashboard con Recaudo Mensual (Actualizado)

### Especificaciones de diseño:

```
┌───────────────────────────────────────────────────────────────────────────┐
│ TOPBAR                                                                    │
├──────┬────────────────────────────────────────────────────────────────────┤
│      │  Dashboard — Parqueadero Autos Colombia                            │
│  S   │  ──────────────────────────────────────────────────────────────── │
│  I   │  ┌────────────┐ ┌────────────┐ ┌────────────┐ ┌────────────────┐ │
│  D   │  │🚗 Vehículos│ │👤 Usuarios │ │🅿️ Disponib.│ │💰 Recaudo Mes  │ │
│  E   │  │     45     │ │     32     │ │     28     │ │  $3'750,000    │ │
│  B   │  └────────────┘ └────────────┘ └────────────┘ └────────────────┘ │
│  A   │  ┌───────────────┐ ┌────────────────┐ ┌─────────────────────────┐│
│  R   │  │📥 Entradas hoy│ │📤 Salidas hoy  │ │⚠️ Novedades abiertas    ││
│      │  │      12       │ │      10        │ │          3              ││
│      │  └───────────────┘ └────────────────┘ └─────────────────────────┘│
│      │                                                                    │
│      │  Últimos 10 movimientos          Acciones rápidas                  │
│      │  ┌──────────────────────────┐   ┌────────────────────────────┐    │
│      │  │ [tabla de movimientos]   │   │ [+ Entrada] [+ Salida]     │    │
│      │  │                          │   │ [+ Usuario] [+ Pago]       │    │
│      │  └──────────────────────────┘   └────────────────────────────┘    │
└──────┴────────────────────────────────────────────────────────────────────┘
```

**Especificación de la tarjeta de recaudo:**
- Fondo: `#198754` (Bootstrap success verde) con texto blanco
- Valor en formato `$X,XXX,XXX` con separadores de miles
- Subtexto: "Recaudo del mes actual"
- Icono: 💰 o `bi-currency-dollar` de Bootstrap Icons
