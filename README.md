# Desarrollo de Aplicaciones para la Visualización de Datos (Curso 2026-2027)

## Información general

El objetivo de esta asignatura es desarrollar la capacidad de **interpretar un problema de negocio** e identificar los aspectos más relevantes a través de los datos, resumiendo los resultados mediante el **desarrollo y despliegue de aplicaciones o cuadros de mando interactivos**.

La asignatura se estructura en tres bloques:

1. **Introducción a Python** — lectura, preprocesamiento y modelado de datos.
2. **Visualizaciones interactivas** — Plotly, Dash y cuadros de mando.
3. **Despliegue** — APIs, entornos y puesta en producción (Render, AWS serverless).

Al finalizar, el alumnado podrá crear **cuadros de mando y aplicaciones** que faciliten la visualización, el análisis y el consumo continuo de datos.

## Estructura del repositorio

| Carpeta | Contenido |
| --- | --- |
| `1_Introduccion_Python/` | Notebooks, ejercicios y soluciones del Tema 1 |
| `2_app_visualizaciones/` | Plotly, Dash, callbacks y `requirements.txt` |
| `3_despliegue_apps/` | Entornos/Git, Render, API Flask y Serverless en AWS |
| `Intertrimestral/` | Material de la prueba intertrimestral del curso actual |
| `0_Intertrimestral_23/` … `0_Intertrimestral_25/` | Exámenes intertrimestrales de cursos anteriores |
| `0_examen_final_23/` … `0_examen_final_25/` | Exámenes finales de cursos anteriores |
| `0_DAVD_Introduccion.pdf` | Presentación de introducción a la asignatura |

## Contenidos

### Tema 1: Introducción a Python
- Instalación y configuración de entornos (venv, Anaconda, Colab).
- Variables, estructuras de control, funciones y clases.
- Lectura y manipulación de datos (pandas).
- Introducción a modelos con scikit-learn.
- Visualizaciones básicas (matplotlib / plotly).

### Tema 2: Visualización interactiva
- Gráficos interactivos con **Plotly**.
- **HTML** y **CSS** aplicados a **Dash**.
- Callbacks y componentes interactivos.
- Cuadros de mando completos.
- Automatización en la adquisición y presentación de datos.

### Tema 3: Despliegue de aplicaciones
- Entornos virtuales, dependencias y control de versiones (Git/GitHub).
- Entornos de desarrollo, testing y producción.
- CI/CD y ciclo de vida de un modelo.
- APIs REST para servir modelos.
- Despliegue de aplicaciones Dash (Render).
- Introducción a despliegue serverless en AWS.

## Evaluación

| Elemento | Fecha | Peso |
| --- | --- | --- |
| Propuesta / redacción del proyecto | **1 de octubre de 2026** | 10 % |
| Prueba intertrimestral | **15 de octubre de 2026** | 10 % |
| Desarrollo de aplicación y presentación | Continua + **26 de noviembre y 3 de diciembre de 2026** | 50 % |
| Examen teórico-práctico | **Diciembre de 2026** | 30 % |

### Desglose del proyecto de aplicación (50 %)

1. Propuesta de idea y URL del repositorio en GitHub — incluida en el 10 % de redacción.
2. Desarrollo y actualizaciones periódicas en el repositorio — **20 %** (actividad en GitHub).
3. Presentación de la aplicación — **20 %** (calidad de la exposición).
4. Calidad y estructura del código — **20 %**.
5. Aplicación desplegada en una URL accesible — **40 %** (diseño, interacción e innovación).

Se valorará la **mejora continua** del proyecto a lo largo del semestre.

La exposición durará **5 minutos**, más **2 minutos** de preguntas.

**Requisito indispensable:** aprobar todas las partes de la evaluación y asistir al menos al **85 %** de las sesiones.

### Entrega de la propuesta (1 de octubre de 2026)

Documento PDF de **dos páginas** con:

- **Motivación** — relevancia del problema, necesidad cubierta y aportación frente a soluciones existentes.
- **Visión estratégica** — alcance, usuarios, beneficios y escenarios de uso.
- **Repositorio en GitHub** — nombre adecuado y `README.md` con título, descripción, objetivos y plan de trabajo inicial.

## Entorno de trabajo y recursos

- El código del proyecto deberá estar en **Python** y versionado en **GitHub**.
- Cada estudiante tendrá acceso de escritura únicamente a su propio proyecto en el repositorio oficial de la asignatura.

### Entornos recomendados
- [Google Colab](https://colab.research.google.com/)
- [Anaconda](https://www.anaconda.com/download)
- [venv (librería estándar)](https://docs.python.org/3/library/venv.html)

### Recursos de apoyo
- [The Hitchhiker’s Guide to Python](https://docs.python-guide.org/)
- [Dash documentation](https://dash.plotly.com/)
- [Plotly Python](https://plotly.com/python/)
- [Scikit-learn](https://scikit-learn.org/stable/)
- [Flask](https://flask.palletsprojects.com/)
