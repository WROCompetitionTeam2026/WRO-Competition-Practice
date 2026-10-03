# WRO Future Engineers / requisitos de documentación

**Referencias:** reglas internacionales de 2026, capítulo 7 y apéndice C; rúbrica de documentación; preguntas y respuestas oficiales revisadas el 3 de octubre de 2026. Para un evento en Puerto Rico, hay que seguir las instrucciones del organizador local.

## Documentos oficiales

- [Temporada WRO 2026](https://wro-association.org/competition/2026-season/)
- [Reglas de Future Engineers](https://wro-association.org/wp-content/uploads/WRO-2026-Future-Engineers-Self-Driving-Cars-General-Rules.pdf)
- [Rúbrica de documentación](https://wro-association.org/wp-content/uploads/WRO-2026-Future-Engineers-Documentation-Rubric.pdf)
- [Preguntas y respuestas oficiales](https://wro-association.org/competition/questions-answers/)
- [Plantilla oficial del repositorio](https://github.com/World-Robot-Olympiad-Association/wro2022-fe-template)

## Relación con la plantilla

| Sección de la plantilla | Ubicación en este repositorio |
|---|---|
| `src` | [Capturas de programación](../Code/README.md) |
| `schemes` | [Electrónica y diagrama](../Electronics/README.md) |
| `v-photos` | [Las seis vistas del carro](../Mechanics/Vehicle%20Photos/README.md) |
| `t-photos` | [Fotos del equipo](../General%20Photos/README.md) |
| `video` | [Videos](../video/video.md) |
| `models` | [Modelos 3D](../Mechanics/3D%20Models/README.md) |
| `other` | [Documentación](README.md) y [archivo histórico](../archive/README.md) |

Los nombres de la plantilla son una referencia para organizar el material. La organización del repositorio permite encontrar las secciones correspondientes sin duplicar las fotos.

## Estado de la documentación

| Requisito internacional | Estado actual |
|---|---|
| Repositorio público | El repositorio está publicado; debe mantener la visibilidad durante el período requerido |
| README en inglés de por lo menos 5,000 caracteres | La presentación actual está en **español**, por petición del equipo. Tiene más de 5,000 caracteres, pero no cumple el requisito internacional de idioma |
| Explicación de movilidad, energía, sensores y obstáculos | Disponible en las secciones técnicas y en la libreta |
| Código de todos los componentes programados | Se publican **capturas solamente**. Los programas editables y las exportaciones quedan locales; esta publicación no sustituye la entrega internacional del código de control |
| Fotos de las seis vistas del carro | Disponibles; confirmar que representan el montaje después de los últimos cambios |
| Foto del equipo | Hay fotos de eventos; falta confirmar una que muestre a los tres estudiantes |
| Un video de YouTube por reto con al menos 30 segundos de conducción autónoma | Los clips originales están publicados; faltan los dos enlaces correspondientes |
| Libreta y copia impresa para la final internacional | La libreta y el PDF están en español. La final internacional solicita documentación en inglés |
| Archivos de fabricación, cuando apliquen | No se recibieron modelos de este tipo; la carpeta contiene una explicación |
| Información suficiente para reproducir el montaje | Hay fotos y conexiones de referencia; faltan medidas, piezas, relación de engranajes, consumo y código publicable |

Esta tabla presenta el estado real del material disponible. La presentación en español y la publicación de capturas responden a las instrucciones del equipo; los requisitos internacionales se mantienen como referencia aparte.

## Plazos de commits y visibilidad

El capítulo 7 solicita:

1. Un primer commit por lo menos **dos meses antes de la competencia**, con al menos **una quinta parte de la cantidad final de código**.
2. Un segundo commit por lo menos **un mes antes**.
3. Un tercer commit por lo menos **dos semanas antes**. Esa versión es la referencia principal para evaluar la documentación.
4. Entregar el enlace del repositorio por lo menos **tres semanas antes**, conforme a la fecha y hora establecidas por el organizador.
5. Mantener el repositorio público desde la entrega hasta por lo menos **doce meses después de la competencia**.

El historial original contiene diez commits del 26–30 de abril de 2026. La fecha del evento y la versión entregada para evaluación no se incluyeron en el material, así que esos plazos no se presentan como verificados. Las fechas de las carpetas y de guardado de los programas son distintas a las fechas reales de publicación.

## Los cinco criterios de la rúbrica

Cada criterio se evalúa con 0, 2, 4 o 6 puntos, para un máximo de **30 puntos de documentación**.

| Criterio | Evidencia disponible |
|---|---|
| Movilidad y diseño mecánico | [Mecánica](../Mechanics/README.md), seis vistas y registros del montaje |
| Arquitectura de energía y sensores | [Electrónica](../Electronics/README.md), conexiones e historia de los sensores |
| Programación y estrategia de obstáculos | [Capturas](../Code/README.md), explicaciones y diagrama de flujo |
| Decisiones de ingeniería y funcionamiento del sistema | [Libreta](Engineering-Journal.md): prototipos, limitaciones de sensores y motivos de los cambios |
| Reproducibilidad y calidad del repositorio | README, galerías, inventarios e historial; publicación del código pendiente |

La rúbrica considera el razonamiento, las pruebas y la posibilidad de reproducir el proyecto. Los resultados publicados son los que ya registró el equipo; no se añadieron mediciones de torque, corriente, velocidad ni porcentajes de éxito.

## Detalles del carro y del programa

- Las reglas 11.3–11.5 piden cuatro ruedas, un sistema de tracción conectado y un actuador de dirección. El prototipo de tres ruedas corresponde a una etapa de pruebas.
- La regla 9.11 indica el procedimiento de espera y botón de inicio, y el uso del espacio uno en SPIKE. Los programas recientes revisados comienzan el avance en su evento de inicio.
- Las versiones #6/#7/#8 utilizan distancia y yaw. No muestran por sí solas una tarea completa de pilares rojo/derecha y verde/izquierda, tres vueltas y estacionamiento.
- Las medidas, la masa y la configuración final deben confirmarse en el carro que se use en la pista.

Las preguntas y respuestas oficiales también aclaran la medición del estacionamiento, el tamaño del carro, la orientación al estacionarse y la evaluación cuando las ruedas tienen distintos anchos. Consulta las referencias antes del evento.

[Volver al inicio](../README.md)
