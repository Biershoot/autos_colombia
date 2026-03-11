# Plan de Pruebas Resumido — Iteración 2
## Parqueadero Autos Colombia
## Gestión de Usuarios y Gestión de Celdas

**Proyecto:** Sistema de Gestión Parqueadero Autos Colombia  
**Versión:** 1.2  
**Fecha:** Marzo 2026  
**Responsable:** Equipo de Desarrollo  

---

## 1. Objetivo del Plan de Pruebas

Verificar que los módulos de **Gestión de Usuarios** y **Gestión de Celdas** implementados en la Iteración 2 cumplen con los requerimientos funcionales definidos (RF-10 al RF-18) y con las historias de usuario HU-10 a HU-17, garantizando la calidad del sistema antes de su entrega.

---

## 2. Alcance

| Módulo              | Funcionalidades cubiertas                                          |
|---------------------|--------------------------------------------------------------------|
| Gestión de Usuarios | Registrar, buscar, ver perfil, editar, desactivar/reactivar        |
| Gestión de Celdas   | Crear, editar, visualizar panel, filtrar, asignar, liberar         |

**Fuera del alcance (Iteración 2):** Autenticación, gestión de pagos, registro de movimientos, gestión de incidentes.

---

## 3. Tipos de Prueba

| Tipo de Prueba          | Descripción                                            |
|-------------------------|--------------------------------------------------------|
| Pruebas Funcionales     | Verifican el cumplimiento de los RF                    |
| Pruebas de Validación   | Verifican reglas de negocio y datos                    |
| Pruebas de Flujo        | Verifican flujos positivos y negativos (happy/sad path)|
| Pruebas de Interfaz     | Verifican que los mensajes y la UI respondan correctamente |

---

## 4. Casos de Prueba — Módulo: Gestión de Usuarios

---

### CP-U01 — Registrar usuario con datos válidos

| Campo               | Detalle                                              |
|---------------------|------------------------------------------------------|
| **ID**              | CP-U01                                               |
| **Historia**        | HU-04, RF-10                                         |
| **Precondición**    | El sistema está funcionando. No existe usuario con el mismo documento ni correo. |
| **Datos de entrada**| Nombre: "Juan Carlos Pérez", Documento: "12345678", Correo: "juan@correo.com", Teléfono: "3001234567", Dirección: "Calle 10 #20-30" |
| **Pasos**           | 1. Ir a Usuarios → Nuevo Usuario. 2. Ingresar los datos. 3. Clic en "Guardar Usuario". |
| **Resultado esperado** | El usuario es creado con estado activo. El sistema redirige al perfil del usuario con el mensaje "Usuario creado exitosamente." |
| **Resultado obtenido** | |
| **Estado**          | ⬜ Pendiente / ✅ Aprobado / ❌ Fallido |

---

### CP-U02 — Registrar usuario con documento duplicado

| Campo               | Detalle                                              |
|---------------------|------------------------------------------------------|
| **ID**              | CP-U02                                               |
| **Historia**        | RF-10 (flujo alternativo A)                          |
| **Precondición**    | Existe un usuario con documento "12345678".          |
| **Datos de entrada**| Documento: "12345678", demás datos diferentes y válidos. |
| **Pasos**           | 1. Ir a Usuarios → Nuevo Usuario. 2. Ingresar el documento ya existente. 3. Clic en "Guardar Usuario". |
| **Resultado esperado** | El sistema muestra el error: "El número de documento ya se encuentra registrado." El usuario NO es creado. |
| **Resultado obtenido** | |
| **Estado**          | ⬜ Pendiente / ✅ Aprobado / ❌ Fallido |

---

### CP-U03 — Registrar usuario con correo duplicado

| Campo               | Detalle                                              |
|---------------------|------------------------------------------------------|
| **ID**              | CP-U03                                               |
| **Historia**        | RF-10 (flujo alternativo B)                          |
| **Precondición**    | Existe un usuario con correo "juan@correo.com".      |
| **Datos de entrada**| Correo: "juan@correo.com", demás datos diferentes y válidos. |
| **Pasos**           | 1. Ir a Usuarios → Nuevo Usuario. 2. Ingresar el correo ya existente. 3. Clic en "Guardar". |
| **Resultado esperado** | El sistema muestra el error: "El correo electrónico ya se encuentra registrado." El usuario NO es creado. |
| **Resultado obtenido** | |
| **Estado**          | ⬜ Pendiente / ✅ Aprobado / ❌ Fallido |

---

### CP-U04 — Registrar usuario con campos vacíos

| Campo               | Detalle                                              |
|---------------------|------------------------------------------------------|
| **ID**              | CP-U04                                               |
| **Historia**        | RF-10, RNF-10                                        |
| **Precondición**    | Ninguna.                                             |
| **Datos de entrada**| Todos los campos vacíos.                             |
| **Pasos**           | 1. Ir a Usuarios → Nuevo Usuario. 2. No ingresar ningún dato. 3. Clic en "Guardar". |
| **Resultado esperado** | El sistema muestra mensajes de validación en los campos obligatorios. El formulario NO se envía. |
| **Resultado obtenido** | |
| **Estado**          | ⬜ Pendiente / ✅ Aprobado / ❌ Fallido |

---

### CP-U05 — Buscar usuario por nombre

| Campo               | Detalle                                              |
|---------------------|------------------------------------------------------|
| **ID**              | CP-U05                                               |
| **Historia**        | HU-10, RF-11                                         |
| **Precondición**    | Existen usuarios registrados, incluyendo uno de nombre "María López". |
| **Datos de entrada**| Término de búsqueda: "María"                         |
| **Pasos**           | 1. Ir al módulo de Usuarios. 2. Escribir "María" en el campo de búsqueda. |
| **Resultado esperado** | La lista se filtra mostrando únicamente usuarios cuyo nombre contenga "María". |
| **Resultado obtenido** | |
| **Estado**          | ⬜ Pendiente / ✅ Aprobado / ❌ Fallido |

---

### CP-U06 — Buscar usuario con criterio sin resultados

| Campo               | Detalle                                              |
|---------------------|------------------------------------------------------|
| **ID**              | CP-U06                                               |
| **Historia**        | HU-10, RF-11                                         |
| **Precondición**    | No existe ningún usuario con nombre "XXXXXXXX".      |
| **Datos de entrada**| Término de búsqueda: "XXXXXXXX"                      |
| **Pasos**           | 1. Ir al módulo de Usuarios. 2. Escribir "XXXXXXXX" en la búsqueda. |
| **Resultado esperado** | La lista muestra el mensaje: "No se encontraron usuarios con ese criterio." |
| **Resultado obtenido** | |
| **Estado**          | ⬜ Pendiente / ✅ Aprobado / ❌ Fallido |

---

### CP-U07 — Editar datos de usuario

| Campo               | Detalle                                              |
|---------------------|------------------------------------------------------|
| **ID**              | CP-U07                                               |
| **Historia**        | HU-12, RF-13                                         |
| **Precondición**    | Existe un usuario activo en el sistema.              |
| **Datos de entrada**| Nuevo teléfono: "3109876543", nueva dirección: "Av. Siempre Viva #742" |
| **Pasos**           | 1. Ir al perfil del usuario. 2. Clic en "Editar". 3. Modificar teléfono y dirección. 4. Clic en "Guardar". |
| **Resultado esperado** | El sistema guarda los cambios. El perfil del usuario muestra los datos actualizados con el mensaje "Usuario actualizado correctamente." |
| **Resultado obtenido** | |
| **Estado**          | ⬜ Pendiente / ✅ Aprobado / ❌ Fallido |

---

### CP-U08 — Verificar que el documento es de solo lectura en edición

| Campo               | Detalle                                              |
|---------------------|------------------------------------------------------|
| **ID**              | CP-U08                                               |
| **Historia**        | RF-13 (restricción)                                  |
| **Precondición**    | Existe un usuario activo.                            |
| **Pasos**           | 1. Ir al perfil del usuario. 2. Clic en "Editar". 3. Intentar modificar el campo "Número de Documento". |
| **Resultado esperado** | El campo "Número de Documento" está deshabilitado (readonly) y no puede ser modificado. |
| **Resultado obtenido** | |
| **Estado**          | ⬜ Pendiente / ✅ Aprobado / ❌ Fallido |

---

### CP-U09 — Desactivar usuario sin vehículos activos

| Campo               | Detalle                                              |
|---------------------|------------------------------------------------------|
| **ID**              | CP-U09                                               |
| **Historia**        | HU-13, RF-14                                         |
| **Precondición**    | Existe un usuario activo sin vehículos activos asociados. |
| **Pasos**           | 1. Ir al perfil del usuario. 2. Clic en "Desactivar Usuario". 3. Confirmar la acción. |
| **Resultado esperado** | El usuario pasa a estado inactivo. El sistema muestra el mensaje "El usuario ha sido desactivado exitosamente." El usuario desaparece del listado principal. |
| **Resultado obtenido** | |
| **Estado**          | ⬜ Pendiente / ✅ Aprobado / ❌ Fallido |

---

### CP-U10 — Desactivar usuario con vehículos activos (flujo alternativo)

| Campo               | Detalle                                              |
|---------------------|------------------------------------------------------|
| **ID**              | CP-U10                                               |
| **Historia**        | HU-13, RF-14 (flujo alternativo)                     |
| **Precondición**    | Existe un usuario activo con al menos un vehículo activo. |
| **Pasos**           | 1. Ir al perfil del usuario. 2. Clic en "Desactivar Usuario". |
| **Resultado esperado** | El sistema muestra una advertencia indicando que el usuario tiene vehículos activos y no puede ser desactivado hasta desactivarlos primero. |
| **Resultado obtenido** | |
| **Estado**          | ⬜ Pendiente / ✅ Aprobado / ❌ Fallido |

---

## 5. Casos de Prueba — Módulo: Gestión de Celdas

---

### CP-C01 — Crear celda con datos válidos

| Campo               | Detalle                                              |
|---------------------|------------------------------------------------------|
| **ID**              | CP-C01                                               |
| **Historia**        | HU-14, RF-15                                         |
| **Precondición**    | No existe una celda con el número "3001".            |
| **Datos de entrada**| Número: "3001", Tipo: "carro", Piso: 3, Tarifa: 150000 |
| **Pasos**           | 1. Ir a Celdas → Nueva Celda. 2. Ingresar los datos. 3. Clic en "Guardar Celda". |
| **Resultado esperado** | La celda es creada con estado "disponible". Aparece en el panel de celdas. El sistema muestra "Celda creada exitosamente." |
| **Resultado obtenido** | |
| **Estado**          | ⬜ Pendiente / ✅ Aprobado / ❌ Fallido |

---

### CP-C02 — Crear celda con número duplicado

| Campo               | Detalle                                              |
|---------------------|------------------------------------------------------|
| **ID**              | CP-C02                                               |
| **Historia**        | RF-15 (flujo alternativo)                            |
| **Precondición**    | Existe una celda con número "1001".                  |
| **Datos de entrada**| Número: "1001", demás datos válidos.                 |
| **Pasos**           | 1. Ir a Celdas → Nueva Celda. 2. Ingresar número "1001". 3. Clic en "Guardar". |
| **Resultado esperado** | El sistema muestra el error: "El número de celda ya está registrado." La celda NO es creada. |
| **Resultado obtenido** | |
| **Estado**          | ⬜ Pendiente / ✅ Aprobado / ❌ Fallido |

---

### CP-C03 — Crear celda con tarifa negativa o cero

| Campo               | Detalle                                              |
|---------------------|------------------------------------------------------|
| **ID**              | CP-C03                                               |
| **Historia**        | RF-15 (restricciones), RNF-12                        |
| **Precondición**    | Ninguna.                                             |
| **Datos de entrada**| Tarifa: -50000 o 0                                   |
| **Pasos**           | 1. Ir a Celdas → Nueva Celda. 2. Ingresar tarifa negativa o cero. 3. Clic en "Guardar". |
| **Resultado esperado** | El sistema muestra un error de validación. La celda NO es creada. |
| **Resultado obtenido** | |
| **Estado**          | ⬜ Pendiente / ✅ Aprobado / ❌ Fallido |

---

### CP-C04 — Editar tarifa de celda disponible

| Campo               | Detalle                                              |
|---------------------|------------------------------------------------------|
| **ID**              | CP-C04                                               |
| **Historia**        | HU-15, RF-16                                         |
| **Precondición**    | Existe una celda disponible con tarifa $150,000.     |
| **Datos de entrada**| Nueva tarifa: 175000                                 |
| **Pasos**           | 1. Ir al panel de Celdas. 2. Seleccionar la celda. 3. Clic en "Editar". 4. Cambiar la tarifa. 5. Guardar. |
| **Resultado esperado** | La celda queda con la tarifa actualizada a $175,000. El sistema muestra "Celda actualizada correctamente." |
| **Resultado obtenido** | |
| **Estado**          | ⬜ Pendiente / ✅ Aprobado / ❌ Fallido |

---

### CP-C05 — Verificar que el número de celda no se puede editar

| Campo               | Detalle                                              |
|---------------------|------------------------------------------------------|
| **ID**              | CP-C05                                               |
| **Historia**        | RF-16 (restricción)                                  |
| **Precondición**    | Existe una celda en el sistema.                      |
| **Pasos**           | 1. Ir al panel de Celdas. 2. Seleccionar la celda. 3. Clic en "Editar". 4. Intentar modificar el número de celda. |
| **Resultado esperado** | El campo "Número de Celda" está deshabilitado (readonly) y no puede ser modificado. |
| **Resultado obtenido** | |
| **Estado**          | ⬜ Pendiente / ✅ Aprobado / ❌ Fallido |

---

### CP-C06 — Visualizar panel de celdas

| Campo               | Detalle                                              |
|---------------------|------------------------------------------------------|
| **ID**              | CP-C06                                               |
| **Historia**        | HU-16, RF-17                                         |
| **Precondición**    | Existen celdas registradas en el sistema.            |
| **Pasos**           | 1. Ir al módulo de Celdas.                           |
| **Resultado esperado** | El sistema muestra todas las celdas en formato de cuadrícula. Las celdas disponibles tienen fondo verde y las ocupadas tienen fondo amarillo. Se muestran las 3 tarjetas de estadísticas. |
| **Resultado obtenido** | |
| **Estado**          | ⬜ Pendiente / ✅ Aprobado / ❌ Fallido |

---

### CP-C07 — Filtrar celdas por tipo

| Campo               | Detalle                                              |
|---------------------|------------------------------------------------------|
| **ID**              | CP-C07                                               |
| **Historia**        | HU-16, RF-17                                         |
| **Precondición**    | Existen celdas de diferentes tipos en el sistema.    |
| **Datos de entrada**| Filtro tipo: "moto"                                  |
| **Pasos**           | 1. Ir al módulo de Celdas. 2. Seleccionar filtro "Tipo: Moto". |
| **Resultado esperado** | El panel muestra únicamente celdas de tipo "moto". Las estadísticas se actualizan para reflejar solo el subconjunto filtrado. |
| **Resultado obtenido** | |
| **Estado**          | ⬜ Pendiente / ✅ Aprobado / ❌ Fallido |

---

### CP-C08 — Filtrar celdas por estado disponible

| Campo               | Detalle                                              |
|---------------------|------------------------------------------------------|
| **ID**              | CP-C08                                               |
| **Historia**        | HU-16, RF-17                                         |
| **Precondición**    | Existen celdas disponibles y ocupadas.               |
| **Datos de entrada**| Filtro estado: "disponible"                          |
| **Pasos**           | 1. Ir al módulo de Celdas. 2. Seleccionar filtro "Estado: Disponible". |
| **Resultado esperado** | El panel muestra únicamente celdas con estado "disponible" (todas con fondo verde). |
| **Resultado obtenido** | |
| **Estado**          | ⬜ Pendiente / ✅ Aprobado / ❌ Fallido |

---

### CP-C09 — Estado de celda cambia al registrar vehículo

| Campo               | Detalle                                              |
|---------------------|------------------------------------------------------|
| **ID**              | CP-C09                                               |
| **Historia**        | HU-17, RF-17, RNF-12                                 |
| **Precondición**    | Existe la celda "1005" con estado "disponible".      |
| **Pasos**           | 1. Registrar un nuevo vehículo. 2. Asignar la celda "1005". 3. Guardar el vehículo. 4. Ir al panel de Celdas y verificar celda "1005". |
| **Resultado esperado** | La celda "1005" ahora aparece con estado "ocupada" (fondo amarillo) en el panel. |
| **Resultado obtenido** | |
| **Estado**          | ⬜ Pendiente / ✅ Aprobado / ❌ Fallido |

---

### CP-C10 — Estado de celda vuelve a disponible al desactivar vehículo

| Campo               | Detalle                                              |
|---------------------|------------------------------------------------------|
| **ID**              | CP-C10                                               |
| **Historia**        | HU-17, RNF-12                                        |
| **Precondición**    | Existe un vehículo activo asignado a la celda "1005" (estado: ocupada). |
| **Pasos**           | 1. Ir al detalle del vehículo. 2. Desactivar el vehículo. 3. Ir al panel de Celdas y verificar celda "1005". |
| **Resultado esperado** | La celda "1005" vuelve a estado "disponible" (fondo verde) automáticamente. |
| **Resultado obtenido** | |
| **Estado**          | ⬜ Pendiente / ✅ Aprobado / ❌ Fallido |

---

## 6. Matriz de Trazabilidad

| Caso de Prueba | Historia de Usuario | Req. Funcional | Req. No Funcional |
|----------------|---------------------|----------------|-------------------|
| CP-U01         | HU-04, HU-10        | RF-10          | RNF-10            |
| CP-U02         | HU-04               | RF-10          | RNF-11            |
| CP-U03         | HU-04               | RF-10          | RNF-11            |
| CP-U04         | HU-10               | RF-10          | RNF-10            |
| CP-U05         | HU-10               | RF-11          | RNF-09            |
| CP-U06         | HU-10               | RF-11          | RNF-10            |
| CP-U07         | HU-12               | RF-13          | RNF-14            |
| CP-U08         | HU-12               | RF-13          | —                 |
| CP-U09         | HU-13               | RF-14          | RNF-11            |
| CP-U10         | HU-13               | RF-14          | RNF-11            |
| CP-C01         | HU-14               | RF-15          | RNF-12            |
| CP-C02         | HU-14               | RF-15          | RNF-12            |
| CP-C03         | HU-14               | RF-15          | RNF-12            |
| CP-C04         | HU-15               | RF-16          | —                 |
| CP-C05         | HU-15               | RF-16          | —                 |
| CP-C06         | HU-16               | RF-17          | RNF-13, RNF-09    |
| CP-C07         | HU-16               | RF-17          | RNF-13            |
| CP-C08         | HU-16               | RF-17          | RNF-13            |
| CP-C09         | HU-17               | RF-17          | RNF-12            |
| CP-C10         | HU-17               | RF-17          | RNF-12            |

---

## 7. Criterios de Aceptación del Plan

| Criterio                                               | Condición de Éxito              |
|--------------------------------------------------------|---------------------------------|
| Todos los casos de prueba funcionales ejecutados       | 100% ejecutados                 |
| Casos de prueba aprobados                              | ≥ 90% aprobados                 |
| Cero defectos críticos sin resolver                    | 0 defectos de severidad Alta    |
| Tiempo de respuesta módulo usuarios (listado)          | < 1.5 segundos                  |
| Tiempo de respuesta panel de celdas                    | < 1 segundo                     |

---

## 8. Ambiente de Pruebas

| Componente        | Detalle                                         |
|-------------------|-------------------------------------------------|
| Sistema Operativo | Windows 10 / macOS / Ubuntu 20.04+              |
| Navegador         | Google Chrome 120+, Firefox 120+, Edge 120+     |
| Lenguaje          | Python 3.10+                                    |
| Framework         | Flask 3.0.0                                     |
| Base de datos     | SQLite (ambiente de pruebas local)              |
| URL               | http://localhost:5000                           |
| Datos de prueba   | Ejecutar `database/seed.sql` para datos iniciales |
