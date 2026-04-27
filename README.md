# 🤖 WRO Competition Practice
Repositorio oficial de desarrollo para nuestra participación en **WRO (World Robot Olympiad)**

---

## 🚀 Proyecto del Robot

Este proyecto documenta el desarrollo de un robot **LEGO SPIKE Prime** capaz de:

- 🛣️ Seguir trayectorias
- 🎨 Detectar colores (verde, amarillo, azul)
- 🚧 Esquivar obstáculos
- 🧠 Mantener orientación con control de yaw
- ⚙️ Adaptarse dinámicamente al entorno

---

## 🧭 Arquitectura del Sistema

```mermaid
flowchart TD
    A[Inicio] --> B[Lectura de sensores]
    B --> C{¿Obstáculo?}
    C -->|Sí| D[Esquivar obstáculo]
    C -->|No| E{¿Color detectado?}
    
    E -->|Blanco| F[Corrección de límite]
    E -->|Verde/Amarillo| G[Corrección temprana]
    E -->|Azul| H[Corrección de línea]
    E -->|Ninguno| I[Movimiento continuo]

    D --> B
    F --> B
    G --> B
    H --> B
    I --> B
