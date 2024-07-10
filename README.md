# Web Scraping API for Coursera

## Descripción

Este proyecto es una API de FastAPI para realizar scraping en Coursera. La API permite realizar búsquedas de cursos en Coursera y extraer información relevante de los resultados de búsqueda.

## Requisitos

- Python 3.7+
- FastAPI
- Uvicorn
- Celery
- Requests
- BeautifulSoup

## Instalación

1. Crea y activa un entorno virtual:

    ```bash
    python -m venv env
    source env/bin/activate  # En Windows: env\Scripts\activate
    ```

2. Instala las dependencias:

    ```bash
    pip install -r requirements.txt
    ```
3. Inicia el servidor FastAPI:

    ```bash
    uvicorn api.main:app --reload
    ```

4. Realiza una solicitud POST a `/scrape/coursera` con el parámetro `query` para buscar cursos en Coursera o en Udemy:

    ```bash
    curl -X POST "http://127.0.0.1:8000/scrape/coursera" -d "query=machine+learning"
    curl -X POST "http://127.0.0.1:8000/scrape/udemy" -d "query=machine+learning"
    ```

5. La API devolverá información relevante sobre los cursos encontrados.

## Archivos

- `api/main.py`: Punto de entrada principal del API.
- `api/tasks.py`: Funciones de scraping y tareas de Celery.
- `requirements.txt`: Dependencias del proyecto.
- `vercel.json`: Configuración para despliegue en Vercel (opcional).

