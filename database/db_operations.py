from app import db 
from app.models import Article 

def insert_article(title, link, summary, image_url, full_article):
    new_article = Article(
        title=title,
        link=link,
        summary=summary,
        image_url=image_url,
        full_article=full_article
    )
    db.session.add(new_article)
    db.session.commit()


def save_articles(articles):
    try:
        with db.session.begin_nested():
            db.session.add_all(articles)
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        print(f"An error occurred while saving articles: {e}")

def build_query(filter_category):
    if filter_category:
        return Article.query.filter(Article.categories.contains(filter_category))
    else:
        return Article.query

def paginate_query(query, page, per_page):
    return query.order_by(Article.id.desc()).paginate(page=page, per_page=per_page, error_out=False)
