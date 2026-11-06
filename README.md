# Evidencia 1 — Apártalo: tu primer sprint de verdad
## Variante 2: Clínica Veterinaria Huellitas

### Descripción del Proyecto
Sistema de gestión de citas y reglas de negocio automatizadas para la clínica **Veterinaria Huellitas**, desarrollado bajo la metodología ágil Scrum.

---

### Bitácora de Roles Scrum (Una sola persona)
Para este sprint, se asumieron y ejecutaron formalmente los siguientes roles y responsabilidades:

1. **Product Owner (PO):**
   - Definición, análisis y priorización del Product Backlog.
   - Creación de las Historias de Usuario (`HU01`, `HU02`, `HU03`) con sus respectivos criterios de aceptación detallados en los Issues de GitHub.
   - Elaboración de reglas de negocio para tarifas de consulta, recargos por peso, descuentos por múltiples mascotas y políticas de cancelación.

2. **Scrum Master (SM):**
   - Configuración inicial del marco de trabajo en GitHub (creación del repositorio a partir de la plantilla y configuración del tablero Kanban "Sprint 1 - Veterinaria Huellitas").
   - Monitoreo del flujo de avance en las columnas del tablero (`Backlog`, `To Do`, `In Progress`, `Done`).
   - Eliminación de impedimentos técnicos y facilitación de la ceremonia del sprint.

3. **Desarrollador (Dev):**
   - Implementación de la lógica de negocio en Python dentro del archivo `src/apartalo/reglas.py` (`R1` y `R2`).
   - Desarrollo de pruebas unitarias robustas utilizando `pytest` en la carpeta de pruebas para garantizar el cumplimiento de los criterios de aceptación.
   - Gestión de control de versiones y commits descriptivos etiquetados por rol.

---

### Planificación y Capacidad del Sprint
- **Velocidad de referencia estimada:** 22 puntos de historia.
- **Historias seleccionadas para el Sprint 1:**
  - `HU01`: Cálculo del total de la cita con recargos y descuentos (R1).
  - `HU02`: Aplicación de cargos por cancelación tardía o inasistencia (R2).
- **Backlog (Siguiente Sprint):**
  - `HU03`: Control de cupo máximo de citas por hora (R3).

---

### Ejecución de Pruebas Unitarias
Las pruebas unitarias implementadas se ejecutan y validan localmente mediante el comando:
```bash
pytest
