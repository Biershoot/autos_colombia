-- ============================================================
-- DATOS DE PRUEBA - Parqueadero Autos Colombia
-- ============================================================

-- Usuarios
INSERT INTO users (document, full_name, email, phone, address) VALUES
('1020345678', 'Carlos Andrés Ramírez',    'carlos.ramirez@gmail.com',    '3001234567', 'Calle 45 # 12-30, Bogotá'),
('1032456789', 'María Fernanda López',     'mf.lopez@hotmail.com',        '3112345678', 'Carrera 7 # 89-15, Bogotá'),
('1045678901', 'Juan Pablo Martínez',      'juan.martinez@outlook.com',   '3223456789', 'Avenida 68 # 55-20, Bogotá'),
('1056789012', 'Luisa Valentina Torres',   'luisa.torres@gmail.com',      '3134567890', 'Calle 100 # 14-05, Bogotá'),
('1067890123', 'Andrés Felipe García',     'andres.garcia@yahoo.com',     '3245678901', 'Transversal 22 # 30-10, Bogotá');

-- Celdas de ejemplo
INSERT INTO cells (number, cell_type, floor, monthly_fee, status) VALUES
('P101', 'car',        1, 150000, 'available'),
('P102', 'car',        1, 150000, 'available'),
('P103', 'car',        1, 150000, 'available'),
('P201', 'motorcycle', 1,  80000, 'available'),
('P202', 'motorcycle', 1,  80000, 'available'),
('P301', 'truck',      1, 200000, 'available'),
('P401', 'car',        2, 150000, 'available'),
('P402', 'car',        2, 150000, 'available');

-- Vehículos
INSERT INTO vehicles (plate, brand, model, year, color, vehicle_type, user_id, cell_id) VALUES
('ABC123', 'Toyota',    'Corolla',   2019, 'Blanco',  'car',        1, 1),
('XYZ789', 'Chevrolet', 'Spark',     2021, 'Rojo',    'car',        2, 2),
('MNO456', 'Honda',     'CB190R',    2022, 'Negro',   'motorcycle', 3, 4),
('PQR321', 'Mazda',     'CX-30',     2020, 'Gris',    'car',        4, 3),
('STU654', 'Yamaha',    'FZ25',      2023, 'Azul',    'motorcycle', 5, 5);

-- Actualizar celdas como ocupadas
UPDATE cells SET status = 'occupied' WHERE id IN (1, 2, 3, 4, 5);

-- Movimientos (entradas y salidas)
INSERT INTO movements (vehicle_id, movement_type, notes, timestamp) VALUES
(1, 'entry', NULL,               datetime('now', '-2 hours')),
(2, 'entry', NULL,               datetime('now', '-1 hour')),
(3, 'entry', 'Cliente frecuente', datetime('now', '-3 hours')),
(1, 'exit',  NULL,               datetime('now', '-30 minutes')),
(4, 'entry', NULL,               datetime('now', '-45 minutes')),
(5, 'entry', NULL,               datetime('now', '-20 minutes'));

-- Pagos del mes actual
INSERT INTO payments (user_id, vehicle_id, amount, period_month, period_year, payment_method, status) VALUES
(1, 1, 150000, strftime('%m', 'now'), strftime('%Y', 'now'), 'cash',     'paid'),
(2, 2, 150000, strftime('%m', 'now'), strftime('%Y', 'now'), 'transfer', 'paid'),
(3, 3,  80000, strftime('%m', 'now'), strftime('%Y', 'now'), 'nequi',    'paid'),
(4, 4, 150000, strftime('%m', 'now'), strftime('%Y', 'now'), 'card',     'paid');

-- Novedades
INSERT INTO incidents (vehicle_id, title, description, severity, status) VALUES
(1, 'Rayón en puerta trasera derecha',
   'El propietario reportó un rayón de aproximadamente 15cm en la puerta trasera derecha al momento del ingreso.',
   'low', 'open'),
(3, 'Llanta trasera baja de presión',
   'Se detectó que la llanta trasera de la motocicleta tenía baja presión. Se notificó al propietario.',
   'medium', 'resolved');
