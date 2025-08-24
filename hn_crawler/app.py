from flask import Flask, render_template
from hn_crawler.scraper import HackerNewsScraper

def create_app():
    app = Flask(__name__)
    scraper = HackerNewsScraper()

    @app.route('/')
    def index():
        items = scraper.scrape()
        more_than_five = scraper.filter_by_title_length(items, 5, 'comments', mode="greater")
        less_than_five = scraper.filter_by_title_length(items, 5, 'points', mode="less_equal")
        return render_template('index.html', 
                            more_than_five=more_than_five, 
                            less_than_five=less_than_five)

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True, host='0.0.0.0')