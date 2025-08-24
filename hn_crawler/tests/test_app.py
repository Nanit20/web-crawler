import pytest
from hn_crawler.app import create_app

@pytest.fixture
def client():
    app = create_app()
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_index_route(client):
    response = client.get('/')
    assert response.status_code == 200
    assert b'Hacker News Crawler' in response.data
    assert b'Titles with More Than 5 Words' in response.data
    assert b'Titles with 5 or Fewer Words' in response.data