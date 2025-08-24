# web-crawler

A Python-based web crawler that scrapes Hacker News (https://news.ycombinator.com/) and provides filtering capabilities through a Flask web interface.

Good morning, afternoon, or evening. This is the result of the web scraping I completed. It took me quite some time, as I had never done web scraping before; however, with the help of online documentation and a few tutorials, I was able to complete it successfully!

First, I implemented the exercise in Python, as it is one of my strongest languages. While researching, I found that BeautifulSoup was one of the most commonly recommended tools. Reference links:

Web Scraping 101: Tools, Techniques, and Best Practices -> https://medium.com/geekculture/web-scraping-101-tools-techniques-and-best-practices-417e377fbeaf

Keith Galli – YouTube Tutorial -> https://www.youtube.com/watch?v=DcI_AZqfZVc&ab_channel=KeithGalli

After some investigation, I decided to go with this option and started building the project. I used the following video as a full guide: Corey Schafer – Web Scraping with BeautifulSoup -> https://www.youtube.com/watch?v=ng2o98k983k&ab_channel=CoreySchafer
, and also referred to the following documentation:

Real Python: Web Scraping with BeautifulSoup -> https://realpython.com/beautiful-soup-web-scraper-python/

BeautifulSoup Documentation -> https://www.crummy.com/software/BeautifulSoup/bs4/doc/

Requests Library Documentation -> https://requests.readthedocs.io/en/latest/

I started with test_scrapper.py to test the scraper itself before moving on to the app. Then, I created test_app.py to test the web application after verifying that the scraper was working correctly.

I tried to simplify the code as much as possible to make it clean, readable, and easy to follow. Once I had it running locally (simply in Visual Studio Code), I pushed it to GitHub, created a Codespace, and started making commits so the progress could be tracked.

At some point, I ran into errors that I didn’t fully understand. After reviewing the code and running the tests again, I noticed a parsing issue because I had cleaned up the code and was no longer using .text.
<img width="512" height="70" alt="image" src="https://github.com/user-attachments/assets/071c3023-16ab-4d6b-9aea-31a90bc64d7f" />


Another issue occurred when running python hn_crawler/app.py, as the hn_crawler package could not be found. I resolved this by running the module as python -m hn_crawler.app.

I also realized that the titles were not being filtered correctly for those with fewer than five words. After struggling to identify the error, I asked a former university colleague and friend for help. He pointed out that when passing 0 as min_words, the code would only recognize empty titles. I then adjusted the function accordingly (commit: Final fixes + less and more than 5 words).

Finally, everything was working perfectly. However, as a full-stack developer, I couldn’t leave the web page with a plain white background and four basic columns, so I added some styling to make it more visually appealing.
