import requests
from bs4 import BeautifulSoup

def fetch_page(url):
    """Fetches a webpage and returns a BeautifulSoup object."""
    response = requests.get(url)
    if response.ok:
        return BeautifulSoup(response.text, 'html.parser')
    else:
        print(f"Failed to fetch {url}")
        return None

def categorize_article(title, summary):
    categories = []
    keywords = {
        'mars': [
            'mars', 'martian', 'red planet', 'mars rover', 'mars exploration',
            'martian surface', 'mars mission', 'life on mars', 'terraforming mars', 'olympus mons'
        ],
        'black holes': [
            'black hole', 'event horizon', 'singularity', 'accretion disk', 
            'hawking radiation', 'supermassive black hole', 'stellar black hole',
            'gravitational waves', 'spaghettification', 'sagittarius a*'
        ]
    }
    combined_text = title.lower() + ' ' + summary.lower()
    for category, triggers in keywords.items():
        if any(trigger in combined_text for trigger in triggers):
            categories.append(category)
    return categories
