from fastapi import FastAPI
from .tasks import scrape_linkedin, scrape_coursera, scrape_udemy

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Web Scraping API"}

@app.post("/scrape/linkedin")
def start_linkedin_scraping(query: str, location: str):
    scrape_linkedin.delay(query, location)
    return {"message": "LinkedIn scraping started"}

@app.post("/scrape/coursera")
def start_coursera_scraping(query: str):
    result = scrape_coursera(query)
    return {"data": result}

@app.post("/scrape/udemy")
def start_udemy_scraping(query: str):
    scrape_udemy.delay(query)
    return {"message": "Udemy scraping started"}
