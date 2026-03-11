# Requerimientos del Sistema — Parqueadero Autos Colombia
## Iteración 2: Gestión de Usuarios y Gestión de Celdas

---

## 1. Requerimientos Funcionales

### RF-10 — Registrar Usuario
**Descripción:** El sistema debe permitir registrar un nuevo cliente que contrata el servicio de mensualidad.  
**Actor:** Administrador  
**Precondición:** El administrador ha iniciado sesión en el sistema.  
**Flujo principal:**
1. El administrador accede al módulo de Usuarios.
2. Selecciona la opción "Nuevo Usuario".
3. Ingresa los datos: nombre completo, número de documento, teléfono, correo electrónico y dirección.
4. El sistema valida que el documento y el correo no estén registrados previamente.
5. El sistema guarda el usuario con estado activo y fecha de creación automática.
6. El sistema muestra el perfil del usuario recién creado con mensaje de confirmación.

**Postcondición:** El usuario queda registrado en el sistema con estado activo.  
**Flujo alternativo A:** Si el documento ya existe, el sistema muestra el mensaje: *"El número de documento ya se encuentra registrado."*  
**Flujo alternativo B:** Si el correo ya existe, el sistema muestra el mensaje: *"El correo electrónico ya se encuentra registrado."*  
**Restricciones de validación:**
- Nombre completo: mínimo 3 caracteres, máximo 100.
- Documento: solo dígitos, mínimo 6, máximo 15.
- Correo: formato válido de correo electrónico.
- Teléfono: solo dígitos, máximo 15 caracteres.

---

### RF-11 — Consultar y Buscar Usuarios
**Descripción:** El sistema debe permitir consultar el listado de usuarios registrados con opciones de búsqueda y paginación.  
**Actor:** Administrador  
**Precondición:** Existen usuarios registrados en el sistema.  
**Flujo principal:**
1. El administrador accede al módulo de Usuarios.
2. El sistema muestra la lista paginada de todos los usuarios activos.
3. El administrador puede escribir en el campo de búsqueda para filtrar por nombre, número de documento o correo electrónico.
4. El sistema actualiza la lista en tiempo real con los resultados que coinciden con el criterio de búsqueda.
5. El administrador puede hacer clic en cualquier usuario para ver su perfil detallado.

**Postcondición:** El administrador puede ver y acceder a los usuarios del sistema.  
**Regla de negocio:** Los usuarios inactivos no aparecen en la lista principal pero son consultables desde el detalle de un vehículo o historial de pagos.

---

### RF-12 — Ver Perfil Detallado de Usuario
**Descripción:** El sistema debe mostrar el perfil completo de un usuario con sus vehículos y pagos asociados.  
**Actor:** Administrador  
**Precondición:** El usuario existe en el sistema.  
**Información mostrada:**
- Datos personales completos (nombre, documento, correo, teléfono, dirección).
- Estado (activo/inactivo) y fecha de registro.
- Lista de vehículos registrados a su nombre con placa, marca/modelo y celda asignada.
- Historial de pagos con período, monto, método y estado.

---

### RF-13 — Editar Información de Usuario
**Descripción:** El sistema debe permitir actualizar los datos de un usuario existente.  
**Actor:** Administrador  
**Precondición:** El usuario existe y está activo en el sistema.  
**Flujo principal:**
1. El administrador accede al perfil del usuario.
2. Selecciona la opción "Editar".
3. Modifica los campos permitidos: nombre completo, teléfono, correo electrónico y dirección.
4. El sistema valida que el correo no esté en uso por otro usuario diferente.
5. El sistema guarda los cambios y redirige al perfil actualizado con mensaje de confirmación.

**Postcondición:** Los datos del usuario quedan actualizados.  
**Restricción:** El número de documento no puede ser modificado una vez registrado.

---

### RF-14 — Desactivar Usuario
**Descripción:** El sistema debe permitir desactivar a un usuario sin eliminarlo físicamente de la base de datos.  
**Actor:** Administrador  
**Precondición:** El usuario existe y está activo. El usuario no debe tener vehículos activos con mensualidades pendientes.  
**Flujo principal:**
1. El administrador accede al perfil del usuario.
2. Selecciona la opción "Desactivar Usuario".
3. El sistema solicita confirmación de la acción.
4. El sistema cambia el estado del usuario a inactivo.
5. El sistema muestra mensaje de confirmación.

**Postcondición:** El usuario queda inactivo. Su historial se conserva íntegro.  
**Flujo alternativo:** Si el usuario tiene vehículos activos, el sistema muestra advertencia indicando que debe desactivar los vehículos primero.  
**Regla de negocio:** Los usuarios desactivados no pueden tener nuevos vehículos ni pagos registrados.

---

### RF-15 — Crear Celda
**Descripción:** El sistema debe permitir registrar una nueva celda de parqueadero.  
**Actor:** Administrador  
**Precondición:** El administrador ha iniciado sesión en el sistema.  
**Flujo principal:**
1. El administrador accede al módulo de Celdas.
2. Selecciona la opción "Nueva Celda".
3. Ingresa los datos: número de celda, tipo de vehículo (carro/moto/camión), piso y tarifa mensual.
4. El sistema valida que el número de celda no exista ya en el sistema.
5. El sistema guarda la celda con estado "disponible" por defecto.
6. El sistema confirma la creación y redirige al panel de celdas.

**Postcondición:** La celda queda registrada como disponible para ser asignada a un vehículo.  
**Flujo alternativo:** Si el número de celda ya existe, el sistema muestra el mensaje: *"El número de celda ya está registrado."*  
**Restricciones:**
- Número de celda: alfanumérico, máximo 10 caracteres, único.
- Tipo: debe ser uno de los valores válidos (carro, moto, camión).
- Piso: entero positivo, mínimo 1.
- Tarifa mensual: valor numérico positivo en COP.

---

### RF-16 — Editar Información de Celda
**Descripción:** El sistema debe permitir actualizar los datos de una celda existente.  
**Actor:** Administrador  
**Precondición:** La celda existe en el sistema.  
**Flujo principal:**
1. El administrador accede al módulo de Celdas.
2. Selecciona la celda que desea editar.
3. Modifica los campos: tipo de vehículo, piso o tarifa mensual.
4. El sistema guarda los cambios y confirma la actualización.

**Postcondición:** Los datos de la celda quedan actualizados.  
**Restricción:** El número de celda no puede ser modificado una vez creado.  
**Regla de negocio:** Si la celda está actualmente ocupada, se puede editar la tarifa pero el cambio aplicará a partir del siguiente período de facturación.

---

### RF-17 — Consultar y Filtrar Celdas
**Descripción:** El sistema debe permitir consultar todas las celdas con opciones de filtrado y vista visual.  
**Actor:** Administrador / Operador  
**Precondición:** Existen celdas registradas en el sistema.  
**Flujo principal:**
1. El usuario accede al módulo de Celdas.
2. El sistema muestra todas las celdas en vista de cuadrícula (grid).
3. Las celdas disponibles se visualizan en color verde y las ocupadas en color amarillo.
4. El usuario puede filtrar por: tipo de vehículo (carro/moto/camión), estado (disponible/ocupada) y piso.
5. El sistema actualiza la vista mostrando únicamente las celdas que coincidan con los filtros.
6. En la parte superior se muestran estadísticas: total, disponibles y ocupadas.

**Postcondición:** El usuario puede ver el estado de las celdas del parqueadero.

---

### RF-18 — Ver Estadísticas de Ocupación de Celdas
**Descripción:** El sistema debe presentar métricas de ocupación de celdas en tiempo real.  
**Actor:** Administrador  
**Indicadores:**
- Total de celdas registradas.
- Celdas disponibles (total y porcentaje).
- Celdas ocupadas (total y porcentaje).
- Desglose por tipo de vehículo (carro, moto, camión).
- Capacidad disponible por piso.

---

## 2. Requerimientos No Funcionales — Iteración 2

### RNF-09 — Rendimiento en Carga de Listados
- El listado de usuarios debe cargar en menos de **1.5 segundos** con hasta 500 usuarios registrados.
- El panel de celdas (grid visual) debe renderizar en menos de **1 segundo** con hasta 200 celdas.

### RNF-10 — Usabilidad en Formularios
- Los formularios de registro y edición de usuarios deben completarse en menos de **2 minutos** por un operador capacitado.
- Los mensajes de validación deben ser claros, específicos y aparecer junto al campo que presenta el error.
- Los campos obligatorios deben estar claramente marcados con un indicador visual.

### RNF-11 — Integridad de Datos de Usuarios
- No debe ser posible registrar dos usuarios con el mismo número de documento.
- No debe ser posible registrar dos usuarios con el mismo correo electrónico.
- La eliminación de un usuario debe ser lógica (cambio de estado), nunca física.
- El historial de pagos y vehículos de un usuario desactivado debe conservarse íntegro.

### RNF-12 — Integridad de Datos de Celdas
- No puede existir una celda con número duplicado.
- Una celda ocupada no puede ser asignada a otro vehículo sin antes liberarla.
- El estado de una celda debe actualizarse automáticamente al registrar/desregistrar un vehículo.

### RNF-13 — Consistencia Visual del Panel de Celdas
- Las celdas disponibles deben representarse consistentemente en color verde (#198754).
- Las celdas ocupadas deben representarse consistentemente en color amarillo (#ffc107).
- La vista de cuadrícula debe ser responsiva y funcionar en resoluciones desde 768px de ancho.

### RNF-14 — Trazabilidad de Cambios
- El sistema debe registrar la fecha de creación de cada usuario.
- Cualquier cambio en el estado de una celda (disponible → ocupada y viceversa) debe ser rastreable a través del registro de movimientos o vehículos.

### RNF-15 — Accesibilidad
- Los formularios deben tener etiquetas (`label`) correctamente asociadas a sus campos para compatibilidad con lectores de pantalla.
- El contraste de colores en el panel de celdas debe cumplir con el nivel AA de las WCAG 2.1.
