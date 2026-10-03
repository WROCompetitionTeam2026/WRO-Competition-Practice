# Mecánica / el carro ERA

## Fotos del robot

[Ver las seis vistas](Vehicle%20Photos/README.md): frente, atrás, izquierda, derecha, arriba y abajo.

![ERA visto desde el lado derecho](Vehicle%20Photos/right.jpg)

## Cómo fue cambiando el montaje

El concepto inicial fue un carro compacto de cuatro ruedas, inspirado en la distribución de un Fórmula 1 y con espacio para los motores y sensores. En abril usamos un prototipo de tres ruedas para simplificar las pruebas. El conjunto de fotos posterior muestra un montaje de cuatro ruedas.

| Fecha | Trabajo registrado por el equipo |
|---|---|
| 30 de marzo–2 de abril | Rediseño compacto para las pruebas del taller |
| 8 de abril | Reposición de motores y prototipo temporal de tres ruedas para probar sensores |
| 23 de abril | Cambios en la parte frontal para mejorar el sensor de color orientado al piso |
| 29 de septiembre | Plan de reposicionar sensores, agregar un mecanismo de eje trasero y trabajar con más engranajes |
| 30 de septiembre | Refuerzo de la estructura reportado como completado |
| 1 de octubre | Nuevos ajustes para reducir vibraciones en las conexiones y mantener una trayectoria más recta |

Estos registros presentan el trabajo y las razones que anotó el equipo. No incluyen una medición de torque, relación de engranajes ni porcentaje de reducción de vibraciones.

## Detalles de los mecanismos

| Mecanismo trasero | Parte inferior |
|---|---|
| ![Detalle del mecanismo trasero](Development/rear-drive-detail.png) | ![Detalle de la parte inferior](Development/underside-detail.png) |

![Detalle de la dirección y el motor](Development/steering-and-motor-detail.png)

En `Development/` están las demás fotos originales. Las imágenes con nombres que comienzan con `IMG_20260929` documentan el carro durante los cambios de finales de septiembre. El equipo debe confirmar que las seis vistas corresponden al montaje usado después de las modificaciones del 1–2 de octubre.

## Datos para reproducir el carro

Los programas recientes utilizan D para el avance y F para la dirección. Para reproducir exactamente el montaje también hacen falta la configuración del eje, los engranajes, el centrado de la dirección, la distancia entre ejes, el ancho entre ruedas, el diámetro de las ruedas, las dimensiones, la masa y la lista de piezas.

Las reglas internacionales 11.1–11.5 solicitan un carro de cuatro ruedas, con eje de tracción y actuador de dirección, dentro de 300 × 200 × 300 mm y 1.5 kg. No permiten mover las ruedas izquierda y derecha de manera independiente como una base de tracción diferencial. El prototipo de tres ruedas corresponde a una etapa de prueba del proyecto.

## Modelos de construcción

En [Modelos 3D](3D%20Models/README.md) se indica qué archivos de diseño se recibieron. Las fotos de montaje se presentan como fotos, no como modelos CAD.

[Libreta](../Docs/Engineering-Journal.md) · [Volver al inicio](../README.md)
