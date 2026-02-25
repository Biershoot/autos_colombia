-- ============================================================
-- PARQUEADERO AUTOS COLOMBIA
-- Modelo Físico - Base de Datos
-- ============================================================

-- ---------------------------------------------------------------
-- TABLA: users (Usuarios / Clientes mensuales)
-- ---------------------------------------------------------------
CREATE TABLE IF NOT EXISTS users (
    id          INTEGER     PRIMARY KEY AUTOINCREMENT,
    document    VARCHAR(20) NOT NULL UNIQUE,       -- Cédula o NIT
    full_name   VARCHAR(120) NOT NULL,
    email       VARCHAR(120) NOT NULL UNIQUE,
    phone       VARCHAR(20)  NOT NULL,
    address     VARCHAR(200),
    is_active   BOOLEAN     NOT NULL DEFAULT 1,
    created_at  DATETIME    NOT NULL DEFAULT CURRENT_TIMESTAMP
);

-- ---------------------------------------------------------------
-- TABLA: cells (Celdas del parqueadero)
-- ---------------------------------------------------------------
CREATE TABLE IF NOT EXISTS cells (
    id          INTEGER     PRIMARY KEY AUTOINCREMENT,
    number      VARCHAR(10) NOT NULL UNIQUE,       -- Ej: "1001", "2A05"
    cell_type   VARCHAR(20) NOT NULL               -- car | motorcycle | truck
                    CHECK (cell_type IN ('car', 'motorcycle', 'truck')),
    status      VARCHAR(20) NOT NULL DEFAULT 'available'
                    CHECK (status IN ('available', 'occupied')),
    floor       INTEGER     NOT NULL DEFAULT 1,
    monthly_fee REAL        NOT NULL               -- Tarifa mensual en COP
);

-- ---------------------------------------------------------------
-- TABLA: vehicles (Vehículos registrados)
-- ---------------------------------------------------------------
CREATE TABLE IF NOT EXISTS vehicles (
    id              INTEGER     PRIMARY KEY AUTOINCREMENT,
    plate           VARCHAR(10) NOT NULL UNIQUE,
    brand           VARCHAR(60) NOT NULL,
    model           VARCHAR(60) NOT NULL,
    year            INTEGER,
    color           VARCHAR(40),
    vehicle_type    VARCHAR(20) NOT NULL
                        CHECK (vehicle_type IN ('car', 'motorcycle', 'truck')),
    is_active       BOOLEAN     NOT NULL DEFAULT 1,
    registered_at   DATETIME    NOT NULL DEFAULT CURRENT_TIMESTAMP,

    -- Relaciones
    user_id         INTEGER     NOT NULL,
    cell_id         INTEGER,

    FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE RESTRICT,
    FOREIGN KEY (cell_id) REFERENCES cells(id) ON DELETE SET NULL
);

-- ---------------------------------------------------------------
-- TABLA: movements (Registro de entradas y salidas)
-- ---------------------------------------------------------------
CREATE TABLE IF NOT EXISTS movements (
    id              INTEGER     PRIMARY KEY AUTOINCREMENT,
    movement_type   VARCHAR(10) NOT NULL
                        CHECK (movement_type IN ('entry', 'exit')),
    timestamp       DATETIME    NOT NULL DEFAULT CURRENT_TIMESTAMP,
    notes           VARCHAR(255),

    -- Relaciones
    vehicle_id      INTEGER     NOT NULL,

    FOREIGN KEY (vehicle_id) REFERENCES vehicles(id) ON DELETE CASCADE
);

-- ---------------------------------------------------------------
-- TABLA: payments (Pagos mensuales)
-- ---------------------------------------------------------------
CREATE TABLE IF NOT EXISTS payments (
    id              INTEGER     PRIMARY KEY AUTOINCREMENT,
    amount          REAL        NOT NULL,
    payment_date    DATETIME    NOT NULL DEFAULT CURRENT_TIMESTAMP,
    period_month    INTEGER     NOT NULL CHECK (period_month BETWEEN 1 AND 12),
    period_year     INTEGER     NOT NULL,
    status          VARCHAR(20) NOT NULL DEFAULT 'paid'
                        CHECK (status IN ('paid', 'pending', 'overdue')),
    payment_method  VARCHAR(30),                   -- cash | transfer | card | nequi | daviplata

    -- Relaciones
    user_id         INTEGER     NOT NULL,
    vehicle_id      INTEGER,

    FOREIGN KEY (user_id)    REFERENCES users(id)    ON DELETE RESTRICT,
    FOREIGN KEY (vehicle_id) REFERENCES vehicles(id) ON DELETE SET NULL,

    -- Un vehículo no puede tener dos pagos en el mismo período
    UNIQUE (vehicle_id, period_month, period_year, status)
);

-- ---------------------------------------------------------------
-- TABLA: incidents (Novedades sobre vehículos)
-- ---------------------------------------------------------------
CREATE TABLE IF NOT EXISTS incidents (
    id          INTEGER     PRIMARY KEY AUTOINCREMENT,
    title       VARCHAR(100) NOT NULL,
    description TEXT         NOT NULL,
    severity    VARCHAR(20)  NOT NULL DEFAULT 'low'
                    CHECK (severity IN ('low', 'medium', 'high')),
    status      VARCHAR(20)  NOT NULL DEFAULT 'open'
                    CHECK (status IN ('open', 'resolved', 'closed')),
    created_at  DATETIME     NOT NULL DEFAULT CURRENT_TIMESTAMP,
    resolved_at DATETIME,

    -- Relaciones
    vehicle_id  INTEGER     NOT NULL,

    FOREIGN KEY (vehicle_id) REFERENCES vehicles(id) ON DELETE CASCADE
);

-- ---------------------------------------------------------------
-- ÍNDICES para optimización de consultas frecuentes
-- ---------------------------------------------------------------
CREATE INDEX IF NOT EXISTS idx_movements_vehicle   ON movements (vehicle_id);
CREATE INDEX IF NOT EXISTS idx_movements_timestamp ON movements (timestamp DESC);
CREATE INDEX IF NOT EXISTS idx_movements_type      ON movements (movement_type);
CREATE INDEX IF NOT EXISTS idx_vehicles_plate      ON vehicles  (plate);
CREATE INDEX IF NOT EXISTS idx_vehicles_user       ON vehicles  (user_id);
CREATE INDEX IF NOT EXISTS idx_payments_user       ON payments  (user_id);
CREATE INDEX IF NOT EXISTS idx_payments_period     ON payments  (period_year, period_month);
CREATE INDEX IF NOT EXISTS idx_incidents_vehicle   ON incidents (vehicle_id);
CREATE INDEX IF NOT EXISTS idx_incidents_status    ON incidents (status);
