from scraper import mars_scraper, space_com_scraper
from database.db_operations import save_articles

def scrape_all_sources():
    articles = []
    articles.extend(mars_scraper.scrape_nasa_articles())
    articles.extend(space_com_scraper.scrape_articles())
    
    save_articles(articles)

if __name__ == "__main__":
    scrape_all_sources()
