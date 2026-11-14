# Pruebas — línea base v1.0

| PR | RF | Descripción |
|---|---|---|
| PR-01 | RF-01 | Registrar un pedido válido con 2 ítems genera pedido en estado «Registrado» |
| PR-02 | RF-02 | Producto sin stock ofrece alternativa; si se rechaza, cancela sin cobro (E1) |
| PR-03 | RF-03 | Cancelar un pedido antes de su preparación libera el stock |
| PR-04 | RF-04 | El pedido solo avanza por los estados permitidos (Registrado → En preparación → Listo) |
| PR-05 | RF-05 | Faltante de insumos anula el ítem, notifica al cajero y reembolsa parcialmente (E3) |
| PR-06 | RF-06 | Despacho y confirmación de entrega cambian el pedido a «Entregado» |
| PR-07 | RF-07 | Cobro válido (efectivo o tarjeta) cambia el pedido a «Pagado» |
| PR-08 | RF-07 | Pago rechazado: 2 reintentos y anulación del pedido con liberación de stock (E2) |
| PR-09 | RF-08 | Emisión de comprobante para todo pedido cobrado |
| PR-10 | RF-09 | Anulación de comprobante y reembolso registran el movimiento |
