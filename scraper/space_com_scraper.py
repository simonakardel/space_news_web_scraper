from scraper.utilities import fetch_page, categorize_article
from app.models import Article
from datetime import datetime

def scrape_articles():
    url = 'https://www.space.com/the-universe/black-holes'
    soup = fetch_page(url)
    articles = []
    if soup:
        for article_div in soup.find_all('div', class_='listingResult'):
            try:
                title = article_div.find('h3').get_text(strip=True) if article_div.find('h3') else None
                article_link_tag = article_div.find('a', class_='article-link', href=True)
                link = article_link_tag['href'] if article_link_tag and 'href' in article_link_tag.attrs else None
                summary = article_div.find('p', class_='synopsis').get_text(strip=True) if article_div.find('p') else None
                image_tag = article_div.find('img')
                image_url = image_tag['data-original-mos'] if image_tag and 'data-original-mos' in image_tag.attrs else (
                    image_tag['src'] if image_tag else None)
                date_scraped = datetime.now().date()
                if title and summary and link and image_url:
                    categories = categorize_article(title, summary)
                    new_article = Article(
                        title=title,
                        link=link,
                        summary=summary,
                        image_url=image_url,
                        categories=categories,
                        source="space.com",
                        date_scraped=date_scraped,
                    )
                    articles.append(new_article)
            except Exception as e:
                print(f"Error processing article at {link}: {e}")

    return articles



