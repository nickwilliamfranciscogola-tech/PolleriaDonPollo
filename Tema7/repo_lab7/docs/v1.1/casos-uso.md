# Casos de uso afectados por CR-001

## CU-10 Cobrar con billetera digital (nuevo)
- **Actor principal:** Cajero · **Actores secundarios:** Cliente; Billetera digital (simulada).
- **Precondición:** pedido en estado «Listo para cobro» con monto calculado.
- **Flujo principal:**
  1. El cajero selecciona el medio de pago Yape o Plin.
  2. El sistema genera la solicitud de pago por el monto del pedido.
  3. El cliente aprueba el pago en su billetera.
  4. El sistema recibe la confirmación y registra el número de operación.
  5. El sistema cambia el pedido a «Pagado» y dispara CU-08 Emitir comprobante.
- **Excepción E2 (rechazo o sin confirmación en 120 s):** el sistema permite hasta 2 reintentos; al agotarlos, anula el pedido y libera el stock reservado.
- **Trazabilidad:** RF-10 · HU-15 · CLS-07, CLS-10, CLS-11 · PR-11, PR-12.

## CU-07 Registrar cobro (modificado)
Se agrega un punto de extensión «medio = billetera» que invoca CU-10. Los medios Efectivo y Tarjeta no cambian (PR-13).

## CU-08 Emitir comprobante (modificado)
El comprobante imprime el medio de pago y el número de operación cuando existe (PR-14).
