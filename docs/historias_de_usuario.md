# Historias de Usuario — Parqueadero Autos Colombia
## Iteración 1: Gestión de Entrada y Salida de Vehículos

---

## HU-01 — Registrar Entrada de Vehículo

**Como** operador del parqueadero,  
**quiero** registrar la entrada de un vehículo al parqueadero,  
**para** llevar un control preciso del ingreso y la ocupación de celdas.

### Criterios de Aceptación:
- ✅ El sistema permite ingresar o seleccionar la placa del vehículo.
- ✅ El sistema muestra advertencia si el vehículo ya tiene una entrada activa sin salida.
- ✅ Al registrar la entrada, el timestamp se guarda automáticamente con fecha y hora del servidor.
- ✅ La celda asignada al vehículo cambia a estado "ocupada" al registrar la entrada.
- ✅ El operador puede agregar observaciones opcionales.
- ✅ El sistema confirma el registro con un mensaje de éxito.

**Estimación:** 3 puntos de historia  
**Prioridad:** Alta

---

## HU-02 — Registrar Salida de Vehículo

**Como** operador del parqueadero,  
**quiero** registrar la salida de un vehículo del parqueadero,  
**para** liberar la celda y mantener el historial actualizado.

### Criterios de Aceptación:
- ✅ El sistema permite seleccionar la placa del vehículo que va a salir.
- ✅ El sistema valida que el vehículo tenga una entrada registrada sin salida correspondiente.
- ✅ Al registrar la salida, la celda asociada cambia a estado "disponible".
- ✅ El operador puede agregar observaciones opcionales.
- ✅ El sistema muestra advertencia si se intenta registrar una salida sin entrada previa.

**Estimación:** 3 puntos de historia  
**Prioridad:** Alta

---

## HU-03 — Consultar Historial de Movimientos

**Como** administrador del parqueadero,  
**quiero** consultar el historial completo de entradas y salidas,  
**para** auditar y controlar el flujo de vehículos.

### Criterios de Aceptación:
- ✅ El sistema muestra una lista paginada de todos los movimientos.
- ✅ Se puede filtrar por tipo de movimiento (entrada/salida).
- ✅ Se puede buscar por placa del vehículo.
- ✅ Cada registro muestra: placa, tipo, marca/modelo, fecha y hora, observaciones.
- ✅ Los resultados se ordenan por fecha descendente (más recientes primero).

**Estimación:** 2 puntos de historia  
**Prioridad:** Alta

---

## HU-04 — Registrar un Nuevo Usuario

**Como** administrador,  
**quiero** registrar un nuevo cliente mensual,  
**para** tener su información disponible para asignarle vehículos y gestionar pagos.

### Criterios de Aceptación:
- ✅ El sistema solicita: nombre completo, documento, teléfono, correo, dirección.
- ✅ El sistema valida que el documento y el correo sean únicos.
- ✅ Se puede ver el perfil del usuario con sus vehículos y pagos asociados.
- ✅ Se puede editar la información del usuario.
- ✅ Se puede desactivar un usuario (no eliminar físicamente).

**Estimación:** 2 puntos de historia  
**Prioridad:** Alta

---

## HU-05 — Registrar un Vehículo

**Como** administrador,  
**quiero** registrar el vehículo de un cliente,  
**para** poder gestionar su entrada, salida y pagos de mensualidad.

### Criterios de Aceptación:
- ✅ El sistema solicita: placa, tipo, marca, modelo, año, color, propietario, celda.
- ✅ La placa debe ser única en el sistema.
- ✅ El sistema solo muestra celdas disponibles al momento del registro.
- ✅ Al asignar una celda, su estado cambia a "ocupada".
- ✅ El vehículo aparece en el listado con opción de ver detalle.

**Estimación:** 3 puntos de historia  
**Prioridad:** Alta

---

## HU-06 — Visualizar Estado de Celdas

**Como** operador del parqueadero,  
**quiero** ver el estado de todas las celdas del parqueadero,  
**para** saber rápidamente cuáles están disponibles y cuáles están ocupadas.

### Criterios de Aceptación:
- ✅ El sistema muestra todas las celdas en formato visual de cuadrícula.
- ✅ Las celdas disponibles se muestran en verde y las ocupadas en amarillo.
- ✅ Se puede filtrar por tipo de vehículo, estado y piso.
- ✅ Cada celda muestra su número, tipo y tarifa mensual.
- ✅ Hay un resumen estadístico (total, disponibles, ocupadas) en la parte superior.

**Estimación:** 2 puntos de historia  
**Prioridad:** Media

---

## HU-07 — Registrar Pago Mensual

**Como** administrador,  
**quiero** registrar el pago mensual de un cliente,  
**para** mantener un control de los ingresos del parqueadero.

### Criterios de Aceptación:
- ✅ El sistema permite seleccionar usuario, vehículo, mes, año y método de pago.
- ✅ Al seleccionar un vehículo, el sistema pre-carga automáticamente el monto de la tarifa.
- ✅ El sistema rechaza pagos duplicados para el mismo vehículo y período.
- ✅ El historial de pagos es consultable con filtros por estado, mes y año.
- ✅ El dashboard muestra el recaudo total del mes en curso.

**Estimación:** 3 puntos de historia  
**Prioridad:** Alta

---

## HU-08 — Registrar Novedad sobre un Vehículo

**Como** operador del parqueadero,  
**quiero** registrar una novedad o incidente sobre un vehículo,  
**para** documentar daños, situaciones especiales o alertas relacionadas.

### Criterios de Aceptación:
- ✅ El sistema permite registrar título, descripción, severidad y vehículo asociado.
- ✅ Las novedades tienen tres niveles de severidad: baja, media y alta.
- ✅ Una novedad abierta puede ser marcada como resuelta.
- ✅ Las novedades abiertas se cuentan en el dashboard.
- ✅ Cada vehículo muestra su historial de novedades en su página de detalle.

**Estimación:** 2 puntos de historia  
**Prioridad:** Media

---

## HU-09 — Ver Dashboard de Resumen

**Como** administrador del parqueadero,  
**quiero** ver un panel con las métricas más importantes del día,  
**para** tomar decisiones rápidas sobre la operación.

### Criterios de Aceptación:
- ✅ El dashboard muestra total de vehículos activos, usuarios, celdas disponibles/ocupadas.
- ✅ Muestra el conteo de entradas y salidas del día actual.
- ✅ Muestra el recaudo total del mes en curso.
- ✅ Muestra el número de novedades abiertas.
- ✅ Muestra los últimos 10 movimientos registrados en tiempo real.
- ✅ Ofrece accesos directos a las acciones más frecuentes.

**Estimación:** 2 puntos de historia  
**Prioridad:** Media

---

## Resumen de Estimación

| Historia | Descripción                        | Puntos | Prioridad |
|----------|------------------------------------|--------|-----------|
| HU-01    | Registrar entrada de vehículo      | 3      | Alta      |
| HU-02    | Registrar salida de vehículo       | 3      | Alta      |
| HU-03    | Consultar historial de movimientos | 2      | Alta      |
| HU-04    | Registrar nuevo usuario            | 2      | Alta      |
| HU-05    | Registrar vehículo                 | 3      | Alta      |
| HU-06    | Visualizar estado de celdas        | 2      | Media     |
| HU-07    | Registrar pago mensual             | 3      | Alta      |
| HU-08    | Registrar novedad sobre vehículo   | 2      | Media     |
| HU-09    | Ver dashboard de resumen           | 2      | Media     |
| **Total**|                                    | **22** |           |
