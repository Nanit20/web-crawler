from dataclasses import dataclass
import re
import requests
from bs4 import BeautifulSoup
from typing import List

@dataclass
class NewsItem:
    number: int
    title: str
    points: int
    comments: int

class HackerNewsScraper:
    def __init__(self, url: str = "https://news.ycombinator.com/"):
        self.url = url

    def fetch_page(self) -> str:
        response = requests.get(self.url)
        response.raise_for_status()
        return response.text

    def parse_page(self, html: str) -> List[NewsItem]:
        soup = BeautifulSoup(html, 'html.parser')
        items = []
        rows = soup.select('tr.athing')[:30]  # Get first 30 entries

        for index, row in enumerate(rows, 1):
            # Extraer título
            title_span = row.select_one('span.titleline > a')
            title = title_span.text.strip() if title_span else ''
            
            # Extraer subtext (puntos y comentarios)
            subtext = row.find_next_sibling('tr').find('td', class_='subtext')
            points = 0
            comments = 0
            if subtext:
                score = subtext.find('span', class_='score')
                points = int(score.text.split()[0]) if score else 0
                comment_link = subtext.find_all('a')[-1]
                comments_text = comment_link.text.strip()
                comments = int(comments_text.split()[0]) if comments_text != 'discuss' else 0

            items.append(NewsItem(number=index, title=title, points=points, comments=comments))
    
        return items

    def get_word_count(self, title: str) -> int:

        clean_title = re.sub(r'[^\w\s]', ' ', title)
        return len(clean_title.split())

    def filter_by_title_length(self, items: List[NewsItem], min_words: int, sort_key: str, mode: str = "greater") -> List[NewsItem]:
        if mode == "greater":
            filtered = [item for item in items if self.get_word_count(item.title) > min_words]
        else:
            filtered = [item for item in items if self.get_word_count(item.title) <= min_words]

        if sort_key == 'comments':
            return sorted(filtered, key=lambda x: x.comments, reverse=True)
        return sorted(filtered, key=lambda x: x.points, reverse=True)

    def scrape(self) -> List[NewsItem]:
        html = self.fetch_page()
        return self.parse_page(html)