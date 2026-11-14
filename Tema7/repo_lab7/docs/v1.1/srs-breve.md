# SRS breve — versión v1.1 (CR-001)

| RF | Requisito | OBJ | HU | CU | Estado |
|---|---|---|---|---|---|
| RF-01 | Registrar pedido | OBJ-1 | HU-01, HU-02 | CU-01 | Base |
| RF-02 | Validar disponibilidad | OBJ-1 | HU-03 | CU-02 | Base |
| RF-03 | Modificar o cancelar pedido | OBJ-1 | HU-04, HU-05 | CU-03 | Base |
| RF-04 | Preparar pedido y estados | OBJ-2 | HU-06, HU-07 | CU-04 | Base |
| RF-05 | Gestionar faltante de insumos | OBJ-2 | HU-08 | CU-05 | Base |
| RF-06 | Despachar y confirmar entrega | OBJ-2 | HU-09, HU-10 | CU-06 | Base |
| RF-07 | Registrar y validar cobro | OBJ-3 | HU-11, HU-12 | CU-07 | Modificado |
| RF-08 | Emitir comprobante | OBJ-3 | HU-13, HU-16 | CU-08 | Modificado |
| RF-09 | Anular comprobante o reembolsar | OBJ-3 | HU-14 | CU-09 | Revisado (sin cambio) |
| RF-10 | Cobrar con billetera digital (Yape/Plin) | OBJ-3 | HU-15 | CU-10 | Nuevo |

## Requisitos modificados o nuevos

**RF-07 (modificado) — Registrar y validar cobro.** El sistema registrará el cobro de un pedido con medio de pago Efectivo, Tarjeta o Billetera digital (Yape/Plin) y validará el monto antes de cambiar el pedido a «Pagado». Si el cobro es rechazado, aplica E2 (hasta 2 reintentos; al agotarlos se anula el pedido y se libera el stock).

**RF-08 (modificado) — Emitir comprobante.** El comprobante indicará el medio de pago y, cuando corresponda, el número de operación.

**RF-10 (nuevo) — Cobrar con billetera digital (Yape/Plin).** El sistema generará una solicitud de pago por el monto total, registrará el número de operación y confirmará el pago a través de la interfaz `PasarelaBilletera`. Si la billetera rechaza la operación o no confirma en 120 s, aplica E2. En esta versión la confirmación se obtiene mediante un simulador (`SimuladorBilletera`); la integración real con la billetera queda fuera de alcance.

**RF-09 (revisado, sin cambio).** El reembolso de pagos hechos con billetera digital se difiere a v1.2 (riesgo R11).

## Historias de usuario nuevas
- **HU-15** Como cajero, quiero cobrar con Yape/Plin registrando el número de operación, para no validar capturas de pantalla manualmente.
- **HU-16** Como cliente, quiero que mi comprobante indique el medio de pago usado, para sustentar mi compra.
