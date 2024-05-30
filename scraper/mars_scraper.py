import sys
import logging
from os.path import dirname, abspath

scraper_dir = dirname(abspath(__file__))
project_dir = dirname(scraper_dir)
sys.path.append(project_dir)

from scraper.utilities import fetch_page, categorize_article
from app.models import Article, db
from datetime import datetime

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

BASE_URL = "https://science.nasa.gov"

def is_absolute_url(url):
    return url.startswith('http://') or url.startswith('https://')

def article_exists(link):
    return db.session.query(Article).filter_by(link=link).first() is not None

def scrape_nasa_articles():
    url = BASE_URL + '/mars/stories/'
    soup = fetch_page(url)
    articles = []
    if soup:
        for item in soup.find_all('div', class_='hds-content-item'):
            try:
                title_tag = item.find('h3')
                title = title_tag.get_text(strip=True) if title_tag else None

                link_tag = item.find('a', href=True)
                link = link_tag['href'] if link_tag else None
                if link and not is_absolute_url(link):
                    link = BASE_URL + link 

                img_tag = item.find('img')
                image_url = img_tag['src'] if img_tag else None

                summary_tag = item.find('p')
                summary = summary_tag.get_text(strip=True) if summary_tag else None

                date_scraped = datetime.now().date()

                if title and link and image_url:
                    categories = categorize_article(title, summary)
                    
                    if not article_exists(link):
                        new_article = Article(
                            title=title, 
                            link=link, 
                            summary=summary, 
                            image_url=image_url, 
                            categories=categories, 
                            source="NASA", 
                            date_scraped=date_scraped
                        )
                        articles.append(new_article)
                        logger.info(f"Added new article: {title}")
                    else:
                        logger.info(f"Article with link {link} already exists. Skipping.")
            except Exception as e:
                logger.error(f"Error processing article: {e}")

    return articles

