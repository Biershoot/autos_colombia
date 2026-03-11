# Diagramas — Iteración 2
## Parqueadero Autos Colombia

---

# PARTE 1: DIAGRAMAS DE CASOS DE USO — ITERACIÓN 2

## Guía de construcción en StarUML

---

## Caso de Uso: Gestión de Usuarios

### Actores involucrados:
- **Administrador** — Actor principal con acceso completo al módulo de usuarios
- **Sistema** — Realiza validaciones automáticas en segundo plano

### Casos de uso a modelar:

```
┌──────────────────────────────────────────────────────────────┐
│           Sistema — Gestión de Usuarios                       │
│                                                               │
│   (Registrar Usuario)   ◄──include──  (Validar Unicidad       │
│                                        Documento/Correo)      │
│                                                               │
│   (Buscar Usuario)                                            │
│                                                               │
│   (Ver Perfil de Usuario)                                     │
│                                                               │
│   (Editar Usuario)      ◄──include──  (Validar Correo Único) │
│                                                               │
│   (Desactivar Usuario)  ◄──include──  (Verificar Vehículos   │
│                                        Activos)               │
│                                ◄──extend── (Reactivar Usuario)│
│                                                               │
└──────────────────────────────┬───────────────────────────────┘
                               │
                        ┌──────┴──────┐
                        │Administrador│
                        └─────────────┘
```

### Instrucciones para StarUML:

**Paso 1 — Crear el diagrama:**
- Abrir StarUML → File → New → Model
- Agregar un diagrama: Model Explorer → clic derecho → Add Diagram → Use Case Diagram
- Nombrar: "CU-02 Gestión de Usuarios"

**Paso 2 — Agregar actores:**
- Herramienta `Actor` → clic en el lienzo → escribir "Administrador"
- Herramienta `Actor` → clic en el lienzo → escribir "Sistema"

**Paso 3 — Agregar el límite del sistema:**
- Herramienta `System Boundary` → dibujar un rectángulo grande
- Doble clic → escribir "Sistema Parqueadero — Módulo de Usuarios"

**Paso 4 — Agregar casos de uso (dentro del límite):**
| Nombre del Caso de Uso         | Tipo         |
|--------------------------------|--------------|
| Registrar Usuario              | Use Case     |
| Validar Unicidad Documento     | Use Case     |
| Buscar Usuario                 | Use Case     |
| Ver Perfil de Usuario          | Use Case     |
| Editar Usuario                 | Use Case     |
| Validar Correo Único           | Use Case     |
| Desactivar Usuario             | Use Case     |
| Verificar Vehículos Activos    | Use Case     |
| Reactivar Usuario              | Use Case     |

**Paso 5 — Agregar relaciones:**
| Origen                     | Destino                         | Tipo         |
|----------------------------|---------------------------------|--------------|
| Administrador              | Registrar Usuario               | Association  |
| Registrar Usuario          | Validar Unicidad Documento      | «include»    |
| Administrador              | Buscar Usuario                  | Association  |
| Administrador              | Ver Perfil de Usuario           | Association  |
| Administrador              | Editar Usuario                  | Association  |
| Editar Usuario             | Validar Correo Único            | «include»    |
| Administrador              | Desactivar Usuario              | Association  |
| Desactivar Usuario         | Verificar Vehículos Activos     | «include»    |
| Reactivar Usuario          | Desactivar Usuario              | «extend»     |

---

## Caso de Uso: Gestión de Celdas

### Actores involucrados:
- **Administrador** — Acceso completo (crear, editar, visualizar)
- **Operador** — Acceso de solo visualización
- **Sistema** — Actualiza estados automáticamente

### Casos de uso a modelar:

```
┌──────────────────────────────────────────────────────────────┐
│           Sistema — Gestión de Celdas                        │
│                                                               │
│   (Crear Celda)         ◄──include──  (Validar Número         │
│                                        Único)                 │
│                                                               │
│   (Editar Celda)                                             │
│                                                               │
│   (Visualizar Panel de Celdas)                               │
│                                                               │
│   (Filtrar Celdas)      ◄──include──  (Visualizar Panel       │
│                                        de Celdas)             │
│                                                               │
│   (Asignar Celda a Vehículo) ◄──include── (Verificar          │
│                                            Disponibilidad)    │
│                                                               │
│   (Liberar Celda)                                            │
│       ◄──extend── (Desactivar Vehículo)                       │
│                                                               │
└───────────────────────────┬──────────────────────────────────┘
                            │
              ┌─────────────┴─────────────┐
              │                           │
       ┌──────┴──────┐             ┌──────┴──────┐
       │Administrador│             │  Operador   │
       └─────────────┘             └─────────────┘
```

### Instrucciones para StarUML:

**Paso 1 — Crear el diagrama:**
- Agregar un diagrama nuevo: Use Case Diagram
- Nombrar: "CU-03 Gestión de Celdas"

**Paso 2 — Agregar actores:**
- Actor: "Administrador"
- Actor: "Operador"
- Actor: "Sistema" (opcional, representa automatismos)

**Paso 3 — Agregar el límite del sistema:**
- System Boundary → "Sistema Parqueadero — Módulo de Celdas"

**Paso 4 — Agregar casos de uso:**
| Nombre del Caso de Uso          | Accesible por        |
|---------------------------------|----------------------|
| Crear Celda                     | Administrador        |
| Validar Número Único            | Sistema              |
| Editar Celda                    | Administrador        |
| Visualizar Panel de Celdas      | Administrador, Operador |
| Filtrar Celdas                  | Administrador, Operador |
| Asignar Celda a Vehículo        | Administrador        |
| Verificar Disponibilidad        | Sistema              |
| Liberar Celda                   | Sistema              |

**Paso 5 — Agregar relaciones:**
| Origen                      | Destino                    | Tipo         |
|-----------------------------|----------------------------|--------------|
| Administrador               | Crear Celda                | Association  |
| Crear Celda                 | Validar Número Único       | «include»    |
| Administrador               | Editar Celda               | Association  |
| Administrador               | Visualizar Panel de Celdas | Association  |
| Operador                    | Visualizar Panel de Celdas | Association  |
| Administrador               | Filtrar Celdas             | Association  |
| Operador                    | Filtrar Celdas             | Association  |
| Filtrar Celdas              | Visualizar Panel de Celdas | «include»    |
| Administrador               | Asignar Celda a Vehículo   | Association  |
| Asignar Celda a Vehículo    | Verificar Disponibilidad   | «include»    |
| Liberar Celda               | Asignar Celda a Vehículo   | «extend»     |

---

---

# PARTE 2: DIAGRAMAS DE SECUENCIA — ITERACIONES 1 Y 2

## Guía de construcción en StarUML

---

## DS-01 — Registrar Entrada de Vehículo (Iteración 1)

### Participantes (lifelines):
- `:Operador` — Actor externo
- `:MovimientosController` — Blueprint Flask `movements.py`
- `:Vehicle` — Modelo SQLAlchemy
- `:Movement` — Modelo SQLAlchemy
- `:Cell` — Modelo SQLAlchemy
- `:Database` — Capa de persistencia

### Secuencia:

```
Operador          MovimientosCtrl    Vehicle        Movement       Cell         Database
   │                    │               │               │              │              │
   │── POST /register ──►               │               │              │              │
   │     (placa, tipo)  │               │               │              │              │
   │                    │── query(placa)►               │              │              │
   │                    │               │── SELECT ─────────────────────────────────► │
   │                    │               │◄── vehicle obj ──────────────────────────── │
   │                    │◄── vehicle ───│               │              │              │
   │                    │               │               │              │              │
   │                    │── check last movement ────────►              │              │
   │                    │               │◄── last_movement ────────────│              │
   │                    │               │               │              │              │
   │   [Alt: ya existe entrada activa]  │               │              │              │
   │◄── flash warning ──│               │               │              │              │
   │                    │               │               │              │              │
   │   [Normal: no hay entrada activa]  │               │              │              │
   │                    │── create() ───────────────────►              │              │
   │                    │               │               │── INSERT ──────────────────►│
   │                    │               │               │◄── ok ───────────────────── │
   │                    │               │               │              │              │
   │                    │── update status('ocupada') ──────────────────►              │
   │                    │               │               │              │── UPDATE ───►│
   │                    │               │               │              │◄── ok ─────  │
   │                    │── db.commit() ─────────────────────────────────────────────►│
   │◄── redirect + flash success ──────────────────────────────────────────────────   │
```

### Instrucciones StarUML:

1. Model Explorer → Add Diagram → Sequence Diagram → "DS-01 Registrar Entrada"
2. Agregar `Lifeline` para cada participante listado arriba
3. Usar `Message` (flecha sólida) para llamadas síncronas
4. Usar `Return Message` (flecha punteada) para respuestas
5. Usar `Combined Fragment` tipo `alt` para modelar el flujo alternativo

---

## DS-02 — Registrar Salida de Vehículo (Iteración 1)

### Participantes: `:Operador`, `:MovimientosController`, `:Vehicle`, `:Movement`, `:Cell`, `:Database`

### Secuencia simplificada:

```
Operador          MovimientosCtrl    Vehicle        Movement       Cell         Database
   │                    │               │               │              │              │
   │── POST /register ──►               │               │              │              │
   │   (placa, salida)  │               │               │              │              │
   │                    │── query(placa)►               │               │             │
   │                    │◄── vehicle ───│               │              │              │
   │                    │── get last entry ─────────────►              │              │
   │                    │◄── last_movement ─────────────│              │              │
   │                    │               │               │              │              │
   │   [Alt: no hay entrada sin salida] │               │              │              │
   │◄── flash warning ──│               │               │              │              │
   │                    │               │               │              │              │
   │   [Normal: hay entrada sin salida] │               │              │              │
   │                    │── create(exit) ───────────────►              │              │
   │                    │               │               │── INSERT ──────────────────►│
   │                    │── update status('disponible') ──────────────►              │
   │                    │── db.commit() ─────────────────────────────────────────────►│
   │◄── redirect + flash success ──────│               │              │              │
```

---

## DS-03 — Registrar Nuevo Usuario (Iteración 2)

### Participantes:
- `:Administrador`
- `:UsersController` — Blueprint `users.py`
- `:UserForm` — WTForms
- `:User` — Modelo SQLAlchemy
- `:Database`

### Secuencia:

```
Administrador    UsersController    UserForm         User          Database
      │                 │               │               │               │
      │── GET /new ─────►               │               │               │
      │◄── render form ─│               │               │               │
      │                 │               │               │               │
      │── POST /new ────►               │               │               │
      │   (form data)   │── validate ──►│               │               │
      │                 │               │── check rules │               │
      │                 │◄── valid: True│               │               │
      │                 │               │               │               │
      │                 │── query(document) ────────────►               │
      │                 │               │               │── SELECT ─────►│
      │                 │               │               │◄── result ──── │
      │                 │◄── exists? ───────────────────│               │
      │                 │               │               │               │
      │   [Alt: documento duplicado]    │               │               │
      │◄── flash error ─│               │               │               │
      │◄── re-render ───│               │               │               │
      │                 │               │               │               │
      │   [Alt: correo duplicado]       │               │               │
      │◄── flash error ─│               │               │               │
      │                 │               │               │               │
      │   [Normal: datos únicos]        │               │               │
      │                 │── User(data) ─────────────────►               │
      │                 │── db.session.add() ────────────►              │
      │                 │── db.commit() ─────────────────────────────── ►│
      │                 │◄── user.id ───────────────────│               │
      │◄── redirect /detail + flash success ──────────────────────────  │
```

---

## DS-04 — Editar Usuario (Iteración 2)

### Participantes: `:Administrador`, `:UsersController`, `:UserForm`, `:User`, `:Database`

### Secuencia:

```
Administrador    UsersController    UserForm         User          Database
      │                 │               │               │               │
      │── GET /<id>/edit►               │               │               │
      │                 │── query(id) ──────────────────►               │
      │                 │               │               │── SELECT ─────►│
      │                 │◄── user obj ──────────────────│               │
      │◄── render form pre-cargado ─────│               │               │
      │                 │               │               │               │
      │── POST /<id>/edit►              │               │               │
      │   (datos nuevos)│── validate ──►│               │               │
      │                 │◄── valid: True│               │               │
      │                 │               │               │               │
      │                 │── check email único (excluyendo mismo id) ─────►│
      │                 │◄── sin conflicto ─────────────────────────────  │
      │                 │               │               │               │
      │                 │── user.full_name = ... ────────►               │
      │                 │── user.phone = ... ────────────►               │
      │                 │── user.email = ... ────────────►               │
      │                 │── db.commit() ─────────────────────────────────►│
      │◄── redirect /detail + flash success ──────────────────────────   │
```

---

## DS-05 — Desactivar Usuario (Iteración 2)

### Participantes: `:Administrador`, `:UsersController`, `:User`, `:Vehicle`, `:Database`

### Secuencia:

```
Administrador    UsersController    User           Vehicle        Database
      │                 │               │               │               │
      │── POST /<id>/deactivate ────────►               │               │
      │                 │── query(id) ──►               │               │
      │                 │◄── user obj ──│               │               │
      │                 │               │               │               │
      │                 │── check active vehicles ──────►               │
      │                 │               │               │── SELECT ─────►│
      │                 │               │               │◄── count ───── │
      │                 │◄── active_count ──────────────│               │
      │                 │               │               │               │
      │   [Alt: tiene vehículos activos]│               │               │
      │◄── flash warning + redirect ───────────────────────────────     │
      │                 │               │               │               │
      │   [Normal: sin vehículos activos]               │               │
      │                 │── user.is_active = False ──────►               │
      │                 │── db.commit() ─────────────────────────────────►│
      │◄── redirect /users + flash success ───────────────────────────   │
```

---

## DS-06 — Crear Celda (Iteración 2)

### Participantes: `:Administrador`, `:CellsController`, `:CellForm`, `:Cell`, `:Database`

### Secuencia:

```
Administrador    CellsController    CellForm          Cell         Database
      │                 │               │               │               │
      │── GET /new ─────►               │               │               │
      │◄── render form ─│               │               │               │
      │                 │               │               │               │
      │── POST /new ────►               │               │               │
      │   (number, type, floor, fee)    │               │               │
      │                 │── validate ──►│               │               │
      │                 │◄── valid: True│               │               │
      │                 │               │               │               │
      │                 │── query(number) ──────────────►               │
      │                 │               │               │── SELECT ─────►│
      │                 │               │               │◄── result ──── │
      │                 │◄── exists? ───────────────────│               │
      │                 │               │               │               │
      │   [Alt: número duplicado]       │               │               │
      │◄── flash error + re-render ─────│               │               │
      │                 │               │               │               │
      │   [Normal: número disponible]   │               │               │
      │                 │── Cell(data, status='available') ──────────────►│
      │                 │── db.session.add() ────────────►              │
      │                 │── db.commit() ─────────────────────────────────►│
      │◄── redirect /cells + flash success ───────────────────────────   │
```

---

## DS-07 — Editar Celda (Iteración 2)

### Participantes: `:Administrador`, `:CellsController`, `:CellForm`, `:Cell`, `:Database`

### Secuencia:

```
Administrador    CellsController    CellForm          Cell         Database
      │                 │               │               │               │
      │── GET /<id>/edit►               │               │               │
      │                 │── query(id) ──────────────────►               │
      │                 │               │               │── SELECT ─────►│
      │                 │◄── cell obj ──────────────────│               │
      │◄── render form pre-cargado ─────│               │               │
      │                 │               │               │               │
      │── POST /<id>/edit►              │               │               │
      │   (type, floor, fee)│── validate►               │               │
      │                 │◄── valid: True│               │               │
      │                 │── cell.cell_type = ... ────────►               │
      │                 │── cell.floor = ... ────────────►               │
      │                 │── cell.monthly_fee = ... ──────►               │
      │                 │── db.commit() ─────────────────────────────────►│
      │◄── redirect /cells + flash success ───────────────────────────   │
```

---

---

# PARTE 3: DIAGRAMA DE COMPONENTES — ITERACIONES 1 Y 2

## Guía de construcción en StarUML

---

## DC-01 — Diagrama de Componentes del Sistema

### Instrucciones StarUML:

1. Model Explorer → Add Diagram → Component Diagram
2. Nombrar: "DC-01 Componentes del Sistema"

### Componentes a modelar:

```
┌─────────────────────────────────────────────────────────────────────┐
│                     «subsystem»                                      │
│                   Parqueadero Autos Colombia                         │
│                                                                      │
│  ┌─────────────────────────────────────────────────────────────┐    │
│  │               «component»                                    │    │
│  │           Capa de Presentación (Templates)                   │    │
│  │  ┌──────────────┐  ┌─────────────┐  ┌────────────────────┐  │    │
│  │  │  «component» │  │ «component» │  │    «component»     │  │    │
│  │  │ base.html    │  │ index.html  │  │  users/ templates  │  │    │
│  │  └──────────────┘  └─────────────┘  └────────────────────┘  │    │
│  │  ┌────────────────────┐  ┌────────────────────────────────┐  │    │
│  │  │    «component»     │  │         «component»            │  │    │
│  │  │ cells/ templates   │  │  vehicles, payments, movements │  │    │
│  │  └────────────────────┘  │  incidents/ templates          │  │    │
│  │                          └────────────────────────────────┘  │    │
│  └──────────────────────────────┬──────────────────────────────┘    │
│                                 │ uses                               │
│  ┌──────────────────────────────▼──────────────────────────────┐    │
│  │               «component»                                    │    │
│  │            Capa de Control (Blueprints)                      │    │
│  │                                                              │    │
│  │  ┌─────────────┐  ┌─────────────┐  ┌─────────────────────┐  │    │
│  │  │ «component» │  │ «component» │  │     «component»     │  │    │
│  │  │  main.py    │  │  users.py   │  │      cells.py       │  │    │
│  │  │  (Dashboard)│  │             │  │                     │  │    │
│  │  └─────────────┘  └─────────────┘  └─────────────────────┘  │    │
│  │  ┌─────────────┐  ┌─────────────┐  ┌─────────────────────┐  │    │
│  │  │ «component» │  │ «component» │  │     «component»     │  │    │
│  │  │ vehicles.py │  │ payments.py │  │  movements.py       │  │    │
│  │  └─────────────┘  └─────────────┘  └─────────────────────┘  │    │
│  │  ┌─────────────┐                                             │    │
│  │  │ «component» │                                             │    │
│  │  │incidents.py │                                             │    │
│  │  └─────────────┘                                             │    │
│  └──────────────────────────────┬──────────────────────────────┘    │
│                                 │ uses                               │
│  ┌──────────────────────────────▼──────────────────────────────┐    │
│  │               «component»                                    │    │
│  │              Capa de Modelo (ORM)                            │    │
│  │                                                              │    │
│  │  ┌──────────┐  ┌──────────┐  ┌──────────┐  ┌────────────┐  │    │
│  │  │  «comp»  │  │  «comp»  │  │  «comp»  │  │   «comp»   │  │    │
│  │  │   User   │  │ Vehicle  │  │   Cell   │  │  Movement  │  │    │
│  │  └──────────┘  └──────────┘  └──────────┘  └────────────┘  │    │
│  │  ┌──────────┐  ┌──────────┐                                  │    │
│  │  │  «comp»  │  │  «comp»  │                                  │    │
│  │  │ Payment  │  │ Incident │                                  │    │
│  │  └──────────┘  └──────────┘                                  │    │
│  └──────────────────────────────┬──────────────────────────────┘    │
│                                 │ persists                           │
│  ┌──────────────────────────────▼──────────────────────────────┐    │
│  │               «component»                                    │    │
│  │              Capa de Datos (Database)                        │    │
│  │                                                              │    │
│  │  ┌──────────────────────────┐  ┌──────────────────────────┐  │    │
│  │  │       «component»        │  │       «component»        │  │    │
│  │  │  SQLite (desarrollo)     │  │  PostgreSQL (producción) │  │    │
│  │  │  autos_colombia.db       │  │  DATABASE_URL env var    │  │    │
│  │  └──────────────────────────┘  └──────────────────────────┘  │    │
│  └──────────────────────────────────────────────────────────────┘    │
│                                                                      │
│  ┌────────────────────────────────────────────────────────────────┐  │
│  │              «component» Configuración                          │  │
│  │   config.py  |  run.py  |  requirements.txt  |  .env           │  │
│  └────────────────────────────────────────────────────────────────┘  │
└─────────────────────────────────────────────────────────────────────┘
```

### Interfaces a modelar (puertos):

| Componente proveedor   | Interfaz              | Componente consumidor       |
|------------------------|-----------------------|-----------------------------|
| users.py               | «interface» IUsuarios | main.py (Dashboard)         |
| cells.py               | «interface» ICeldas   | main.py (Dashboard)         |
| cells.py               | «interface» ICeldas   | vehicles.py                 |
| vehicles.py            | «interface» IVehiculos| movements.py                |
| vehicles.py            | «interface» IVehiculos| incidents.py                |
| vehicles.py            | «interface» IVehiculos| payments.py                 |
| users.py               | «interface» IUsuarios | payments.py                 |

### Instrucciones detalladas StarUML:

1. **Crear Componentes:**
   - Herramienta `Component` para cada módulo listado
   - Agrupar por capas usando `Package` con estereotipo `«layer»`

2. **Crear Interfaces:**
   - Herramienta `Interface` → colocar entre componentes relacionados
   - Conectar con `Provided Interface` (círculo) y `Required Interface` (semicírculo)

3. **Conectar componentes:**
   - `Dependency` (flecha punteada) entre capas
   - `Realization` para indicar que un componente implementa una interfaz

4. **Añadir notas:**
   - `Note` para indicar tecnología: Flask, SQLAlchemy, Jinja2

---

---

# PARTE 4: MOCKUPS — ITERACIÓN 2

## Guía de diseño en Figma

---

## M-06 — Pantalla: Lista de Usuarios

### Especificaciones de diseño:

**Layout:**
- Sidebar izquierdo (mismo de todas las pantallas) con íconos de cada módulo
- Topbar con título "Gestión de Usuarios" y botón "+ Nuevo Usuario" (color azul primario)
- Área de contenido principal

**Componentes:**

```
┌─────────────────────────────────────────────────────────────────────────┐
│ TOPBAR: [≡ Autos Colombia]                      [Operador logueado]     │
├──────┬──────────────────────────────────────────────────────────────────┤
│      │  Gestión de Usuarios                    [+ Nuevo Usuario]        │
│  S   │  ─────────────────────────────────────────────────────────────  │
│  I   │  🔍 [Buscar por nombre, documento o correo...         ]          │
│  D   │                                                                  │
│  E   │  ┌─────────────────────────────────────────────────────────┐    │
│  B   │  │ Nombre          │ Documento  │ Correo       │ Tel  │ ⚙  │    │
│  A   │  ├─────────────────────────────────────────────────────────┤    │
│  R   │  │ Carlos Pérez    │ 10234567   │ carlos@...   │ 311  │ ⚙  │    │
│      │  │ María López     │ 45678901   │ maria@...    │ 300  │ ⚙  │    │
│      │  │ Juan García     │ 11223344   │ juan@...     │ 312  │ ⚙  │    │
│      │  └─────────────────────────────────────────────────────────┘    │
│      │                                                                  │
│      │  [← 1 2 3 →]  Mostrando 1-20 de 45 usuarios                    │
└──────┴──────────────────────────────────────────────────────────────────┘
```

**Especificaciones de color y tipografía:**
- Fondo general: `#f8f9fa` (Bootstrap light)
- Topbar: `#212529` (Bootstrap dark) con texto blanco
- Sidebar: `#343a40` con íconos blancos
- Botón principal: `#0d6efd` (Bootstrap primary)
- Filas de tabla: alternadas `#ffffff` / `#f8f9fa`
- Hover en fila: `#e9ecef`

---

## M-07 — Pantalla: Crear / Editar Usuario

### Especificaciones de diseño:

```
┌─────────────────────────────────────────────────────────────────────────┐
│ TOPBAR                                                                   │
├──────┬──────────────────────────────────────────────────────────────────┤
│      │  Nuevo Usuario                                                   │
│  S   │  ─────────────────────────────────────────────────────────────  │
│  I   │  ┌───────────────────────────────────────────────────────────┐  │
│  D   │  │                   Información Personal                     │  │
│  E   │  ├───────────────────────────────────────────────────────────┤  │
│  B   │  │  Nombre Completo *                                         │  │
│  A   │  │  [_______________________________________]                 │  │
│  R   │  │                                                            │  │
│      │  │  Número de Documento *                                     │  │
│      │  │  [_______________________________________]                 │  │
│      │  │                                                            │  │
│      │  │  Correo Electrónico *    │    Teléfono *                  │  │
│      │  │  [______________________] │  [_____________________]      │  │
│      │  │                                                            │  │
│      │  │  Dirección                                                 │  │
│      │  │  [_______________________________________]                 │  │
│      │  │                                                            │  │
│      │  │         [Cancelar]              [Guardar Usuario]          │  │
│      │  └───────────────────────────────────────────────────────────┘  │
└──────┴──────────────────────────────────────────────────────────────────┘
```

**Notas de UX:**
- Los campos obligatorios van marcados con asterisco rojo `*`
- Los errores se muestran en texto rojo debajo del campo (`text-danger`)
- El botón "Guardar Usuario" es azul primario; "Cancelar" es outline gris
- En modo edición, el campo "Número de Documento" aparece deshabilitado (gris, `readonly`)

---

## M-08 — Pantalla: Perfil de Usuario

### Especificaciones de diseño:

```
┌─────────────────────────────────────────────────────────────────────────┐
│ TOPBAR                                                                   │
├──────┬──────────────────────────────────────────────────────────────────┤
│      │  ← Volver   Perfil de Carlos Pérez          [Editar] [Desactivar]│
│  S   │  ─────────────────────────────────────────────────────────────  │
│  I   │  ┌────────────────────────┐  ┌────────────────────────────────┐ │
│  D   │  │  📋 Datos Personales   │  │    🚗 Vehículos (2)            │ │
│  E   │  ├────────────────────────┤  ├────────────────────────────────┤ │
│  B   │  │ Documento: 10234567    │  │  ABC-123 | Toyota Corolla      │ │
│  A   │  │ Correo: carlos@...     │  │  Celda: 1001 | Piso 1          │ │
│  R   │  │ Tel: 311-234-5678      │  │                                │ │
│      │  │ Dir: Calle 10 #20-30   │  │  DEF-456 | Honda CB500        │ │
│      │  │ Estado: ✅ Activo      │  │  Celda: 2001 | Piso 2          │ │
│      │  │ Registro: 15/01/2025   │  └────────────────────────────────┘ │
│      │  └────────────────────────┘                                     │
│      │  ┌─────────────────────────────────────────────────────────────┐│
│      │  │  💰 Últimos Pagos                                           ││
│      │  ├──────────────┬────────────┬──────────┬──────────────────────┤│
│      │  │ Período      │  Monto     │ Método   │ Estado               ││
│      │  │ Marzo 2026   │ $150,000   │ Efectivo │ ✅ Pagado            ││
│      │  │ Febrero 2026 │ $150,000   │ Transfer │ ✅ Pagado            ││
│      │  └─────────────────────────────────────────────────────────────┘│
└──────┴──────────────────────────────────────────────────────────────────┘
```

---

## M-09 — Pantalla: Panel de Celdas

### Especificaciones de diseño:

```
┌─────────────────────────────────────────────────────────────────────────┐
│ TOPBAR                                                                   │
├──────┬──────────────────────────────────────────────────────────────────┤
│      │  Gestión de Celdas                         [+ Nueva Celda]       │
│  S   │  ─────────────────────────────────────────────────────────────  │
│  I   │  ┌──────────────┐  ┌──────────────┐  ┌──────────────────────┐  │
│  D   │  │  📦 Total    │  │ ✅ Disponib. │  │    🔴 Ocupadas       │  │
│  E   │  │     45       │  │     28       │  │          17          │  │
│  B   │  └──────────────┘  └──────────────┘  └──────────────────────┘  │
│  A   │                                                                  │
│  R   │  Tipo: [Todos ▼]  Estado: [Todos ▼]  Piso: [Todos ▼]           │
│      │                                                                  │
│      │  ┌──────┐ ┌──────┐ ┌──────┐ ┌──────┐ ┌──────┐ ┌──────┐       │
│      │  │1001  │ │1002  │ │1003  │ │1004  │ │1005  │ │1006  │       │
│      │  │ 🚗   │ │ 🚗   │ │ 🚗   │ │ 🏍   │ │ 🏍   │ │ 🏍   │       │
│      │  │P.1   │ │P.1   │ │P.1   │ │P.1   │ │P.1   │ │P.1   │       │
│      │  │$150k │ │$150k │ │$150k │ │$80k  │ │$80k  │ │$80k  │       │
│      │  │DISP  │ │OCUP  │ │DISP  │ │DISP  │ │OCUP  │ │DISP  │       │
│      │  └──────┘ └──────┘ └──────┘ └──────┘ └──────┘ └──────┘       │
│      │  (verde)  (amaril) (verde)  (verde)  (amaril) (verde)           │
└──────┴──────────────────────────────────────────────────────────────────┘
```

**Especificaciones de color del grid de celdas:**
- Celda disponible: fondo `#d1e7dd` (Bootstrap success light), borde `#198754`
- Celda ocupada: fondo `#fff3cd` (Bootstrap warning light), borde `#ffc107`
- Tarjeta: `border-radius: 8px`, `padding: 12px`, `min-width: 80px`
- Hover: sombra `box-shadow: 0 2px 8px rgba(0,0,0,0.15)`

---

## M-10 — Pantalla: Crear / Editar Celda

### Especificaciones de diseño:

```
┌─────────────────────────────────────────────────────────────────────────┐
│ TOPBAR                                                                   │
├──────┬──────────────────────────────────────────────────────────────────┤
│      │  Nueva Celda                                                     │
│  S   │  ─────────────────────────────────────────────────────────────  │
│  I   │  ┌───────────────────────────────────────────────────────────┐  │
│  D   │  │                  Datos de la Celda                         │  │
│  E   │  ├───────────────────────────────────────────────────────────┤  │
│  B   │  │  Número de Celda *              │  Tipo de Vehículo *     │  │
│  A   │  │  [__________________]           │  [Carro       ▼]        │  │
│  R   │  │                                 │                         │  │
│      │  │  Piso *                         │  Tarifa Mensual (COP) * │  │
│      │  │  [__________________]           │  [__________________]   │  │
│      │  │                                 │                         │  │
│      │  │  ℹ️ El estado inicial será "Disponible" automáticamente.   │  │
│      │  │                                                            │  │
│      │  │         [Cancelar]              [Guardar Celda]            │  │
│      │  └───────────────────────────────────────────────────────────┘  │
└──────┴──────────────────────────────────────────────────────────────────┘
```

**Notas de UX:**
- En modo edición, el campo "Número de Celda" aparece deshabilitado
- El campo "Tarifa Mensual" debe tener el prefijo visual `$` y separadores de miles
- El campo tipo tiene tres opciones: Carro, Moto, Camión (con íconos)
