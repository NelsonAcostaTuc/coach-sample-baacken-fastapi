from celery import Celery
import requests
from bs4 import BeautifulSoup
import os

celery = Celery(__name__, broker='pyamqp://guest@localhost//')

HTML_FILE_PATH = os.path.join(os.path.dirname(__file__), 'coursera_search_results.html')

@celery.task
def fetch_html(query):
    url = f"https://www.coursera.org/search?query={query}"
    response = requests.get(url)
    if response.status_code == 200:
        with open(HTML_FILE_PATH, "w", encoding="utf-8") as file:
            file.write(response.text)
        print("HTML saved successfully.")
    else:
        print(f"Error: {response.status_code}")

@celery.task
def scrape_linkedin(query, location):
    url = f"https://api.linkedin.com/v2/jobSearch?q={query}&location={location}"
    headers = {
        "Authorization": f"Bearer YOUR_API_KEY"
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        data = response.json()
        # Procesar y guardar datos según necesidad
        print(data)
    else:
        print(f"Error: {response.status_code}")

@celery.task
def scrape_coursera(query):
    fetch_html(query)  # Fetch the HTML first
    
    # Verify the file exists before reading
    if not os.path.exists(HTML_FILE_PATH):
        return {"error": "HTML file not found"}
    
    with open(HTML_FILE_PATH, "r", encoding="utf-8") as file:
        content = file.read()
        
    soup = BeautifulSoup(content, 'html.parser')

    # Extract the title of the page
    page_title = soup.title.string if soup.title else "No title found"
    
    # Extract meta description
    meta_description = soup.find('meta', attrs={'name': 'description'})
    meta_description_content = meta_description['content'] if meta_description else "No description found"

    # Extract the first paragraph text as an example
    first_paragraph = soup.find('p')
    first_paragraph_text = first_paragraph.text if first_paragraph else "No paragraph found"
    
    # Debugging: print the extracted data
    print(f"Page Title: {page_title}")
    print(f"Meta Description: {meta_description_content}")
    print(f"First Paragraph: {first_paragraph_text}")

    data = {
        'page_title': page_title,
        'meta_description': meta_description_content,
        'first_paragraph': first_paragraph_text
    }

    return data

@celery.task
def fetch_html_udemy(query):
    url = f"https://www.udemy.com/courses/search/?q={query}"
    response = requests.get(url)
    if response.status_code == 200:
        with open(HTML_FILE_PATH, "w", encoding="utf-8") as file:
            file.write(response.text)
        print("HTML saved successfully.")
    else:
        print(f"Error: {response.status_code}")

@celery.task
def scrape_udemy(query):
    fetch_html(query)  # Fetch the HTML first
    
    # Verify the file exists before reading
    if not os.path.exists(HTML_FILE_PATH):
        return {"error": "HTML file not found"}
    
    with open(HTML_FILE_PATH, "r", encoding="utf-8") as file:
        content = file.read()
        
    soup = BeautifulSoup(content, 'html.parser')

    # Extraer y mostrar el título de la página
    page_title = soup.title.string if soup.title else 'No title found'
    
    # Extraer y mostrar la meta descripción
    meta_description = soup.find('meta', attrs={'name': 'description'})
    meta_description_content = meta_description['content'] if meta_description else 'No description found'
    
    # Extraer enlaces populares
    popular_links = []
    popular_topics = soup.select('div.js-side-nav-popular-topics a')
    for link in popular_topics:
        popular_links.append({
            'text': link.get_text(strip=True),
            'href': link['href']
        })
    
    # Devolver la información extraída
    result = {
        'page_title': page_title,
        'meta_description': meta_description_content,
        'popular_links': popular_links
    }
    return result