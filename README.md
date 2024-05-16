# Space News Web Scraper

This project is a web scraper designed to gather articles about space, with a particular focus on Mars and black holes. The motivation behind it was to explore web scraping techniques and centralize my favorite space articles in one place.

Web scraping is a method used to extract significant amounts of data from websites. You can do this using online services, APIs, or by writing your own code. For this project, I opted to write my own code in Python, using libraries like BeautifulSoup and Requests.

This project features a collection of web scrapers that extract articles from various space-related websites. Each scraper is organized in a dedicated Python file, extracting the title, summary, link, image URL, and source of each article. The collected data is then stored in a SQLite database.

The project structure is as follows:
- **Scraper Directory:** Contains the scraping logic. Each website has its own scraper file (e.g., `mars_scraper.py`, `space_com_scraper.py`), and `scraping_controller.py` manages the overall scraping process.
- **Database Directory:** Handles operations for storing scraped articles in the database.
- **App Directory:** Hosts a Flask application that presents the scraped articles on a webpage. Articles are displayed in a structured format, with the latest articles shown first.

This project demonstrates how web scraping can automate data collection, making it easier for enthusiasts of specific topics to access information. It also showcases the power and flexibility of Python and its libraries for web scraping and development.

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/yourusername/yourrepository.git
    ```
2. Navigate to the project directory:
    ```sh
    cd yourrepository
    ```
3. Install the required Python packages:
    ```sh
    pip install -r requirements.txt
    ```

## Usage

To run a scraper, navigate to the project directory and execute the corresponding Python file. For instance, to run the `space_com_scraper.py` scraper, use this command:

```sh
python space_com_scraper.py
