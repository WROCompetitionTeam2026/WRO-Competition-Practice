# Electrónica / energía y sensores

## Conexiones de referencia

![Conexiones del hub de ERA](Diagrams/hub-connections.svg)

Este diagrama se preparó a partir de las versiones recientes #6, #7 y #8. Representa los puertos utilizados por esos programas, no una medición del circuito eléctrico.

| Puerto o componente | Función en las versiones recientes |
|---|---|
| A | Sensor de distancia para revisar el espacio lateral |
| C | Sensor de distancia; evento por debajo de 20 pulgadas para el giro de esquina |
| D | Motor de avance |
| E | Sensor de distancia para revisar el espacio lateral |
| F | Motor de dirección y lectura de su posición |
| Sensor interno del hub | Medición de yaw, es decir, orientación del carro |

El comentario original de la versión #7 identifica A como el sensor izquierdo y E como el derecho. Hay que verificar esa orientación en el montaje que se vaya a usar. El programa no permite confirmar por sí solo la posición física de C. El puerto B no aparece utilizado en estas tres versiones.

## Alimentación

Las fotos muestran un hub SPIKE y componentes LEGO conectados por cable. La batería del hub alimenta el controlador y sus componentes. El material entregado no incluye mediciones de corriente, autonomía ni una tabla de consumo del montaje.

La libreta registra el reemplazo de sensores en agosto y el trabajo de refuerzo de la estructura del 1 de octubre para reducir vibraciones en las conexiones. Estas son las mejoras de confiabilidad que reportó el equipo.

## El sensor de color en las versiones anteriores

Durante abril y mayo trabajamos en la calibración y la posición del sensor de color. También documentamos las dificultades causadas por un sensor rayado. El prototipo Python de agosto utiliza D para color y C para distancia, con los motores en E/F.

Esa distribución histórica es distinta a la reciente. Las versiones #6/#7/#8 no leen el sensor de color, así que el diagrama no representa una rutina de clasificación de pilares rojos y verdes en esos programas.

## Referencias del montaje

Consulta [las fotos de arriba y abajo](../Mechanics/Vehicle%20Photos/README.md) y [los detalles de los mecanismos](../Mechanics/README.md) para revisar la posición de los cables. Para reproducir el montaje hacen falta las alturas y los ángulos de los sensores, la versión del firmware, los datos de batería y las mediciones de consumo.

[Libreta de ingeniería](../Docs/Engineering-Journal.md) · [Volver al inicio](../README.md)
