
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import JSON

db = SQLAlchemy()

class Article(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False, unique=True)
    link = db.Column(db.String(255), unique=True)
    summary = db.Column(db.Text)
    image_url = db.Column(db.String(255))
    date_scraped = db.Column(db.Date)
    categories = db.Column(JSON)
    source = db.Column(db.String(255))

    def __repr__(self):
        return f"<Article {self.title}>"
