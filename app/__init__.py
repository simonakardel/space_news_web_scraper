from flask import Flask, render_template, request, redirect, url_for, session
from flask_sqlalchemy import SQLAlchemy
from apscheduler.schedulers.background import BackgroundScheduler
from .models import db, Article
from scraper.scrapping_controller import scrape_all_sources
import os
from database.db_operations import build_query, paginate_query
from dotenv import load_dotenv
from flask_migrate import Migrate

load_dotenv()

ARTICLES_PER_PAGE = 9


def create_app():
    """
    Creates and configures the Flask application.

    Returns:
        app (Flask): The Flask application instance.
    """
    app = Flask(__name__)


    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('SUPABASE_DATABASE_URL')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    app.secret_key = os.environ.get('SECRET_KEY', 'default_secret_key')

    db.init_app(app)
    migrate = Migrate(app, db)

    with app.app_context():
        db.create_all()

    init_routes(app)
    init_scheduler(app)

    return app


def init_scheduler(app):
    """
    Initializes and starts the background scheduler for scraping.
    """
    scheduler = BackgroundScheduler(daemon=True)

    def scrape_with_context():
        """
        Scrapes all sources within the Flask application context.
        """
        with app.app_context():
            scrape_all_sources()

    scheduler.add_job(scrape_with_context, 'interval', minutes=1)
    scheduler.start()


def init_routes(app):
    """
    Initializes the routes for the Flask application.

    Args:
        app (Flask): The Flask application instance.
    """
    @app.route('/')
    def index():
        """
        Renders the home page with articles.

        Returns:
            render_template: The rendered template with articles and pagination.
        """
        page = request.args.get('page', default=1, type=int)
        filter_category = request.args.get('filter')

        session_filter = session.get('filter')
        if filter_category and filter_category != session_filter:
            session['filter'] = filter_category
            return redirect(url_for('index', filter=filter_category, page=1))

        if not filter_category:
            if session_filter:
                session.pop('filter', None)
                return redirect(url_for('index', page=1))

        if filter_category:
            query = build_query(filter_category)
        else:
            query = Article.query

        articles_pagination = paginate_query(query, page, ARTICLES_PER_PAGE)

        articles = articles_pagination.items
        current_page = articles_pagination.page

        return render_template('home.html', articles=articles, pagination=articles_pagination, current_page=current_page)


if __name__ == "__main__":
    app = create_app()
    app.run(use_reloader=False)
