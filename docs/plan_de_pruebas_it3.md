# Plan de Pruebas Resumido — Iteración 3
## Parqueadero Autos Colombia — Gestión de Pagos

**Proyecto:** Sistema de Gestión Parqueadero Autos Colombia  
**Versión:** 1.3  
**Fecha:** Marzo 2026  
**Módulo evaluado:** Gestión de Pagos

---

## 1. Objetivo

Verificar que el módulo de **Gestión de Pagos** implementado en la Iteración 3 cumple con los requerimientos funcionales RF-19 al RF-25 y las historias de usuario HU-18 a HU-23, garantizando la calidad del sistema antes de su entrega final.

---

## 2. Alcance

| Módulo           | Funcionalidades cubiertas                                              |
|------------------|------------------------------------------------------------------------|
| Gestión de Pagos | Registrar, consultar, filtrar pagos · Auto-calcular tarifa · Prevenir duplicados · Recaudo en dashboard |

**Fuera del alcance:** Autenticación, gestión de usuarios, gestión de celdas, movimientos, novedades.

---

## 3. Tipos de Prueba

| Tipo                  | Descripción                                                  |
|-----------------------|--------------------------------------------------------------|
| Pruebas Funcionales   | Verifican el cumplimiento de los RF                          |
| Pruebas de Validación | Verifican reglas de negocio y restricciones de datos         |
| Pruebas de Flujo      | Verifican flujos positivos (happy path) y negativos (sad path) |
| Pruebas AJAX          | Verifican la carga dinámica de vehículos y auto-cálculo      |
| Pruebas de Interfaz   | Verifican mensajes, badges y visualización correcta          |

---

## 4. Casos de Prueba — Módulo: Gestión de Pagos

---

### CP-P01 — Registrar pago con datos válidos

| Campo                 | Detalle |
|-----------------------|---------|
| **ID**                | CP-P01 |
| **Historia / RF**     | HU-18, RF-19 |
| **Precondición**      | Existen usuario activo y vehículo activo con celda asignada. No hay pago para ese vehículo en marzo 2026. |
| **Datos de entrada**  | Usuario: Carlos Pérez · Vehículo: ABC-123 · Mes: Marzo · Año: 2026 · Método: Efectivo |
| **Pasos**             | 1. Ir a Pagos → Nuevo Pago. 2. Seleccionar usuario. 3. Seleccionar vehículo. 4. Verificar que el monto se pre-carga. 5. Seleccionar mes, año y método. 6. Clic en "Registrar Pago". |
| **Resultado esperado** | Pago creado con estado "pagado". Aparece en el historial. Mensaje: "Pago registrado exitosamente." |
| **Resultado obtenido** | |
| **Estado**            | ⬜ Pendiente / ✅ Aprobado / ❌ Fallido |

---

### CP-P02 — Registrar pago duplicado (mismo vehículo, mismo período)

| Campo                 | Detalle |
|-----------------------|---------|
| **ID**                | CP-P02 |
| **Historia / RF**     | HU-22, RF-23 |
| **Precondición**      | Ya existe un pago para el vehículo ABC-123 en marzo 2026. |
| **Datos de entrada**  | Vehículo: ABC-123 · Mes: Marzo · Año: 2026 |
| **Pasos**             | 1. Ir a Pagos → Nuevo Pago. 2. Seleccionar el mismo usuario y vehículo. 3. Seleccionar el mismo período. 4. Guardar. |
| **Resultado esperado** | Error: "Ya existe un pago registrado para este vehículo en el período seleccionado." El pago NO se registra. |
| **Resultado obtenido** | |
| **Estado**            | ⬜ Pendiente / ✅ Aprobado / ❌ Fallido |

---

### CP-P03 — Registrar pago con monto cero

| Campo                 | Detalle |
|-----------------------|---------|
| **ID**                | CP-P03 |
| **Historia / RF**     | RF-19, RNF-17 |
| **Precondición**      | Ninguna. |
| **Datos de entrada**  | Monto: 0 |
| **Pasos**             | 1. Ir a Pagos → Nuevo Pago. 2. Ingresar monto 0. 3. Guardar. |
| **Resultado esperado** | Error de validación. El pago NO se registra. |
| **Resultado obtenido** | |
| **Estado**            | ⬜ Pendiente / ✅ Aprobado / ❌ Fallido |

---

### CP-P04 — Registrar pago con campos vacíos

| Campo                 | Detalle |
|-----------------------|---------|
| **ID**                | CP-P04 |
| **Historia / RF**     | RF-19, RNF-18 |
| **Precondición**      | Ninguna. |
| **Datos de entrada**  | Todos los campos vacíos. |
| **Pasos**             | 1. Ir a Pagos → Nuevo Pago. 2. No ingresar datos. 3. Clic en "Registrar Pago". |
| **Resultado esperado** | Mensajes de validación en los campos obligatorios. El formulario NO se envía. |
| **Resultado obtenido** | |
| **Estado**            | ⬜ Pendiente / ✅ Aprobado / ❌ Fallido |

---

### CP-P05 — Auto-carga de vehículos al seleccionar usuario (AJAX)

| Campo                 | Detalle |
|-----------------------|---------|
| **ID**                | CP-P05 |
| **Historia / RF**     | HU-19, RF-21 |
| **Precondición**      | El usuario Carlos Pérez tiene 2 vehículos activos registrados. |
| **Datos de entrada**  | Seleccionar usuario: "Carlos Pérez" |
| **Pasos**             | 1. Ir a Pagos → Nuevo Pago. 2. Seleccionar el usuario Carlos Pérez en el selector. |
| **Resultado esperado** | Sin recargar la página, el selector de vehículo se llena con los 2 vehículos del usuario, mostrando placa y tarifa de cada uno. |
| **Resultado obtenido** | |
| **Estado**            | ⬜ Pendiente / ✅ Aprobado / ❌ Fallido |

---

### CP-P06 — Auto-cálculo del monto al seleccionar vehículo

| Campo                 | Detalle |
|-----------------------|---------|
| **ID**                | CP-P06 |
| **Historia / RF**     | HU-19, RF-21 |
| **Precondición**      | El vehículo ABC-123 tiene asignada la celda 1001 con tarifa $150,000. |
| **Datos de entrada**  | Seleccionar vehículo: ABC-123 |
| **Pasos**             | 1. En el formulario de nuevo pago, con el usuario ya seleccionado. 2. Seleccionar el vehículo ABC-123. |
| **Resultado esperado** | El campo "Monto" se actualiza automáticamente con $150,000 sin recargar la página. |
| **Resultado obtenido** | |
| **Estado**            | ⬜ Pendiente / ✅ Aprobado / ❌ Fallido |

---

### CP-P07 — Usuario sin vehículos activos

| Campo                 | Detalle |
|-----------------------|---------|
| **ID**                | CP-P07 |
| **Historia / RF**     | HU-19, RF-21 |
| **Precondición**      | El usuario seleccionado no tiene vehículos activos. |
| **Datos de entrada**  | Seleccionar usuario sin vehículos. |
| **Pasos**             | 1. Ir a Pagos → Nuevo Pago. 2. Seleccionar usuario sin vehículos. |
| **Resultado esperado** | El selector de vehículo muestra: "Este usuario no tiene vehículos registrados." El campo monto queda vacío. |
| **Resultado obtenido** | |
| **Estado**            | ⬜ Pendiente / ✅ Aprobado / ❌ Fallido |

---

### CP-P08 — Consultar historial de pagos

| Campo                 | Detalle |
|-----------------------|---------|
| **ID**                | CP-P08 |
| **Historia / RF**     | HU-20, RF-20 |
| **Precondición**      | Existen pagos registrados en el sistema. |
| **Pasos**             | 1. Ir al módulo de Pagos. |
| **Resultado esperado** | Se muestra lista paginada con: usuario, placa, período, monto, método, fecha y badge de estado con color correspondiente. Ordenada por fecha descendente. |
| **Resultado obtenido** | |
| **Estado**            | ⬜ Pendiente / ✅ Aprobado / ❌ Fallido |

---

### CP-P09 — Filtrar pagos por estado "pagado"

| Campo                 | Detalle |
|-----------------------|---------|
| **ID**                | CP-P09 |
| **Historia / RF**     | HU-21, RF-22 |
| **Precondición**      | Existen pagos con diferentes estados. |
| **Datos de entrada**  | Filtro estado: "pagado" |
| **Pasos**             | 1. Ir a Pagos. 2. Seleccionar filtro Estado: Pagado. 3. Clic en Filtrar. |
| **Resultado esperado** | Solo se muestran pagos con badge verde (estado pagado). |
| **Resultado obtenido** | |
| **Estado**            | ⬜ Pendiente / ✅ Aprobado / ❌ Fallido |

---

### CP-P10 — Filtrar pagos por mes y año específico

| Campo                 | Detalle |
|-----------------------|---------|
| **ID**                | CP-P10 |
| **Historia / RF**     | HU-21, RF-22 |
| **Precondición**      | Existen pagos de diferentes meses. |
| **Datos de entrada**  | Mes: Marzo (3) · Año: 2026 |
| **Pasos**             | 1. Ir a Pagos. 2. Seleccionar Mes: Marzo, Año: 2026. 3. Filtrar. |
| **Resultado esperado** | Solo se muestran pagos del período marzo 2026. |
| **Resultado obtenido** | |
| **Estado**            | ⬜ Pendiente / ✅ Aprobado / ❌ Fallido |

---

### CP-P11 — Verificar recaudo en el dashboard

| Campo                 | Detalle |
|-----------------------|---------|
| **ID**                | CP-P11 |
| **Historia / RF**     | HU-23, RF-24 |
| **Precondición**      | Existen pagos con estado "pagado" en el mes actual. |
| **Pasos**             | 1. Ir al Dashboard. 2. Observar la tarjeta de Recaudo. |
| **Resultado esperado** | La tarjeta muestra la suma correcta en COP de todos los pagos "pagado" del mes actual. |
| **Resultado obtenido** | |
| **Estado**            | ⬜ Pendiente / ✅ Aprobado / ❌ Fallido |

---

### CP-P12 — Verificar badges de estado en historial

| Campo                 | Detalle |
|-----------------------|---------|
| **ID**                | CP-P12 |
| **Historia / RF**     | RF-25, RNF-19 |
| **Precondición**      | Existen pagos con los tres estados posibles. |
| **Pasos**             | 1. Ir al historial de pagos sin filtros. |
| **Resultado esperado** | Pagos "pagado" tienen badge verde, "pendiente" badge amarillo y "vencido" badge rojo. |
| **Resultado obtenido** | |
| **Estado**            | ⬜ Pendiente / ✅ Aprobado / ❌ Fallido |

---

## 5. Matriz de Trazabilidad

| Caso de Prueba | Historia de Usuario | Req. Funcional | Req. No Funcional |
|----------------|---------------------|----------------|-------------------|
| CP-P01         | HU-18               | RF-19          | RNF-17, RNF-18    |
| CP-P02         | HU-22               | RF-23          | RNF-17            |
| CP-P03         | HU-18               | RF-19          | RNF-17            |
| CP-P04         | HU-18               | RF-19          | RNF-18            |
| CP-P05         | HU-19               | RF-21          | RNF-16, RNF-18    |
| CP-P06         | HU-19               | RF-21          | RNF-16, RNF-18    |
| CP-P07         | HU-19               | RF-21          | RNF-18            |
| CP-P08         | HU-20               | RF-20          | RNF-16, RNF-19    |
| CP-P09         | HU-21               | RF-22          | RNF-19            |
| CP-P10         | HU-21               | RF-22          | RNF-16            |
| CP-P11         | HU-23               | RF-24          | RNF-20            |
| CP-P12         | HU-20               | RF-25          | RNF-19            |

---

## 6. Criterios de Aceptación del Plan

| Criterio                                        | Condición de Éxito        |
|-------------------------------------------------|---------------------------|
| Casos de prueba ejecutados                      | 100% ejecutados           |
| Casos de prueba aprobados                       | ≥ 90% aprobados           |
| Defectos críticos sin resolver                  | 0 defectos de severidad Alta |
| Tiempo de registro de un pago                   | < 1 segundo               |
| Tiempo de respuesta AJAX (carga vehículos)      | < 500 ms                  |
| Listado de pagos (10,000 registros)             | < 2 segundos              |

---

## 7. Ambiente de Pruebas

| Componente        | Detalle                                         |
|-------------------|-------------------------------------------------|
| Sistema Operativo | Windows 10 / macOS / Ubuntu 20.04+              |
| Navegador         | Google Chrome 120+, Firefox 120+, Edge 120+     |
| Lenguaje          | Python 3.10+                                    |
| Framework         | Flask 3.0.0                                     |
| Base de datos     | SQLite (ambiente de pruebas local)              |
| URL               | http://localhost:5000                           |
| Datos de prueba   | Ejecutar `database/seed.sql` para datos iniciales |
