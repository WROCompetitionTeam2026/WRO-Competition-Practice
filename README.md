# 🤖 WRO Competition Practice

Repositorio oficial de desarrollo para nuestra participación en **WRO (World Robot Olympiad)**

---

## 🚀 Proyecto del Robot

Este proyecto documenta el desarrollo de un robot **LEGO SPIKE Prime** capaz de:

* 🛣️ Seguir trayectorias
* 🎨 Detectar colores (verde, amarillo, azul)
* 🚧 Esquivar obstáculos
* 🧠 Mantener orientación con control de yaw
* ⚙️ Adaptarse dinámicamente al entorno

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
```

---

## 🗓️ Fases del Proyecto

### ◉ FASE 01 — INFORMATIVA

📅 **26 Marzo 2026**

* Entrega del robot
* Introducción a reglas y competencia

📅 **27–28 Marzo 2026**

* Estudio de LEGO SPIKE Prime
* Programación y sensores

📅 **30 Marzo – 2 Abril 2026**

* Rediseño completo del robot
* Optimización estructural

---

### ◈ FASE 02 — TEÓRICA

📅 **6–7 Abril 2026**

* Desarrollo del código de movimiento
* Pruebas iniciales

📅 **8 Abril 2026**

* Cambio a diseño tipo triciclo
* Mejor integración de sensores

📅 **9–10 Abril 2026**

* Adaptación del código
* Implementación de navegación

---

### ◆ FASE 03 — PRUEBAS Y AJUSTES

📅 **13–14 Abril 2026**

* Finalización de sensores
* Navegación funcional

📅 **15 Abril 2026**

* Ajustes de velocidad
* Mejora en detección de obstáculos

📅 **16 Abril 2026**

* Código final completo

---

## 📂 Código

El código se encuentra en la carpeta:

```bash
/Codigo
```

Incluye:

* Control de motores
* Sensores (color + distancia)
* Lógica de navegación
* Corrección automática
* Sistema de evasión

---

## 🧪 Lógica de Esquiva

```mermaid
flowchart TD
    A[Detecta obstáculo] --> B[Retrocede]
    B --> C[Giro en arco]
    C --> D[Avanza]
    D --> E{¿Camino libre?}
    E -->|Sí| F[Continúa]
    E -->|No| C
```

---

## 📊 Estado del Proyecto

```
EN DESARROLLO ●

✓ ESTRUCTURA  
✓ CÓDIGO  
✓ SENSORES  
→ COMPETENCIA
```

---

## 🛠️ Actualizaciones Recientes

📅 **23 Abril 2026**

* 🔧 Mejora del sensor de color
* 🔄 Ajuste de rotación en detección de líneas
* 🧱 Rediseño frontal del robot
* 💻 Optimización del código (mayor estabilidad)

---

## 👨‍💻 Equipo

**WRO Future Engineers Team**
