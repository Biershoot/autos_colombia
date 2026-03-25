# Historias de Usuario — Parqueadero Autos Colombia
## Iteración 3: Gestión de Pagos

---

## MÓDULO: GESTIÓN DE PAGOS

---

## HU-18 — Registrar Pago Mensual

**Como** administrador del parqueadero,  
**quiero** registrar el pago de la mensualidad de un cliente,  
**para** mantener un control preciso de los ingresos del parqueadero y el estado de cartera de cada cliente.

### Criterios de Aceptación:
- [ ] El formulario permite seleccionar usuario, vehículo, mes, año y método de pago (efectivo/transferencia/tarjeta).
- [ ] El sistema muestra únicamente usuarios activos en el selector de usuario.
- [ ] Al seleccionar el usuario, el sistema carga automáticamente sus vehículos activos vía AJAX.
- [ ] Al seleccionar el vehículo, el campo "Monto" se pre-carga automáticamente con la tarifa de la celda.
- [ ] El sistema registra el pago con la fecha actual del servidor.
- [ ] El sistema confirma con el mensaje: *"Pago registrado exitosamente."*
- [ ] El pago recién registrado aparece en el historial con estado "pagado".

**Estimación:** 3 puntos de historia  
**Prioridad:** Alta

---

## HU-19 — Auto-calcular Tarifa por Vehículo

**Como** administrador del parqueadero,  
**quiero** que al seleccionar un vehículo el sistema pre-cargue automáticamente el monto del pago,  
**para** reducir errores de digitación y agilizar el proceso de registro de pagos.

### Criterios de Aceptación:
- [ ] Al seleccionar un usuario, el sistema realiza una petición AJAX y carga sus vehículos en el selector.
- [ ] Cada opción del selector de vehículo muestra la placa y la tarifa mensual correspondiente.
- [ ] Al seleccionar el vehículo, el campo "Monto" se actualiza automáticamente sin recargar la página.
- [ ] El monto pre-cargado corresponde exactamente al valor de `monthly_fee` de la celda asignada al vehículo.
- [ ] El administrador puede modificar manualmente el monto si necesita aplicar un ajuste.
- [ ] Si el usuario no tiene vehículos activos, el selector muestra: *"Este usuario no tiene vehículos registrados."*

**Estimación:** 2 puntos de historia  
**Prioridad:** Alta

---

## HU-20 — Consultar Historial de Pagos

**Como** administrador del parqueadero,  
**quiero** consultar el historial completo de pagos registrados,  
**para** auditar los ingresos del parqueadero y verificar el estado de pago de cada cliente.

### Criterios de Aceptación:
- [ ] El sistema muestra una lista paginada de todos los pagos, ordenada por fecha descendente.
- [ ] Cada registro muestra: nombre del usuario, placa del vehículo, período (mes/año), monto, método de pago, fecha y estado.
- [ ] El estado del pago se muestra con un badge de color: verde (pagado), amarillo (pendiente), rojo (vencido).
- [ ] La lista soporta hasta 10,000 registros sin degradación perceptible.
- [ ] Si no hay pagos registrados, el sistema muestra: *"No hay pagos registrados."*

**Estimación:** 2 puntos de historia  
**Prioridad:** Alta

---

## HU-21 — Filtrar Pagos por Estado y Período

**Como** administrador del parqueadero,  
**quiero** filtrar el historial de pagos por estado y período,  
**para** identificar rápidamente los pagos pendientes o vencidos de un mes específico y gestionar la cartera.

### Criterios de Aceptación:
- [ ] El sistema proporciona filtros por: estado (pagado/pendiente/vencido), mes (1–12) y año.
- [ ] Los filtros son combinables entre sí (por ejemplo: pendientes de marzo 2026).
- [ ] Al aplicar filtros, la lista se actualiza mostrando solo los resultados correspondientes.
- [ ] La paginación respeta los filtros activos.
- [ ] Al limpiar los filtros, se restaura el historial completo.
- [ ] El número de resultados filtrados se muestra al usuario.

**Estimación:** 2 puntos de historia  
**Prioridad:** Alta

---

## HU-22 — Prevenir Pago Duplicado

**Como** administrador del parqueadero,  
**quiero** que el sistema impida registrar dos pagos para el mismo vehículo en el mismo período,  
**para** garantizar la integridad del historial de pagos y evitar cobros dobles a los clientes.

### Criterios de Aceptación:
- [ ] Si ya existe un pago para el mismo vehículo en el mismo mes y año, el sistema rechaza el nuevo registro.
- [ ] El sistema muestra el mensaje de error: *"Ya existe un pago registrado para este vehículo en el período seleccionado."*
- [ ] El formulario permanece visible con los datos ingresados para que el administrador pueda corregir.
- [ ] El pago duplicado NO se guarda en la base de datos bajo ninguna circunstancia.

**Estimación:** 2 puntos de historia  
**Prioridad:** Alta

---

## HU-23 — Ver Recaudo Mensual en Dashboard

**Como** administrador del parqueadero,  
**quiero** ver el total de recaudo del mes en el dashboard principal,  
**para** tener una visión inmediata del desempeño financiero del parqueadero sin entrar al módulo de pagos.

### Criterios de Aceptación:
- [ ] El dashboard muestra el total en pesos colombianos (COP) de todos los pagos con estado "pagado" del mes actual.
- [ ] El indicador se actualiza automáticamente cada vez que se registra un nuevo pago.
- [ ] El dashboard muestra el número total de pagos registrados en el mes actual.
- [ ] Desde el dashboard hay un acceso directo al módulo de pagos.
- [ ] Si no hay pagos en el mes actual, el indicador muestra $0.

**Estimación:** 1 punto de historia  
**Prioridad:** Media

---

## Resumen de Estimación — Iteración 3

| Historia | Descripción                        | Módulo | Puntos | Prioridad |
|----------|------------------------------------|--------|--------|-----------|
| HU-18    | Registrar pago mensual             | Pagos  | 3      | Alta      |
| HU-19    | Auto-calcular tarifa por vehículo  | Pagos  | 2      | Alta      |
| HU-20    | Consultar historial de pagos       | Pagos  | 2      | Alta      |
| HU-21    | Filtrar pagos por estado y período | Pagos  | 2      | Alta      |
| HU-22    | Prevenir pago duplicado            | Pagos  | 2      | Alta      |
| HU-23    | Ver recaudo mensual en dashboard   | Pagos  | 1      | Media     |
| **Total**|                                    |        | **12** |           |

---

## Acumulado Total del Proyecto

| Iteración   | Historias        | Puntos  | Módulos cubiertos                        |
|-------------|------------------|---------|------------------------------------------|
| Iteración 1 | HU-01 a HU-09    | 22      | Entradas/Salidas, Dashboard, Novedades   |
| Iteración 2 | HU-10 a HU-17    | 18      | Usuarios, Celdas                         |
| Iteración 3 | HU-18 a HU-23    | 12      | Pagos                                    |
| **Total**   | **23 historias** | **52**  |                                          |
