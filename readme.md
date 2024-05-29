# Space News Web Scraper

A Flask application that scrapes and displays the latest space news from various sources. This project utilizes web scraping to gather articles and presents them in a user-friendly web interface.

## Features

- **Automated Scraping:** Periodically scrapes articles from specified space news websites.
- **Categorization:** Articles are categorized based on keywords (e.g., Mars, Black Holes).
- **Pagination:** Articles are displayed with pagination to improve readability.
- **Filter:** Users can filter articles by category.
- **User-friendly Interface:** Simple and clean web interface built with basic HTML and CSS.

## Installation and Setup

To run this application locally, follow these steps:

1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/space-news-web-scraper.git
   cd space-news-web-scraper
   
2. **Install the required dependencies:**

    ```bash
    pip install -r requirements.txt

3. **Set up the environment variables:**

    Create a `.env` file in the root directory and add the following:

    `SECRET_KEY=your_secret_key`

4. **Initialize the database:**

    ```bash
    flask db init
    flask db migrate
    flask db upgrade

5. **Run the application:**

    ``` bash
    flask run

## Usage


Once the application is running, open your web browser and navigate to <http://127.0.0.1:5000/>. The home page displays the latest scraped articles. You can filter articles by category using the filter options provided.

## Configuration

### Scheduler Interval

The scraping interval is set to 1 day by default. You can modify this interval in the `init_scheduler` function within the `app.py` file.

## Dependencies

-   **Flask:** Micro web framework for Python.
-   **Flask-SQLAlchemy:** SQLAlchemy support for Flask applications.
-   **APScheduler:** Python Scheduler for scheduling tasks.
-   **BeautifulSoup4:** Library for web scraping purposes.
-   **Requests:** Simple HTTP library for Python.
-   **python-dotenv:** Reads key-value pairs from a `.env` file and can set them as environment variables.