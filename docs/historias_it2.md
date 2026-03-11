# Historias de Usuario — Parqueadero Autos Colombia
## Iteración 2: Gestión de Usuarios y Gestión de Celdas

---

## MÓDULO: GESTIÓN DE USUARIOS

---

## HU-10 — Buscar y Consultar Usuarios

**Como** administrador del parqueadero,  
**quiero** buscar usuarios por nombre, documento o correo,  
**para** encontrar rápidamente el perfil de un cliente sin recorrer toda la lista.

### Criterios de Aceptación:
- [ ] El sistema muestra una lista paginada de todos los usuarios activos al ingresar al módulo.
- [ ] El campo de búsqueda filtra en tiempo real por nombre completo, número de documento o correo electrónico.
- [ ] Cada fila del listado muestra: nombre, documento, correo, teléfono y estado.
- [ ] Los resultados se ordenan por nombre de forma ascendente por defecto.
- [ ] Si no hay resultados para la búsqueda, el sistema muestra el mensaje: *"No se encontraron usuarios con ese criterio."*
- [ ] La lista soporta hasta 500 usuarios sin degradar el tiempo de carga más de 1.5 segundos.

**Estimación:** 2 puntos de historia  
**Prioridad:** Alta

---

## HU-11 — Ver Perfil Detallado de Usuario

**Como** administrador del parqueadero,  
**quiero** ver toda la información de un cliente en una sola pantalla,  
**para** conocer sus vehículos registrados, celdas asignadas e historial de pagos sin navegar por múltiples módulos.

### Criterios de Aceptación:
- [ ] El perfil muestra: nombre completo, documento, correo, teléfono, dirección, estado y fecha de registro.
- [ ] El perfil muestra la lista de vehículos del usuario con placa, marca/modelo, tipo y celda asignada.
- [ ] El perfil muestra los últimos 5 pagos del usuario con período, monto y método de pago.
- [ ] Desde el perfil hay botones de acción directa: "Editar" y "Desactivar".
- [ ] Si el usuario no tiene vehículos, se muestra el mensaje: *"Este usuario no tiene vehículos registrados."*
- [ ] Si el usuario no tiene pagos, se muestra el mensaje: *"No hay pagos registrados para este usuario."*

**Estimación:** 2 puntos de historia  
**Prioridad:** Alta

---

## HU-12 — Editar Información de Usuario

**Como** administrador del parqueadero,  
**quiero** actualizar los datos de contacto de un cliente,  
**para** mantener la información del sistema al día ante cambios de teléfono, correo o dirección.

### Criterios de Aceptación:
- [ ] El formulario de edición viene pre-cargado con los datos actuales del usuario.
- [ ] Los campos editables son: nombre completo, teléfono, correo electrónico y dirección.
- [ ] El número de documento aparece como campo de solo lectura (no es modificable).
- [ ] El sistema valida que el correo nuevo no esté en uso por un usuario diferente.
- [ ] Al guardar, el sistema muestra el mensaje: *"Usuario actualizado correctamente."*
- [ ] Al cancelar, el sistema regresa al perfil del usuario sin guardar cambios.
- [ ] Los errores de validación se muestran junto al campo correspondiente.

**Estimación:** 2 puntos de historia  
**Prioridad:** Alta

---

## HU-13 — Desactivar Usuario

**Como** administrador del parqueadero,  
**quiero** desactivar a un cliente que ya no usa el servicio de mensualidad,  
**para** retirar sus accesos sin perder el historial histórico de pagos y vehículos.

### Criterios de Aceptación:
- [ ] La opción "Desactivar" está disponible en el perfil del usuario activo.
- [ ] El sistema solicita una confirmación con el mensaje: *"¿Está seguro que desea desactivar a [nombre del usuario]? Esta acción cambiará su estado a inactivo."*
- [ ] Al confirmar, el usuario cambia a estado inactivo y desaparece del listado principal.
- [ ] Los vehículos, pagos y movimientos asociados al usuario se conservan en el sistema.
- [ ] El sistema muestra el mensaje: *"El usuario ha sido desactivado exitosamente."*
- [ ] Si el usuario tiene vehículos activos asignados a celdas, el sistema muestra advertencia antes de desactivar.
- [ ] Un usuario inactivo puede ser reactivado mediante la opción "Activar" en su perfil.

**Estimación:** 3 puntos de historia  
**Prioridad:** Alta

---

## MÓDULO: GESTIÓN DE CELDAS

---

## HU-14 — Crear Nueva Celda

**Como** administrador del parqueadero,  
**quiero** registrar una nueva celda en el sistema,  
**para** habilitar nuevos espacios disponibles cuando el parqueadero amplíe su capacidad.

### Criterios de Aceptación:
- [ ] El formulario solicita: número de celda, tipo de vehículo (carro/moto/camión), piso y tarifa mensual.
- [ ] El número de celda debe ser único en el sistema.
- [ ] El sistema rechaza el registro si el número de celda ya existe con el mensaje: *"El número de celda ya está registrado."*
- [ ] Al crear la celda, su estado inicial es "disponible" automáticamente.
- [ ] La tarifa mensual se ingresa en pesos colombianos (COP) y debe ser un valor positivo mayor a cero.
- [ ] La celda recién creada aparece inmediatamente en el panel de celdas.
- [ ] El sistema confirma la creación con el mensaje: *"Celda creada exitosamente."*

**Estimación:** 2 puntos de historia  
**Prioridad:** Alta

---

## HU-15 — Editar Celda

**Como** administrador del parqueadero,  
**quiero** actualizar los datos de una celda existente,  
**para** corregir errores de registro o ajustar las tarifas mensuales.

### Criterios de Aceptación:
- [ ] El formulario de edición viene pre-cargado con los datos actuales de la celda.
- [ ] Los campos editables son: tipo de vehículo, piso y tarifa mensual.
- [ ] El número de celda aparece como campo de solo lectura (no es modificable).
- [ ] La tarifa mensual modificada se aplicará a los nuevos pagos registrados.
- [ ] Al guardar, el sistema muestra el mensaje: *"Celda actualizada correctamente."*
- [ ] Al cancelar, el sistema regresa al panel de celdas sin guardar cambios.

**Estimación:** 2 puntos de historia  
**Prioridad:** Media

---

## HU-16 — Visualizar y Filtrar Celdas

**Como** operador del parqueadero,  
**quiero** ver el estado de todas las celdas en un panel visual con opciones de filtro,  
**para** identificar rápidamente qué celdas están disponibles y asignarlas a nuevos clientes.

### Criterios de Aceptación:
- [ ] El sistema muestra todas las celdas en formato de cuadrícula (grid card).
- [ ] Las celdas disponibles se muestran con fondo verde y las ocupadas con fondo amarillo.
- [ ] Cada tarjeta de celda muestra: número, ícono del tipo de vehículo, piso y tarifa mensual.
- [ ] El usuario puede filtrar simultáneamente por: tipo (carro/moto/camión), estado (disponible/ocupada) y piso.
- [ ] En la parte superior hay 3 tarjetas de estadísticas: Total celdas, Disponibles, Ocupadas.
- [ ] Si no hay celdas que coincidan con los filtros, se muestra: *"No hay celdas con los filtros seleccionados."*
- [ ] El panel funciona correctamente en resoluciones desde 768px (tablet).

**Estimación:** 2 puntos de historia  
**Prioridad:** Alta

---

## HU-17 — Asignar Celda Disponible a Vehículo

**Como** administrador del parqueadero,  
**quiero** que al registrar un vehículo solo se puedan seleccionar celdas disponibles del tipo correcto,  
**para** evitar asignaciones incorrectas y garantizar que cada celda tenga máximo un vehículo.

### Criterios de Aceptación:
- [ ] En el formulario de registro de vehículo, el selector de celdas muestra únicamente celdas con estado "disponible".
- [ ] Las celdas se agrupan o filtran automáticamente según el tipo de vehículo seleccionado.
- [ ] Al asignar la celda al guardar el vehículo, el estado de la celda cambia automáticamente a "ocupada".
- [ ] Si no hay celdas disponibles del tipo requerido, el sistema muestra: *"No hay celdas disponibles para este tipo de vehículo."*
- [ ] Al desactivar un vehículo, la celda asignada vuelve automáticamente a estado "disponible".

**Estimación:** 3 puntos de historia  
**Prioridad:** Alta

---

## Resumen de Estimación — Iteración 2

| Historia | Descripción                              | Módulo   | Puntos | Prioridad |
|----------|------------------------------------------|----------|--------|-----------|
| HU-10    | Buscar y consultar usuarios              | Usuarios | 2      | Alta      |
| HU-11    | Ver perfil detallado de usuario          | Usuarios | 2      | Alta      |
| HU-12    | Editar información de usuario            | Usuarios | 2      | Alta      |
| HU-13    | Desactivar usuario                       | Usuarios | 3      | Alta      |
| HU-14    | Crear nueva celda                        | Celdas   | 2      | Alta      |
| HU-15    | Editar celda                             | Celdas   | 2      | Media     |
| HU-16    | Visualizar y filtrar celdas              | Celdas   | 2      | Alta      |
| HU-17    | Asignar celda disponible a vehículo      | Celdas   | 3      | Alta      |
| **Total**|                                          |          | **18** |           |

---

## Acumulado Total del Proyecto

| Iteración    | Historias          | Puntos |
|--------------|--------------------|--------|
| Iteración 1  | HU-01 a HU-09      | 22     |
| Iteración 2  | HU-10 a HU-17      | 18     |
| **Total**    | **17 historias**   | **40** |
