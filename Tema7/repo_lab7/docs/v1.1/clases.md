# Modelo de clases — cambios v1.1

| ID | Clase | Cambio |
|---|---|---|
| CLS-07 | Pago | Agrega `medioPago: MedioPago` (Efectivo, Tarjeta, Yape, Plin) y `numeroOperacion: String` |
| CLS-08 | Comprobante | Muestra `medioPago` y `numeroOperacion` |
| CLS-10 | PasarelaBilletera (interfaz) | `solicitarPago(monto): Operacion`, `consultarEstado(id): EstadoOperacion` |
| CLS-11 | SimuladorBilletera | Implementa `PasarelaBilletera` para pruebas; simula aprobado, rechazado y sin respuesta |
