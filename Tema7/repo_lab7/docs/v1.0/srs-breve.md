# SRS breve — línea base v1.0 (etiqueta v1.0)

| RF | Requisito | OBJ | HU | CU |
|---|---|---|---|---|
| RF-01 | Registrar pedido | OBJ-1 | HU-01, HU-02 | CU-01 |
| RF-02 | Validar disponibilidad | OBJ-1 | HU-03 | CU-02 |
| RF-03 | Modificar o cancelar pedido | OBJ-1 | HU-04, HU-05 | CU-03 |
| RF-04 | Preparar pedido y estados | OBJ-2 | HU-06, HU-07 | CU-04 |
| RF-05 | Gestionar faltante de insumos | OBJ-2 | HU-08 | CU-05 |
| RF-06 | Despachar y confirmar entrega | OBJ-2 | HU-09, HU-10 | CU-06 |
| RF-07 | Registrar y validar cobro | OBJ-3 | HU-11, HU-12 | CU-07 |
| RF-08 | Emitir comprobante | OBJ-3 | HU-13 | CU-08 |
| RF-09 | Anular comprobante o reembolsar | OBJ-3 | HU-14 | CU-09 |

**Nota RF-07 (v1.0):** medios de pago admitidos: efectivo y tarjeta. Excepción E2: hasta 2 reintentos; al agotarlos se anula el pedido y se libera el stock.
