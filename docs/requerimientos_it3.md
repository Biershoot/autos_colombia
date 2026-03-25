# Requerimientos del Sistema — Parqueadero Autos Colombia
## Iteración 3: Gestión de Pagos

---

## 1. Requerimientos Funcionales

### RF-19 — Registrar Pago Mensual
**Descripción:** El sistema debe permitir registrar el pago de la mensualidad de un cliente por un vehículo específico.  
**Actor:** Administrador  
**Precondición:** Existen usuarios y vehículos activos registrados en el sistema.  
**Flujo principal:**
1. El administrador accede al módulo de Pagos.
2. Selecciona la opción "Nuevo Pago".
3. Selecciona el usuario (cliente).
4. El sistema carga automáticamente los vehículos registrados a nombre del usuario.
5. El administrador selecciona el vehículo.
6. El sistema pre-carga automáticamente el monto según la tarifa de la celda asignada al vehículo.
7. El administrador selecciona el período (mes y año) y el método de pago.
8. El sistema valida que no exista ya un pago registrado para ese vehículo en ese período.
9. El sistema guarda el pago con estado "pagado" y la fecha actual.
10. El sistema muestra mensaje de confirmación.

**Postcondición:** El pago queda registrado y el recaudo del mes se actualiza en el dashboard.  
**Flujo alternativo:** Si ya existe un pago para ese vehículo en el mismo período, el sistema muestra: *"Ya existe un pago registrado para este vehículo en el período seleccionado."*  
**Restricciones:**
- El monto debe ser mayor a cero.
- El período debe ser un mes/año válido.
- El método de pago debe ser uno de: efectivo, transferencia, tarjeta.

---

### RF-20 — Consultar Historial de Pagos
**Descripción:** El sistema debe permitir consultar el listado completo de pagos registrados con opciones de filtrado y paginación.  
**Actor:** Administrador  
**Precondición:** Existen pagos registrados en el sistema.  
**Flujo principal:**
1. El administrador accede al módulo de Pagos.
2. El sistema muestra la lista paginada de todos los pagos, ordenada por fecha descendente.
3. El administrador puede filtrar por: estado (pagado/pendiente/vencido), mes y año.
4. El sistema actualiza la lista con los resultados filtrados.
5. Cada registro muestra: usuario, vehículo (placa), período, monto, método de pago, fecha y estado.

**Postcondición:** El administrador puede visualizar el historial de pagos del parqueadero.  
**Regla de negocio:** Los pagos no pueden eliminarse físicamente del sistema.

---

### RF-21 — Auto-calcular Tarifa por Vehículo
**Descripción:** El sistema debe pre-cargar automáticamente el monto del pago según la tarifa de la celda asignada al vehículo seleccionado.  
**Actor:** Administrador / Sistema  
**Precondición:** El vehículo tiene una celda asignada con tarifa mensual configurada.  
**Flujo principal:**
1. El administrador selecciona un usuario en el formulario de nuevo pago.
2. El sistema carga vía AJAX los vehículos activos del usuario con sus tarifas.
3. El administrador selecciona el vehículo.
4. El sistema auto-completa el campo "Monto" con la tarifa mensual de la celda asignada.
5. El administrador puede modificar el monto si es necesario (descuentos, ajustes).

**Postcondición:** El campo monto queda pre-cargado para agilizar el registro.  
**Regla de negocio:** El monto sugerido corresponde al valor de `Cell.monthly_fee` del vehículo seleccionado.

---

### RF-22 — Filtrar Pagos por Estado y Período
**Descripción:** El sistema debe permitir filtrar el historial de pagos por múltiples criterios simultáneos.  
**Actor:** Administrador  
**Filtros disponibles:**
- Estado: pagado / pendiente / vencido
- Mes: enero a diciembre (1–12)
- Año: año de 4 dígitos

**Funcionalidades:**
- Los filtros son combinables (por ejemplo: pagos pendientes de marzo 2026).
- Al limpiar los filtros, se muestra el historial completo.
- La paginación respeta los filtros activos.

---

### RF-23 — Prevenir Pago Duplicado
**Descripción:** El sistema debe rechazar el registro de un pago si ya existe otro pago para el mismo vehículo en el mismo período (mes/año).  
**Actor:** Sistema (validación automática)  
**Precondición:** Existe un pago registrado para el vehículo X en el período M/A.  
**Flujo:**
1. El administrador intenta registrar un pago para el vehículo X en el mismo período M/A.
2. El sistema detecta el duplicado antes de persistir.
3. El sistema muestra el mensaje de error correspondiente.
4. El pago NO es creado.

**Regla de negocio:** La unicidad se aplica sobre la combinación `(vehicle_id, period_month, period_year)`.

---

### RF-24 — Ver Recaudo Mensual en Dashboard
**Descripción:** El sistema debe mostrar en el dashboard el recaudo total de pagos del mes en curso.  
**Actor:** Administrador  
**Indicadores mostrados en el dashboard:**
- Suma total de pagos con estado "pagado" del mes actual.
- Cantidad de pagos registrados en el mes actual.
- Acceso directo al módulo de Pagos desde el dashboard.

---

### RF-25 — Gestionar Estado de Pagos
**Descripción:** El sistema debe manejar tres estados posibles para los pagos y reflejarlos visualmente en el historial.  
**Estados:**
- **Pagado:** El cliente ha cancelado la mensualidad.
- **Pendiente:** El pago está por vencer o no ha sido registrado.
- **Vencido:** El período de pago ha pasado sin que se registre el pago.

**Indicadores visuales:**
- Estado pagado: badge verde.
- Estado pendiente: badge amarillo.
- Estado vencido: badge rojo.

---

## 2. Requerimientos No Funcionales — Iteración 3

### RNF-16 — Rendimiento en Operaciones de Pago
- El registro de un pago debe completarse en menos de **1 segundo**.
- El listado de pagos debe cargar en menos de **2 segundos** con hasta 10,000 registros.
- La carga AJAX de vehículos por usuario debe responder en menos de **500 ms**.

### RNF-17 — Integridad de Datos de Pagos
- No puede existir más de un pago en estado "pagado" para el mismo vehículo en el mismo período.
- Los pagos no pueden eliminarse físicamente del sistema (solo cambio de estado).
- El monto de un pago registrado no puede ser cero ni negativo.
- Toda operación de inserción de pago debe ejecutarse dentro de una transacción de base de datos.

### RNF-18 — Usabilidad del Formulario de Pago
- El formulario de registro de pago debe completarse en menos de **1 minuto** por un operador capacitado.
- La carga automática de vehículos al seleccionar un usuario debe ocurrir sin recargar la página (AJAX).
- El auto-completado del monto debe ejecutarse de forma inmediata al seleccionar el vehículo.

### RNF-19 — Consistencia Visual de Estados de Pago
- Los badges de estado deben ser consistentes con los colores Bootstrap 5:
  - Pagado: `#198754` (success verde).
  - Pendiente: `#ffc107` (warning amarillo).
  - Vencido: `#dc3545` (danger rojo).
- El historial de pagos debe ser ordenado por fecha descendente por defecto.

### RNF-20 — Trazabilidad de Pagos
- Cada pago debe registrar: fecha exacta del pago, usuario que lo registró, vehículo, período y método.
- El dashboard debe reflejar el recaudo del mes actual en tiempo real.
- Los pagos son auditables: no se permite modificar ni eliminar un pago ya registrado.

### RNF-21 — Escalabilidad del Módulo de Pagos
- La base de datos debe soportar hasta **10,000 registros de pagos mensuales** sin degradación perceptible.
- Los índices definidos en `database/schema.sql` sobre `payments.user_id`, `payments.period_month` y `payments.period_year` deben garantizar consultas eficientes.
