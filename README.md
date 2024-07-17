# Web Scraping API for Coursera

## Description

This project is a FastAPI-based API for scraping Coursera. The API allows you to search for courses on Coursera and extract relevant information from the search results.

## Requirements

- Python 3.7+
- FastAPI
- Uvicorn
- Celery
- Requests
- BeautifulSoup

## Installation

1. Create and activate a virtual environment:

    ```bash
    python -m venv env
    source env/bin/activate  # On Windows: env\Scripts\activate
    ```

2. Install the dependencies:

    ```bash
    pip install -r requirements.txt
    ```

3. Start the FastAPI server:

    ```bash
    uvicorn api.main:app --reload
    ```

4. Make a POST request to `/scrape/coursera` with the `query` parameter to search for courses on Coursera or Udemy:

    ```bash
    curl -X POST "http://127.0.0.1:8000/scrape/coursera" -d "query=machine+learning"
    curl -X POST "http://127.0.0.1:8000/scrape/udemy" -d "query=machine+learning"
    ```

5. The API will return relevant information about the found courses.

## Files

- `api/main.py`: Main entry point of the API.
- `api/tasks.py`: Scraping functions and Celery tasks.
- `requirements.txt`: Project dependencies.
- `vercel.json`: Configuration for deployment on Vercel (optional).
