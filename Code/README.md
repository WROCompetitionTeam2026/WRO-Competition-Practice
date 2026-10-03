# Programación / capturas de los programas

Aquí está la documentación visual de los programas de ERA. **Publicamos solamente las capturas**; los proyectos editables de SPIKE y las exportaciones de código quedan en la PC del equipo.

| Actualización | Galería |
|---|---|
| [ACTU 01 · Abril](SPIKE%20Prime/ACTU-01-April/README.md) | Versiones 01–02 |
| [ACTU 02 · Mayo](SPIKE%20Prime/ACTU-02-May/README.md) | Versiones 01–03, incluyendo el experimento relacionado con estacionamiento |
| [ACTU 03 · Agosto](SPIKE%20Prime/ACTU-03-August/README.md) | Versiones 01–04; la versión 01 incluye once capturas de Python |
| [ACTU 04 · Septiembre](SPIKE%20Prime/ACTU-04-September/README.md) | Versiones 01–08; mostramos las recientes #6, #7 y #8 juntas |

El equipo entregó 20 proyectos de origen, contando las variantes. Sus nombres y fechas de guardado están en [el inventario de versiones](../Docs/software-versions.json). Las carpetas corresponden a los grupos originales de trabajo; no representan fechas de publicación en GitHub.

## Septiembre #6

Esta versión utiliza giros activados por distancia y reinicia el yaw después de la esquina. El programa original identifica D como motor de avance, F como motor de dirección y A/C/E para distancia.

![Programa de septiembre, versión 06](SPIKE%20Prime/ACTU-04-September/Version-06/code-01.png)

## Septiembre #7

La variable `Count` coordina los giros y el avance en línea recta. Utiliza márgenes laterales de 6/7 pulgadas y ajustes propios para la dirección y la corrección de orientación.

![Programa de septiembre, versión 07](SPIKE%20Prime/ACTU-04-September/Version-07/code-01.png)

## Septiembre #8

La variable `AJJHHJ` guarda referencias para giros sucesivos de 90°. El comentario original describe objetivos de −90°, −180°, +90° y 0°.

![Programa de septiembre, versión 08](SPIKE%20Prime/ACTU-04-September/Version-08/code-01.png)

## Organización del programa

Las explicaciones se prepararon a partir de los archivos locales del equipo. Las versiones recientes contienen un evento de inicio, un evento de distancia en C y las rutinas `Steering`, `yaw` y `PAOA`. `Steering` centra la dirección y `yaw` aplica correcciones de orientación. `PAOA` aparece definida, pero no se llama desde los eventos principales de esas versiones.

El trabajo de colores, selección automática de sentido, vueltas y estacionamiento se describe en [la libreta](../Docs/Engineering-Journal.md). Las capturas recientes, por sí solas, no demuestran un recorrido completo de ambos retos. La evidencia debe corresponder a la versión usada en la pista.

## El prototipo de Python

La [actualización de agosto](SPIKE%20Prime/ACTU-03-August/README.md) contiene once capturas del prototipo Python de la versión 01. Ese programa histórico utiliza E/F para los motores, D para el sensor de color y C para distancia. Es una configuración distinta a la de los programas recientes.

## Para trabajar con el carro

Identifica la versión en las capturas y abre su proyecto **local** en la aplicación oficial de SPIKE. Las fotos sirven para consultar y documentar el programa, pero no se pueden descargar al hub como código ejecutable.

La documentación internacional de WRO también solicita el código de control. La publicación actual de capturas no sustituye ese requisito; [su estado está explicado aquí](../Docs/WRO-Documentation.md).

[Volver al inicio](../README.md)
