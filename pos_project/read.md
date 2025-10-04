# Entorno virtual - ¡MUY IMPORTANTE!
zero/
env_pos/
venv/
env/

# Archivos de configuración local que pueden contener secretos
local_settings.py
.env

# Bases de datos locales
*.sqlite3
db.sqlite3

# Archivos de medios subidos por los usuarios
/media/

# Archivos estáticos compilados (Django los genera al desplegar)
/staticfiles/

# Archivos de Python
__pycache__/
*.pyc

# Archivos de sistema operativo
.DS_Store
Thumbs.db
```

#### 1.2. Crear el archivo `requirements.txt`

Este archivo es una lista de todas las librerías de Python que tu proyecto necesita para funcionar (como `Django`, `psycopg2-binary`, etc.). Esto permite que cualquier persona (¡incluido tu yo del futuro!) pueda instalar todas las dependencias fácilmente en una nueva máquina.

En tu terminal, asegúrate de que tu entorno virtual esté activado y ejecuta el siguiente comando:

```bash
pip freeze > requirements.txt
```

Esto creará un archivo `requirements.txt` en la raíz de tu proyecto con el contenido necesario.

### Parte 2: Subir el Proyecto a GitHub

Ahora que tu proyecto está preparado, sigue estos pasos en la terminal de VS Code, dentro de la carpeta raíz de tu proyecto.

1.  **Crea un Repositorio en GitHub:** Ve a [github.com](https://github.com), crea un nuevo repositorio **público y vacío** (sin README ni .gitignore) y copia su URL HTTPS.

2.  **Inicializa Git en tu proyecto:**
    ```bash
    git init
    ```

3.  **Añade todos tus archivos:** (Git automáticamente ignorará los que están en `.gitignore`)
    ```bash
    git add .
    ```

4.  **Crea tu primer "commit" (un punto de guardado):**
    ```bash
    git commit -m "Versión inicial del proyecto POS"
    ```

5.  **Conecta tu repositorio local con el de GitHub:**
    ```bash
    # Reemplaza la URL con la de tu repositorio
    git remote add origin [https://github.com/tu-usuario/tu-repositorio.git](https://github.com/tu-usuario/tu-repositorio.git)
    ```

6.  **Sube tu código a GitHub:**
    ```bash
    git push -u origin main
    ```

¡Listo! Tu código ya está seguro en GitHub.

### Parte 3: Descargar y Ejecutar el Proyecto en otra PC

Ahora, imagina que estás en una computadora nueva. Estos son los pasos que seguirías para poner a andar el proyecto.

1.  **Instala el software necesario:** Asegúrate de que la nueva PC tenga instalados Python, Git y PostgreSQL.

2.  **Clona el repositorio:** Abre una terminal y ejecuta el comando `git clone` con la URL de tu repositorio.
    ```bash
    git clone [https://github.com/tu-usuario/tu-repositorio.git](https://github.com/tu-usuario/tu-repositorio.git)
    ```

3.  **Navega a la carpeta del proyecto:**
    ```bash
    cd tu-repositorio
    ```

4.  **Crea y activa un nuevo entorno virtual:**
    ```bash
    python -m venv env
    # Actívalo (env\Scripts\activate en Windows, source env/bin/activate en Mac/Linux)
    ```

5.  **Instala todas las dependencias:** Este comando lee el archivo `requirements.txt` e instala todo lo necesario.
    ```bash
    pip install -r requirements.txt
    ```

6.  **Configura la Base de Datos:**
    * Abre PostgreSQL (o pgAdmin) y crea una nueva base de datos (ej: `dbpedidos`) y un nuevo usuario con su contraseña, tal como lo hiciste en la primera máquina.
    * **¡Paso clave!** Abre el archivo `pos_project/settings.py` y **modifica la sección `DATABASES`** para que coincida con el nombre de la base de datos, usuario y contraseña de la **nueva máquina**. Como este archivo está en tu repositorio, tendrás que editarlo manualmente.

7.  **Crea la estructura de la Base de Datos:** Este comando leerá todos los archivos de migración que descargaste y creará todas las tablas.
    ```bash
    python manage.py migrate
    ```

8.  **Crea un superusuario para la nueva máquina:** Necesitarás un administrador para poder iniciar sesión.
    ```bash
    python manage.py createsuperuser
    ```

9.  **¡Ejecuta el servidor!**
    ```bash
    python manage.py runserver
    

