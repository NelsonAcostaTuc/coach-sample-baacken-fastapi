import requests

def fetch_coursera_html(query):
    url = f"https://www.coursera.org/search?query={query}"
    response = requests.get(url)
    if response.status_code == 200:
        with open("coursera_search_results.html", "w", encoding="utf-8") as file:
            file.write(response.text)
        print("HTML saved successfully.")
    else:
        print(f"Error: {response.status_code}")

# Ejemplo de uso
fetch_coursera_html("machine learning")
