from urllib import request
import requests
import time
from lxml import html
from bs4 import BeautifulSoup
from selectolax.parser import HTMLParser
import matplotlib.pyplot as plt
from urllib.parse import urlencode
from myhtml import html_content
from lib import jrint, get_text, build_url


# search_query = input('Enter Your Search Query: ').strip()
# location = input('Enter Your location: ').strip()
# pages = int(input('Enter Pages To Scrape: ').strip())


header = {
    "User-Agent": "Mozilla/5.0 (iPad; CPU OS 12_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148"
}


# parser = HTMLParser(html_content)
titles = []

# pages = 3
# for page in range(pages):
#     print("page: ", page)

#     url = f"https://ma.indeed.com/jobs?q=developer&l=rabat&start={str(page * 10)}"
#     print("url: ", url)
#     html = requests.get(url, headers=header).text
#     parser = HTMLParser(html)

#     for node in parser.css("ul.css-zu9cdh > li"):
#         if len(node.css("h2.jobTitle > a")) >= 1:
#             job = {
#                 "title": get_text(node.html, "h2.jobTitle > a"),
#                 "company": get_text(node.html, "span.companyName"),
#                 "location": get_text(node.html, "div.companyLocation"),
#   "posted": get_text(node.html, "span.date")
#   }
#             titles.append(job)

# if len(parser.css('a[aria-label="Next Page"]')) >= 1 is not None:
#     print("no more pages to scrap.")
#     break

jrint("titles: ", titles)

# ----------------------

nav_html = """
<nav role="navigation" aria-label="pagination" class="css-98e656 eu4oa1w0"><ul class="css-1g90gv6 eu4oa1w0"><li class="css-227srf eu4oa1w0"><a data-testid="pagination-page-prev" aria-label="Previous Page" href="/jobs?q=developer&amp;l=rabat" class="css-akkh0a e8ju0x50"><svg xmlns="http://www.w3.org/2000/svg" focusable="false" role="img" fill="currentColor" viewBox="0 0 24 24" aria-hidden="true" class="css-1xqhio eac13zx0"><path d="M14.112 18.002c.2.2.52.204.716.008l.707-.707a.507.507 0 00-.009-.716L10.94 12l4.587-4.587c.2-.2.205-.521.01-.716l-.708-.708a.507.507 0 00-.716.01l-5.648 5.647c-.1.1-.148.234-.143.367.002.124.05.247.143.34l.001.001a.758.758 0 00.008.008l5.64 5.64z"></path></svg></a></li><li class="css-227srf eu4oa1w0"><a data-testid="pagination-page-1" aria-label="1" href="/jobs?q=developer&amp;l=rabat" class="css-163rxa6 e8ju0x50">1</a></li><li class="css-227srf eu4oa1w0"><a data-testid="pagination-page-current" aria-current="page" href="#" class="css-1ek5kzj e71d0lh0">2</a></li></ul></nav>
"""
url = "https://ma.indeed.com/jobs?q=developer&l=rabat&start=30"
html = requests.get(url, headers=header).text

# soup = BeautifulSoup(html, "lxml")
soup = BeautifulSoup(nav_html, "html.parser")

# texts = [el.contents[2].get_text().strip() for el in soup.select('a.vacancy-card > h4')]

parser = HTMLParser(html)

# print("soup:", soup.select(".yosegi-InlineWhatWhere-primaryButton"))
print("next", parser.select('a[data-testid="pagination-page-current"]').text().strip())


# Find all <a> tags
# a_tags = soup.find_all(
#     "nav",
#     role="navigation",
# )

# Extract and print the text inside each <a> tag
# for a in a_tags:
# print(a.get_text())
