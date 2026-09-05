# Ejercicio: Git y Dash

## 1. Clonar o actualizar el repositorio

```bash
git clone git@github.com:dmartincc/davd-26-27.git
# Si ya lo tenías clonado:
cd davd-26-27 && git pull
```

## 2. Ir a la carpeta de Dash

```bash
cd 2_app_visualizaciones/
```

## 3. Crear el entorno virtual e instalar dependencias

Con `venv` (recomendado):

```bash
python3 -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install --upgrade pip
pip install -r requirements.txt
```

Alternativa con `virtualenvwrapper`:

```bash
pip install virtualenvwrapper
export WORKON_HOME=~/Envs
mkdir -p $WORKON_HOME
source $(which virtualenvwrapper.sh)   # o la ruta de tu instalación
mkvirtualenv dash
pip install -r requirements.txt
```

## 4. Arrancar la introducción a Dash

```bash
python 2_Introduccion_a_Dash.py
```

Abre en el navegador: http://127.0.0.1:8050/

Revisa el código y fíjate en cómo se combinan componentes HTML/CSS con gráficos Plotly.

## 5. Arrancar el dashboard con callbacks

```bash
python 3_Callbacks_componentes_core.py
```

Explora los dropdowns, el checklist y cómo los callbacks actualizan las figuras.

> Guía ampliada de entornos y Git: [`../3_despliegue_apps/0_entornos_y_git/`](../3_despliegue_apps/0_entornos_y_git/).
