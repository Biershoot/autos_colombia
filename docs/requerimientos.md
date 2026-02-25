# Requerimientos del Sistema — Parqueadero Autos Colombia
## Iteración 1: Gestión de Entrada y Salida de Vehículos

---

## 1. Requerimientos Funcionales

### RF-01 — Gestión de Entrada de Vehículos
**Descripción:** El sistema debe permitir registrar la entrada de un vehículo al parqueadero.  
**Actor:** Operador del parqueadero  
**Precondición:** El vehículo debe estar registrado en el sistema y tener asignada una celda.  
**Flujo principal:**
1. El operador accede al módulo de Entradas/Salidas.
2. Ingresa o selecciona la placa del vehículo.
3. Selecciona "Entrada" como tipo de movimiento.
4. Agrega observaciones opcionales.
5. El sistema valida que no exista una entrada previa sin salida.
6. El sistema registra la entrada con fecha y hora actual.
7. El sistema actualiza el estado de la celda a "ocupada".

**Postcondición:** El movimiento queda registrado con timestamp y la celda pasa a estado ocupado.  
**Flujo alternativo:** Si el vehículo ya tiene una entrada sin salida registrada, el sistema muestra una advertencia.

---

### RF-02 — Gestión de Salida de Vehículos
**Descripción:** El sistema debe permitir registrar la salida de un vehículo del parqueadero.  
**Actor:** Operador del parqueadero  
**Precondición:** El vehículo debe tener una entrada registrada previamente.  
**Flujo principal:**
1. El operador accede al módulo de Entradas/Salidas.
2. Ingresa o selecciona la placa del vehículo.
3. Selecciona "Salida" como tipo de movimiento.
4. El sistema valida que el vehículo tenga una entrada sin salida correspondiente.
5. El sistema registra la salida con fecha y hora actual.
6. El sistema actualiza el estado de la celda a "disponible".

**Postcondición:** El movimiento queda registrado y la celda queda disponible.  
**Flujo alternativo:** Si el vehículo no tiene entrada registrada, el sistema muestra una advertencia.

---

### RF-03 — Consultar Historial de Movimientos
**Descripción:** El sistema debe permitir consultar el historial completo de entradas y salidas.  
**Actor:** Administrador / Operador  
**Funcionalidades:**
- Filtrar por tipo de movimiento (entrada/salida).
- Filtrar por placa del vehículo.
- Paginación de resultados.
- Visualización de fecha, hora y observaciones.

---

### RF-04 — Registro de Usuarios (Clientes)
**Descripción:** El sistema debe permitir registrar los usuarios que tienen contrato de mensualidad.  
**Actor:** Administrador  
**Datos requeridos:** Nombre completo, número de documento, teléfono, correo electrónico, dirección.  
**Validaciones:** Documento y correo únicos en el sistema.

---

### RF-05 — Registro de Vehículos
**Descripción:** El sistema debe permitir registrar los vehículos de los clientes.  
**Actor:** Administrador  
**Datos requeridos:** Placa, marca, modelo, año, color, tipo de vehículo, propietario, celda asignada.  
**Validaciones:** La placa debe ser única. La celda asignada debe estar disponible.

---

### RF-06 — Gestión de Celdas
**Descripción:** El sistema debe gestionar las celdas del parqueadero.  
**Actor:** Administrador  
**Funcionalidades:**
- Crear nuevas celdas con número, tipo, piso y tarifa mensual.
- Visualizar el estado de todas las celdas (disponible/ocupada).
- Filtrar celdas por tipo, estado y piso.
- Editar información de una celda.

---

### RF-07 — Gestión de Pagos Mensuales
**Descripción:** El sistema debe registrar los pagos de mensualidad de los clientes.  
**Actor:** Administrador  
**Funcionalidades:**
- Registrar pago asociado a un usuario y vehículo.
- Registrar período (mes/año), monto y método de pago.
- Prevenir duplicación de pagos para el mismo vehículo en el mismo período.
- Consultar historial de pagos con filtros.
- Al seleccionar un vehículo, pre-poblar automáticamente el monto según la tarifa de la celda asignada.

---

### RF-08 — Registro de Novedades
**Descripción:** El sistema debe permitir registrar novedades o incidentes relacionados con un vehículo.  
**Actor:** Operador / Administrador  
**Datos requeridos:** Título, descripción, severidad (baja/media/alta), vehículo asociado.  
**Funcionalidades:**
- Registrar una nueva novedad.
- Marcar novedades como resueltas.
- Consultar el historial de novedades con filtros por estado y severidad.

---

### RF-09 — Dashboard de Estadísticas
**Descripción:** El sistema debe presentar un panel principal con métricas clave.  
**Actor:** Administrador  
**Indicadores:**
- Total de vehículos activos.
- Total de usuarios registrados.
- Celdas disponibles vs. ocupadas.
- Entradas y salidas del día actual.
- Recaudo mensual.
- Novedades abiertas.
- Últimos 10 movimientos.

---

## 2. Requerimientos No Funcionales

### RNF-01 — Rendimiento
- El sistema debe responder a cualquier consulta en menos de **2 segundos** bajo carga normal (hasta 50 usuarios concurrentes).
- Las operaciones de registro de entrada/salida no deben tardar más de **1 segundo**.

### RNF-02 — Disponibilidad
- El sistema debe estar disponible las **24 horas del día, 7 días a la semana** con un tiempo máximo de inactividad planeada de 4 horas al mes.

### RNF-03 — Usabilidad
- La interfaz debe ser intuitiva y permitir que un operador sin formación técnica pueda registrar una entrada/salida en **menos de 30 segundos**.
- El sistema debe funcionar correctamente en navegadores modernos (Chrome, Firefox, Edge).
- El diseño debe ser responsivo para funcionar en tablets y computadores.

### RNF-04 — Seguridad
- Las contraseñas deben almacenarse con hash (bcrypt o equivalente).
- Las rutas administrativas deben requerir autenticación.
- Se deben registrar los intentos de acceso fallidos.
- El sistema debe proteger contra inyección SQL y XSS.

### RNF-05 — Mantenibilidad
- El código fuente debe seguir el patrón de arquitectura **MVC**.
- El código debe estar documentado con comentarios en funciones clave.
- El sistema debe estar versionado en un repositorio Git.

### RNF-06 — Escalabilidad
- La arquitectura debe permitir migrar de SQLite a PostgreSQL sin cambios en la lógica de negocio.
- El sistema debe soportar el registro de hasta **500 vehículos** y **10,000 movimientos mensuales**.

### RNF-07 — Integridad de Datos
- El sistema debe usar **transacciones de base de datos** para garantizar consistencia al registrar movimientos.
- No debe ser posible eliminar físicamente un movimiento registrado.
- Los pagos duplicados en el mismo período deben ser rechazados por el sistema.

### RNF-08 — Portabilidad
- El sistema debe poder ejecutarse en Windows, macOS y Linux con Python 3.10+.
- Las dependencias deben estar documentadas en `requirements.txt`.
