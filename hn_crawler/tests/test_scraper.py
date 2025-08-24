import pytest
from hn_crawler.scraper import HackerNewsScraper, NewsItem

def test_scraper_initialization():
    scraper = HackerNewsScraper()
    assert scraper.url == "https://news.ycombinator.com/"

def test_get_word_count():
    scraper = HackerNewsScraper()
    assert scraper.get_word_count("This is - a test") == 4
    assert scraper.get_word_count("Hello world!") == 2
    assert scraper.get_word_count("One-two-three four") == 4

def test_filter_by_title_length():
    scraper = HackerNewsScraper()
    items = [
        NewsItem(1, "This is a long title here", 100, 10),
        NewsItem(2, "Short title", 200, 5),
        NewsItem(3, "Another very long title example", 50, 20)
    ]
    more_than_five = scraper.filter_by_title_length(items, 5, 'comments')
    assert len(more_than_five) == 2
    assert more_than_five[0].comments == 20
    less_than_five = scraper.filter_by_title_length(items, 0, 'points')
    assert len(less_than_five) == 1
    assert less_than_five[0].points == 200