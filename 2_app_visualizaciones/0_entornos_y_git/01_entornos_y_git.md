# Entornos virtuales Python y control de versiones (Git/GitHub) — DAVD 2026-2027

| Recurso | Fichero |
| --- | --- |
| Ejercicio / checklist | [`ejercicios/E0_entornos_git.md`](ejercicios/E0_entornos_git.md) |
| Chequeo de entorno | [`ejemplos/check_entorno.py`](ejemplos/check_entorno.py) |
| Plantilla `.gitignore` | [`ejemplos/gitignore_davd.txt`](ejemplos/gitignore_davd.txt) |
| Requisitos Dash (Tema 2) | [`../../2_app_visualizaciones/requirements.txt`](../../2_app_visualizaciones/requirements.txt) |

Este documento es la **referencia amplia** para montar un entorno reproducible y versionar el código del curso **Desarrollo de Aplicaciones para la Visualización de Datos (DAVD)**. Encaja en el **Tema 3 (despliegue)**, pero conviene dominarlo desde el principio: sin `venv` + Git no hay app Dash desplegable de forma seria.

**Repo del curso:** https://github.com/dmartincc/davd-26-27

---
## 0. Objetivos de aprendizaje

Al terminar esta sesión (y este documento) deberías ser capaz de:

1. Explicar por qué una **app Dash / API** de DAVD necesita **reproducibilidad**.
2. Crear, activar, verificar y recrear un entorno con **`venv` + pip**.
3. Distinguir Python global, entorno virtual e intérprete del IDE.
4. Instalar dependencias desde `2_app_visualizaciones/requirements.txt` (Dash, Plotly, pandas…).
5. Explicar el modelo mental de Git: *working tree → staging → commit → remoto*.
6. Usar el flujo diario: rama → cambios → `add` → `commit` → `push` → **Pull Request**.
7. Configurar un `.gitignore` correcto (imprescindible antes de desplegar en Render).
8. Diagnosticar los errores más comunes de venv y de Git/GitHub.

---

## 1. Por qué esta sesión importa en DAVD

### 1.1 Qué entregamos en la asignatura

En DAVD no entregamos “un dashboard que me funciona en el portátil”. Entregamos **aplicaciones o cuadros de mando** que otra persona (compañero, profesor, Render, revisores) debe poder:

1. **clonar** desde GitHub,
2. **instalar** dependencias (`requirements.txt`),
3. **ejecutar** en local (Dash / Flask) y **desplegar**,
4. **revisar** el historial de desarrollo en el repositorio.

Esa cadena se rompe si:

- las librerías están mezcladas con el Python del sistema,
- no hay historial (zips por correo, carpetas `final_v3_definitivo`),
- hay claves API dentro del código,
- el README no explica cómo arrancar.

### 1.2 Mapa mental del semestre

```text
Tema 1  →  Python / pandas / modelos
Tema 2  →  Plotly + Dash (necesitas venv + Git desde el día 1)
Tema 3  →  Despliegue (Render, APIs, AWS) ← este material vive aquí
```

Sin entorno virtual y sin GitHub, **no puedes completar** el proyecto de aplicación ni el despliegue en Render.

### 1.3 Diagrama de reproducibilidad

```text
Máquina del alumno                 Remoto (GitHub)              Otra máquina
──────────────────                 ───────────────              ────────────
código fuente          ───────►    código fuente       ───────► clone
.venv/ (local, NO git)             (sin .venv)                  python -m venv .venv
.env   (local, NO git)             .env.example                 pip install -r …
app Dash / README                     app Dash / README               python app.py / despliegue
```

**Regla de oro:** lo que necesita secreto o es regenerable (`.venv`) no viaja en Git. Lo que define el proyecto (código, tests, README, `requirements.txt`, `.env.example`) sí.

### 1.4 Analogías útiles

| Concepto | Analogía |
| --- | --- |
| `venv` | Caja de herramientas **por obra**; no mezcles destornilladores de dos obras |
| `requirements.txt` | Lista de la compra para montar la caja en otro sitio |
| Commit | Foto del proyecto con una etiqueta (“qué cambió”) |
| Rama | Cuaderno borrador paralelo a la versión estable |
| Pull Request | “¿Puedes revisar esto antes de integrarlo en la versión oficial?” |
| `.gitignore` | Lista de cosas que la cámara de fotos debe ignorar |

---

## 2. Python en tu máquina: qué hay realmente

Antes del venv conviene entender **qué Python** estás usando.

### 2.1 Varias instalaciones posibles

En un mismo ordenador pueden coexistir:

- Python del sistema (macOS/Linux),
- Python de [python.org](https://www.python.org/downloads/),
- Python de la Microsoft Store (Windows),
- Python de Homebrew / pyenv,
- un entorno conda.

Por eso `python`, `python3` y el intérprete del IDE **a veces no son el mismo**.

Comprueba:

```bash
python3 --version
which python3                 # macOS/Linux
where python                  # Windows

python3 -c "import sys; print(sys.executable); print(sys.version)"
```

En DAVD recomendamos **Python 3.11+** (idealmente 3.12).

### 2.2 `pip` va ligado al intérprete

`pip` no es universal: instala paquetes **en el Python que lo invoca**.

Forma segura (siempre):

```bash
python -m pip install paquete
```

Así evitas el clásico: “instalé con `pip` pero `python` no lo ve”.

### 2.3 Qué es `site-packages`

Los paquetes de terceros (`pandas`, `dash`, `plotly`, …) viven en un directorio llamado `site-packages` asociado a un intérprete concreto. Un venv tiene **su propio** `site-packages`.

```bash
python -c "import site; print(site.getsitepackages())"
```

---

## 3. Entornos virtuales con `venv` (teoría amplia)

### 3.1 Definición

Un **entorno virtual** es un directorio (habitualmente `.venv/`) que contiene:

- un intérprete Python “enlazado” al proyecto,
- su propio `pip`,
- su propio `site-packages`,
- scripts de activación.

Cuando lo **activas**, tu shell prioriza ese `python` y ese `pip`.

### 3.2 ¿Qué problema resuelve?

| Sin venv | Con venv |
| --- | --- |
| Proyecto A necesita `pandas 2.0` y B necesita `2.2` → conflicto | Cada proyecto tiene el suyo |
| “En clase funciona, en casa no” | Mismas dependencias vía `requirements.txt` |
| Un upgrade rompe otro trabajo | El daño queda aislado |
| Difícil de desplegar | El PaaS instala desde requirements |

### 3.3 Anatomía de `.venv/`

```text
.venv/
├── pyvenv.cfg                 # metadatos (qué Python base se usó)
├── bin/                       # macOS/Linux: python, pip, activate
│   ├── activate
│   ├── python
│   └── pip
├── Scripts/                   # Windows: python.exe, pip.exe, activate
└── lib/python3.x/site-packages/
    ├── pandas/
    ├── dash/
    ├── plotly/
    └── ...
```

**Importante:** `.venv/` se **regenera**. No se sube a GitHub. Ocupa cientos de MB; versionarlo es un error grave.

### 3.4 Ciclo de vida completo

```text
crear  →  activar  →  instalar  →  trabajar  →  (opcional) freeze
                                      │
                                      ├─ deactivate (salir del shell)
                                      └─ borrar .venv y recrear si se corrompe
```

### 3.5 Crear, activar e instalar (macOS / Linux)

```bash
cd davd-26-27                    # repo del curso, o tu repo personal
python3 --version                # 3.11+ recomendado
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
pip install -r 2_app_visualizaciones/requirements.txt
```

Tras activar, el prompt suele mostrar `(.venv)`.

### 3.6 Windows (PowerShell y cmd)

```bat
cd davd-26-27
python -m venv .venv
.venv\Scripts\activate
python -m pip install --upgrade pip
pip install -r 2_app_visualizaciones/requirements.txt
```

Si PowerShell bloquea scripts:

```powershell
Set-ExecutionPolicy -Scope CurrentUser RemoteSigned
```

Luego cierra y abre la terminal, y vuelve a activar.

En **cmd.exe**:

```bat
.venv\Scripts\activate.bat
```

### 3.7 Cómo verificar que estás dentro del venv

```bash
# Debe contener ".venv" en la ruta
which python          # macOS/Linux
where python          # Windows
echo $VIRTUAL_ENV     # macOS/Linux/Git Bash
echo %VIRTUAL_ENV%    # cmd Windows

python -c "import sys; print(sys.executable)"
python -c "import sys; print(sys.prefix)"
```

Comprobación del curso:

```bash
python 2_app_visualizaciones/0_entornos_y_git/ejemplos/check_entorno.py --strict
```

Debe imprimir `ENTORNO OK`. Sin `--strict` solo avisa si no detecta `.venv`.

### 3.8 Desactivar, recrear y limpiar

```bash
deactivate                 # sales del entorno; no borra ficheros
rm -rf .venv               # macOS/Linux: borra el entorno
rmdir /s /q .venv          # Windows cmd (equivalente aproximado)
```

Luego vuelve a crear e instalar. Recrear el venv es la solución a muchos “estados raros”.

### 3.9 Instalar paquetes adicionales

Durante el curso a veces necesitarás SDKs opcionales:

```bash
pip install openai anthropic huggingface_hub
```

Si el paquete forma parte estable de **tu** proyecto, añádelo a tu `requirements.txt` personal.

```bash
pip show pandas
pip list
pip list --outdated
```

### 3.10 `requirements.txt` en profundidad

#### Estilo A — rangos mínimos (repo del curso)

```text
dash>=2.17
plotly>=5.18
pandas>=2.0
gunicorn>=22.0
```

Ventajas: legible, flexible, fácil de mantener en docencia.  
Inconveniente: dos alumnos pueden resolver versiones ligeramente distintas.

#### Estilo B — pin exacto

```text
pandas==2.2.3
dash==2.17.0
```

Ventajas: máxima reproducibilidad.  
Inconveniente: más fricción al actualizar.

#### Estilo C — lock generado

```bash
pip freeze > requirements-lock.txt
```

Útil para reproducir un bug (“en mi máquina pasaba X”).  
Ojo: `freeze` incluye dependencias transitivas y puede ser ruidoso.

**Recomendación DAVD:**

- Curso / demos Dash: estilo A (`2_app_visualizaciones/requirements.txt`).
- proyecto de aplicación en producción: pinnea o usa lock si despliegas.

### 3.11 Crear un `requirements.txt` desde cero (tu proyecto)

```bash
# con el venv activo y los paquetes ya instalados
pip freeze > requirements.txt     # rápido
# o mejor: mantén a mano solo las dependencias directas
```

Buenas prácticas:

- Lista **dependencias directas** que tu código importa.
- No copies secretos ni rutas locales.
- Documenta en el README la versión de Python (`3.12`).

### 3.12 Configurar el IDE (Cursor / VS Code)

Aunque la terminal use `.venv`, el IDE puede usar otro intérprete.

En Cursor/VS Code:

1. `Cmd/Ctrl + Shift + P`
2. **Python: Select Interpreter**
3. Elige `.venv/bin/python` (o `.venv\Scripts\python.exe`)

Comprueba en la barra de estado que aparece el venv correcto.  
Si el IDE no ve `pandas` pero la terminal sí: **99 % es intérprete mal seleccionado**.

### 3.13 venv vs virtualenv vs conda vs poetry (mapa)

| Herramienta | Qué es | En DAVD |
| --- | --- | --- |
| `venv` | Módulo estándar de Python | **Obligatorio conocer / preferido** |
| `virtualenv` | Herramienta clásica externa | Compatible, no necesaria |
| conda / Anaconda | Gestor de envs + paquetes binarios | Permitido en casa; demos asumen venv |
| poetry / uv / pdm | Gestores modernos de proyectos | Interesantes; fuera del núcleo del curso |

Puedes usar conda personalmente, pero debes entender el flujo **venv + requirements.txt** porque aparece en despliegue y en la evaluación de reproducibilidad.

### 3.14 Variables de entorno y `.env`

Más adelante usaremos claves (`OPENAI_API_KEY`, etc.).

Patrón correcto:

```text
.env            → secretos reales (NO git)
.env.example    → nombres de variables vacíos (SÍ git)
python-dotenv   → carga .env en local
```

Ejemplo `.env.example`:

```text
OPENAI_API_KEY=
ANTHROPIC_API_KEY=
HF_TOKEN=
LOG_LEVEL=INFO
```

Nunca hagas:

```python
API_KEY = "sk-...."   # MAL: secreto en código
```

### 3.15 Anti-patrones de entornos (memorízalos)

1. `sudo pip install …` en el sistema.
2. Subir `.venv/` a GitHub “para facilitar la vida”.
3. Tener tres Pythons y no saber cuál usa el IDE.
4. Mezclar conda base + pip global + venv sin criterio.
5. Instalar paquetes **sin** activar el entorno y luego no entender por qué “no están”.
6. Borrar `requirements.txt` porque “ya lo tengo instalado yo”.

### 3.16 Problemas frecuentes de venv (tabla amplia)

| Síntoma | Causa probable | Qué hacer |
| --- | --- | --- |
| `python3: command not found` | Python no instalado / PATH | Instala 3.12+ y reabre la terminal |
| `pip install` ok pero `import` falla en IDE | IDE con otro intérprete | *Python: Select Interpreter* → `.venv` |
| Paquetes se instalan “fuera” | venv no activado | `source .venv/bin/activate` y repite |
| `ensurepip is not available` | Python incompleto (algunos Linux) | Instala `python3-venv` / reinstala Python |
| Conflictos de versiones imposibles | entorno corrupto o mezcla conda/pip | Borra `.venv` y recrea |
| PowerShell no ejecuta `activate` | ExecutionPolicy | `RemoteSigned` para CurrentUser |
| `permission denied` al crear `.venv` | carpeta protegida / OneDrive raro | Trabaja en una ruta local sencilla |
| `SSL: CERTIFICATE_VERIFY_FAILED` | certificados / proxy | Actualiza certifi; revisa red corporativa |
| Muy lento al instalar | red / índice | Reintenta; evita VPNs inestables |

### 3.17 Mini laboratorio guiado (venv)

Hazlo ahora mismo:

```bash
cd davd-26-27
python3 -m venv .venv
source .venv/bin/activate          # Windows: .venv\Scripts\activate
python -m pip install --upgrade pip
pip install -r 2_app_visualizaciones/requirements.txt
python -c "import sys; print(sys.executable)"
python 3_despliegue_apps/0_entornos_y_git/ejemplos/check_entorno.py --strict
deactivate
python 3_despliegue_apps/0_entornos_y_git/ejemplos/check_entorno.py
# observa el AVISO si no estás en .venv
source .venv/bin/activate
python 3_despliegue_apps/0_entornos_y_git/ejemplos/check_entorno.py --strict
```

Preguntas de autoevaluación:

1. ¿Qué cambia en `sys.executable` al activar?
2. ¿Por qué `--strict` falla fuera del venv?
3. ¿Qué fichero del repo lista las dependencias?

---

## 4. Git: teoría del control de versiones

### 4.1 ¿Qué es Git?

Git es un sistema de control de versiones **distribuido**:

- cada clon tiene el historial completo (`.git/`),
- puedes trabajar offline y sincronizar después,
- las ramas son baratas y naturales.

GitHub es una **plataforma** sobre Git (hosting, PR, issues, Actions). Git ≠ GitHub.

### 4.2 ¿Qué problema resuelve?

| Sin Git | Con Git |
| --- | --- |
| `proyecto_final_v7.zip` | Historial navegable |
| “¿Quién rompió esto?” | `git log` / `git blame` |
| Miedo a experimentar | Ramas descartables |
| Colaborar por WhatsApp | Pull Requests |
| Perder trabajo | Commits recuperables |

### 4.3 Modelo mental: tres zonas + remoto

```text
 ┌────────────────┐    git add     ┌──────────────┐   git commit   ┌─────────────┐
 │  working tree  │ ─────────────► │   staging    │ ─────────────► │  commits    │
 │ (archivos)     │                │  (index)     │                │  locales    │
 └────────────────┘                └──────────────┘                └──────┬──────┘
                                                                          │
                                                                     git push
                                                                          ▼
                                                                   ┌─────────────┐
                                                                   │   remoto    │
                                                                   │  (origin)   │
                                                                   └─────────────┘
```

| Zona | Contenido |
| --- | --- |
| Working tree | Lo que ves en el disco y editas |
| Staging (`index`) | Lo que **entrará** en el próximo commit |
| Commits locales | Historial en `.git/` |
| Remoto (`origin`) | Copia en GitHub |

Comandos de inspección:

```bash
git status          # mapa de las tres zonas
git diff            # working tree vs staging/HEAD
git diff --cached   # staging vs HEAD
git log --oneline --graph --decorate -10
```

### 4.4 Glosario operativo (para examen y práctica)

| Término | Definición en una frase |
| --- | --- |
| Repositorio | Proyecto con historial (carpeta + `.git/`) |
| Commit | Instantánea del proyecto + mensaje + autor + fecha |
| Hash (SHA) | Identificador del commit |
| Branch | Puntero móvil a una línea de commits |
| `main` | Rama principal de integración |
| `HEAD` | “Dónde estoy ahora” |
| Tag | Etiqueta fija (p. ej. `v0.9.0-rc1`) |
| Remote | Servidor Git (normalmente GitHub) |
| `origin` | Nombre por defecto del remoto principal |
| Clone | Copiar un repo remoto a local |
| Fetch | Traer commits remotos **sin** fusionar |
| Pull | Fetch + integrar en tu rama actual |
| Push | Publicar commits locales al remoto |
| Merge | Combinar historias |
| Rebase | Reescribir/reaplicar commits sobre otra base |
| Conflict | Dos cambios incompatibles en las mismas líneas |
| PR / MR | Propuesta de integración con revisión |
| Fork | Copia del repo bajo otra cuenta |
| `.gitignore` | Patrones de ficheros que Git no debe trackear |
| Staging | Selección explícita de qué va al commit |

### 4.5 Snapshots, no “diffs mágicos” solamente

Conceptualemente, Git guarda **instantáneas** del árbol de ficheros. Los diffs son una forma de *ver* diferencias entre instantáneas. Por eso revertir o comparar ramas es potente.

### 4.6 Commits atómicos y mensajes

Un buen commit:

- tiene **un propósito** claro,
- deja el proyecto en un estado coherente (idealmente),
- tiene un mensaje **imperativo** y concreto.

| Bien | Mal |
| --- | --- |
| `Add session 01 notes` | `update` |
| `Fix README install steps` | `cambios` |
| `Ignore venv and env files` | `asdf` |
| `Add sales validator tests` | `WIP!!!!!!!!!!` |

Plantilla mental:

```text
Add X
Fix Y
Update Z
Remove W
```

Mensajes multilínea (cuando hace falta):

```bash
git commit -m "$(cat <<'EOF'
Add environment checklist to README.

Document venv activation for macOS and Windows.
EOF
)"
```

### 4.7 Ramas: para qué sirven en DAVD

Flujo del curso:

```text
main  ──►  practica/sesion-01  ──►  commits  ──►  PR  ──►  main
main  ──►  feature/validador-ventas ──► ...
main  ──►  fix/readme-windows
```

Nombres recomendados:

- `practica/sesion-01`
- `feature/…`
- `fix/…`
- `docs/…`

Evita trabajar días enteros solo en `main` con commits “basura”: dificulta revisión y rollback.

Comandos:

```bash
git branch                     # lista local
git branch -vv                 # tracking
git switch -c practica/sesion-01
# equivalente antiguo:
git checkout -b practica/sesion-01
git switch main
git branch -d practica/sesion-01   # borrar rama ya fusionada
```

### 4.8 Remotos y autenticación

Ver remotos:

```bash
git remote -v
```

Dos URLs habituales:

```text
HTTPS: https://github.com/USUARIO/REPO.git
SSH:   git@github.com:USUARIO/REPO.git
```

#### HTTPS

- Más simple al inicio.
- GitHub pedirá autenticación (credential helper / token).

#### SSH

```bash
ssh-keygen -t ed25519 -C "tu@email.es"
# añade la clave pública en GitHub → Settings → SSH keys
ssh -T git@github.com
```

Si ves `Hi USERNAME! You've successfully authenticated…`, está bien.

### 4.9 Configuración inicial (una vez por máquina)

```bash
git config --global user.name "Tu Nombre"
git config --global user.email "tu@email.es"
git config --global init.defaultBranch main

# útiles
git config --global color.ui auto
git config --global pull.rebase false     # o true si sabes lo que implica
git config --global core.editor "nano"    # o code --wait, vim, etc.
```

Ver configuración:

```bash
git config --list --show-origin | head
```

Si tu email de GitHub es privado, usa el noreply que te da GitHub.

### 4.10 Crear el repositorio personal del curso

1. En GitHub: **New repository**.
2. Nombre: `davd-26-27-apellido-nombre`.
3. Visibility: según indiquen; en máster a menudo privado.
4. Puedes crear con README vacío o sin README (y crearlo en local).
5. **No** marques “Add .venv” (no existe tal opción, pero mentalmente: no lo subas).

Clonar:

```bash
git clone git@github.com:TU_USUARIO/davd-26-27-apellido-nombre.git
cd davd-26-27-apellido-nombre
```

Si el repo del **curso** es distinto del **personal**:

- curso (`dmartincc/davd-26-27`): materiales,
- personal: tus proyectos y entregas.

### 4.11 Flujo diario recomendado (de pe a pa)

```bash
git status
git switch -c practica/sesion-01

# editar ficheros…
git status
git diff

git add README.md sesion01.md .gitignore
git status
git commit -m "Add session 01 notes and environment checklist"

git push -u origin practica/sesion-01
```

En GitHub:

1. *Compare & pull request*
2. Base: `main` ← compare: `practica/sesion-01`
3. Título + descripción clara
4. Create PR → revisión → Merge

Después del merge (local):

```bash
git switch main
git pull origin main
git branch -d practica/sesion-01
```

### 4.12 `git add` con intención

Evita `git add .` al principio (fácil colar `.venv`, datos grandes, secretos).

Mejor:

```bash
git add fichero1 fichero2
git add -p          # staging por hunks (avanzado, muy útil)
```

Si añadiste de más **antes** del commit:

```bash
git restore --staged fichero_no_deseado
```

### 4.13 `.gitignore` en profundidad

Plantilla del curso: [`ejemplos/gitignore_davd.txt`](ejemplos/gitignore_davd.txt)

```gitignore
# Entornos
.venv/
venv/
env/
Envs/

# Secretos
.env
.env.*
!.env.example

# Python
__pycache__/
*.py[cod]
.pytest_cache/
.mypy_cache/
.ruff_cache/
.ipynb_checkpoints/
*.egg-info/
.coverage
htmlcov/
dist/
build/

# OS / IDE
.DS_Store
.idea/
.vscode/
```

Si ya trackeaste algo por error:

```bash
git rm -r --cached .venv
git rm --cached .env
git commit -m "Stop tracking local environment and secrets"
```

`git rm --cached` quita del índice **sin** borrar el fichero local.

### 4.14 Qué NUNCA debe subir a GitHub

1. `.venv/` / `venv/`  
2. `.env` y cualquier API key / token / password  
3. Credenciales cloud, ficheros `*.pem`, capturas con secretos  
4. Datos personales o confidenciales sin permiso  
5. Artefactos enormes innecesarios (modelos GB, datasets enormes) — usa LFS o almacenamiento externo si aplica  

#### Si filtraste un secreto

1. **Rota/revoca** la clave en el proveedor (lo más urgente).  
2. Elimina el secreto del código.  
3. Limpia historial solo si sabes lo que haces (`git filter-repo` / soporte GitHub); no basta un commit nuevo.  
4. Avisa si el repo es compartido.

### 4.15 Leer historial y entender el pasado

```bash
git log --oneline -10
git log --oneline --graph --decorate --all -20
git show HEAD
git show abc1234
git blame README.md
git stash                 # aparcar cambios locales temporalmente
git stash pop
```

### 4.16 Deshacer cosas (con cuidado)

> No memorices solo comandos: entiende **si el commit ya se empujó**.

| Quiero… | Comando habitual | Riesgo |
| --- | --- | --- |
| Descartar cambios de un fichero no commiteado | `git restore fichero` | Pierdes ediciones locales |
| Sacar del staging | `git restore --staged fichero` | Bajo |
| Corregir el último commit local (aún no push) | `git commit --amend` | Medio (no uses si ya hay push compartido) |
| Crear un commit que deshace otro | `git revert HASH` | Bajo/seguro en equipos |
| Mover HEAD atrás (avanzado) | `git reset` | Alto si ya hay push |

En DAVD, preferimos **commits nuevos** y `revert` frente a reescribir historia pública.

### 4.17 Merge, rebase y conflictos (introducción)

Cuando `main` avanzó y tu rama también:

```bash
git switch practica/sesion-01
git fetch origin
git merge origin/main
# o, si tu equipo/profesor lo indica:
# git rebase origin/main
```

Si hay conflicto:

1. Git marca ficheros `UU` / “both modified”.
2. Abres el fichero, buscas `<<<<<<<`, eliges el contenido final, borras marcadores.
3. `git add fichero_resuelto`
4. `git commit` (si era merge) o `git rebase --continue`

Herramientas visuales del IDE ayudan mucho.

### 4.18 Pull Requests: qué debe contener una buena PR

- Título claro.
- Qué problema resuelve.
- Cómo probarlo (comandos).
- Capturas solo si aportan.
- En DAVD sesión 1: formulario de repaso teórico (venv/git).

Ejemplo de descripción:

```markdown
## Resumen
Añade notas de la sesión 1 y gitignore del curso.

## Cómo probar
- Crear venv e instalar requirements
- python 3_despliegue_apps/0_entornos_y_git/ejemplos/check_entorno.py --strict

## Checklist
- [ ] No incluye .venv ni .env
- [ ] README con pasos de instalación
```

### 4.19 GitHub más allá del código

| Función | Uso en DAVD |
| --- | --- |
| Issues | Ideas, bugs, tareas del proyecto |
| Projects / boards | Opcional para proyecto de aplicación |
| Actions (CI) | Tests / checks en cada push (opcional en el proyecto) |
| Releases / tags | versión desplegada de la app |
| Branch protection | Evitar push directo a `main` (avanzado) |

### 4.20 Relación Git ↔ evaluación

| Entregable | Qué se mira |
| --- | --- |
| Proyecto de aplicación (50 %) | Repo GitHub, actividad continua, código y **URL desplegada** |
| Propuesta inicial | URL del repositorio + README del proyecto |
| Examen / prácticas | Capacidad de montar entorno y versionar |
| Uso de IA | Si la usas en el proyecto, **citarla** según la normativa |

Un repo con un único commit `final` la noche anterior cuenta menos que un desarrollo continuo.

### 4.21 Anti-patrones de Git (lista negra)

1. Commits `update`, `fix`, `asdf`.  
2. `git add .` + subir `.venv`.  
3. Fuerzas `push --force` a `main` sin saber.  
4. Trabajar semanas sin push (riesgo de pérdida).  
5. Meter binarios enormes en el historial.  
6. Poner la API key “un momentito” en un notebook y empujar.  
7. Reescribir historia compartida sin avisar.  

### 4.22 Problemas frecuentes de Git/GitHub

| Síntoma | Qué hacer |
| --- | --- |
| `rejected (fetch first)` | `git pull` (o `pull --rebase`) y resuelve; luego `push` |
| `Permission denied (publickey)` | Configura SSH o pasa a HTTPS |
| `Authentication failed` | Token/credencial caducada; regenera |
| PR sin cambios | Estás comparando la misma punta; empuja la rama correcta |
| Aparece `.venv` en el PR | `.gitignore` + `git rm -r --cached .venv` |
| `Your branch is ahead of origin/main` | Falta `git push` |
| Conflictos eternos | Sincroniza `main` más a menudo; PRs pequeños |
| Line endings CRLF/LF | En Windows: revisa `core.autocrlf`; no pelees en binarios |
| Archivo “modificado” sin cambios reales | Atributos/line endings; `git diff` para ver |

---

## 5. Ejemplo guiado extremo a extremo (venv + Git)

### 5.1 Parte A — entorno del curso

```bash
cd davd-26-27
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
pip install -r 2_app_visualizaciones/requirements.txt
python 3_despliegue_apps/0_entornos_y_git/ejemplos/check_entorno.py --strict
```

### 5.2 Parte B — repo personal

```bash
# tras crear el repo vacío en GitHub
git clone git@github.com:TU_USUARIO/davd-26-27-apellido-nombre.git
cd davd-26-27-apellido-nombre

cp /ruta/a/davd-26-27/3_despliegue_apps/0_entornos_y_git/ejemplos/gitignore_davd.txt .gitignore

cat > README.md <<'EOF'
# DAVD 2026-2027 — Apellido, Nombre

Máster: ...

## Objetivos
- Aprender Python robusto y testeable
- Automatizar flujos con IA
- Entregar una solución E2E

## Cómo instalar
```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt   # el de TU proyecto Dash
```
EOF

cat > sesion01.md <<'EOF'
# Sesión 1 — venv y Git

## Conceptos
- El venv aísla dependencias por proyecto
- Git versiona snapshots; GitHub las hospeda
- Nunca subir .venv ni .env

## Comandos clave
- source .venv/bin/activate
- git switch -c practica/sesion-01
- git commit -m "Add ..."
EOF

git switch -c practica/sesion-01
git add .gitignore README.md sesion01.md
git status
git commit -m "Add session 01 notes, README and gitignore"
git push -u origin practica/sesion-01
```

### 5.3 Parte C — Pull Request

1. Abre la URL que imprime GitHub tras el push (o *Contribute → Open pull request*).  
2. Completa la descripción.  
3. Merge a `main` cuando esté listo.  
4. En local: `git switch main && git pull`.

---

## 6. Seguridad, ética y uso de IA (desde el día 1)

### 6.1 Secretos

- Claves solo en `.env` o en secretos del PaaS.
- `.env` en `.gitignore`.
- `.env.example` sí se versiona.

### 6.2 Uso de asistentes (Cursor, ChatGPT, Claude, …)

Cuando generen partes relevantes del trabajo:

1. Revisa el código (no copies ciego).
2. Asegura que no inventa APIs.
3. Documenta en `README (y, si usas IA, cítarla)` herramienta + qué aceptaste/rechazaste.
4. Nunca pegues secretos en prompts cloud.

El uso no autorizado o sin citar puede considerarse plagio según la normativa de la Universidad.

---

## 7. Buenas prácticas de README (mínimo profesional)

Un README de proyecto DAVD debería responder:

1. ¿Qué problema resuelve?  
2. ¿Cómo se instala? (venv + requirements)  
3. ¿Cómo se ejecuta?  
4. ¿Cómo se testea?  
5. ¿Qué variables de entorno necesita?  
6. ¿Dónde está el despliegue (si existe)?  

Si un compañero no puede arrancar en 10 minutos, el README falla.

---

## 8. Autoevaluación (antes de dar por cerrada la sesión)

Responde por escrito en `sesion01.md`:

1. Diferencia entre Python global y `.venv`.  
2. ¿Para qué sirve `python -m pip` frente a llamar solo a `pip`?  
3. Explica working tree / staging / commit.  
4. ¿Clone y pull son lo mismo? ¿Por qué?  
5. Lista cuatro cosas que no se suben a GitHub y justifica una.  
6. Reescribe a buen estilo: `update`, `fix final`, `cambios varios`.  
7. ¿Qué haces si el IDE no importa `pandas` pero la terminal sí?  
8. ¿Qué haces si subiste `.env` por error?

---

## 9. Checklist de salida

### Entorno

- [ ] Python 3.11+ disponible  
- [ ] `.venv` creado y activado  
- [ ] `pip install -r 2_app_visualizaciones/requirements.txt` OK  
- [ ] `check_entorno.py --strict` → `ENTORNO OK`  
- [ ] IDE usando el intérprete del `.venv`  

### Git/GitHub

- [ ] `user.name` y `user.email` configurados  
- [ ] Repo personal creado y clonado  
- [ ] `.gitignore` con `.venv/` y `.env`  
- [ ] Rama de práctica con commits claros  
- [ ] PR visible (o merge) en GitHub  
- [ ] README con instalación básica  

### Comprensión

- [ ] Sé explicar reproducibilidad en una frase  
- [ ] Sé qué no se versiona y por qué  
- [ ] Sé el flujo rama → commit → push → PR  

---

## 10. Para la sesión del 15 sep

1. Deja el venv listo (no lo borres si funciona).  
2. Abre `2_app_visualizaciones/Datos/`.  
3. Ojea `2_app_visualizaciones/` y `2_app_visualizaciones/`.  
4. Trae el repo personal operativo: ahí vivirás el Proyecto I.

---

## 11. Apéndice A — Chuleta rápida de comandos

### venv

```bash
python3 -m venv .venv
source .venv/bin/activate          # Windows: .venv\Scripts\activate
deactivate
python -m pip install -r 2_app_visualizaciones/requirements.txt
python -c "import sys; print(sys.executable)"
```

### Git día a día

```bash
git status
git switch -c feature/nombre
git diff
git add archivo1 archivo2
git commit -m "Add meaningful message"
git push -u origin feature/nombre
git switch main
git pull
```

### Emergencias suaves

```bash
git restore archivo.py
git restore --staged archivo.py
git rm -r --cached .venv
git remote -v
ssh -T git@github.com
```

---

## 12. Apéndice B — Glosario corto EN/ES

| EN | ES / nota |
| --- | --- |
| repository | repositorio |
| commit | confirmación / foto del proyecto |
| branch | rama |
| merge | fusión |
| remote | remoto |
| staging area | área de preparación / stage |
| ignore | ignorar (no trackear) |
| pull request | solicitud de integración |
| virtual environment | entorno virtual |
| dependency | dependencia |

---

## 13. Apéndice C — Preguntas típicas de clase

**¿Puedo usar conda?**  
Sí en tu máquina, pero debes demostrar el flujo venv/requirements cuando se pida reproducibilidad.

**¿Hace falta GitHub Desktop?**  
No. La terminal + IDE bastan. Desktop es opcional.

**¿Puedo trabajar solo en `main`?**  
Técnicamente sí; pedagógicamente no es lo deseable. Usa ramas + PR.

**¿Qué pasa si mi PR es enorme?**  
Revisa por qué: quizá incluiste `.venv` o datos grandes. Corrige y empuja de nuevo.

**¿El profesor necesita acceso al repo privado?**  
Sí, cuando se indique: invita con permiso de lectura (o el que se pida).

---

## 14. Cierre

Si dominas este documento, tienes la base de ingeniería sobre la que se construye DAVD:

> **Código reproducible + historial limpio + secretos fuera.**

Eso no es burocracia: es lo que permite tests, CI, colaboración y despliegue de verdad.
