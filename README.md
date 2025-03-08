# backend-users - Instrucciones de instalación

Estas instrucciones te guiarán para configurar el backend del proyecto "backend-users" en tu máquina local para desarrollo y pruebas.

**Pasos de instalación**

1. **Clonar el repositorio:**
    ```bash
    git clone https://github.com/carlosbarreraacuna/backend-users/
    cd backend-users
    ```
    Reemplaza `https://github.com/carlosbarreraacuna/backend-users/` con la URL real de tu repositorio Git.

2. **Crear un entorno virtual:** 
    ```bash
    python -m venv venv
    ```

3. **Activar el entorno virtual:**
    * Windows:
        ```bash
        venv\Scripts\activate
        ```

4. **Instalar las dependencias:**
    ```bash
    pip install django
    pip install djangorestframework
    pip install django-filter
    pip install django-cors-headers
    pip install psycopg2

5. **Aplicar migraciones:**
    ```bash
    python manage.py migrate
    ```

6. **Iniciar el servidor de desarrollo:**
    ```bash
    python manage.py runserver
    ```
    
    Ahora deberías poder acceder al backend en tu navegador en la dirección [http://127.0.0.1:8000/](http://127.0.0.1:8000/).

