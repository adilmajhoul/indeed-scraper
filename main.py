import requests
import time

# from lxml import html
from bs4 import BeautifulSoup
from selectolax.parser import HTMLParser

# import matplotlib.pyplot as plt
from urllib.parse import urlencode
from myhtml import html_content
from lib import jrint, get_text, build_url
from requests_html import HTMLSession
from fake_headers import Headers


NEXT_PAGE_BUTTON_SELECTOR = 'a[aria-label="Next Page"]'
CURRENT_PAGE_BUTTON_SELECTOR = ""
PREVIOUS_PAGE_BUTTON_SELECTOR = ""
JOB_TITLE_SLECTOR = ""
JOB_COMPANY_SLECTOR = ""
JOB_LOCATION_SLECTOR = ""
JOB_DATE_SLECTOR = ""

SEARCH_BUTTON_SELECTOR = "#jobsearch > div > div.css-169igj0.eu4oa1w0 > button"


header = {
    "User-Agent": "Mozilla/5.0 (iPad; CPU OS 12_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148"
}


def get_header():
    return Headers(
        browser="chrome",  # Generate only Chrome UA
        os="mac",  # Generate ony Windows platform
        headers=True,  # generate misc headers
    ).generate()


# if len(parser.css('a[aria-label="Next Page"]')) >= 1 is not None:
#     print("no more pages to scrap.")
#     break

# -----------------------------------

nav_html = """
<nav role="navigation" aria-label="pagination" class="css-98e656 eu4oa1w0"><ul class="css-1g90gv6 eu4oa1w0"><li class="css-227srf eu4oa1w0"><a data-testid="pagination-page-prev" aria-label="Previous Page" href="/jobs?q=developer&amp;l=rabat&amp;sort=date" class="css-akkh0a e8ju0x50"><svg xmlns="http://www.w3.org/2000/svg" focusable="false" role="img" fill="currentColor" viewBox="0 0 24 24" aria-hidden="true" class="css-1xqhio eac13zx0"><path d="M14.112 18.002c.2.2.52.204.716.008l.707-.707a.507.507 0 00-.009-.716L10.94 12l4.587-4.587c.2-.2.205-.521.01-.716l-.708-.708a.507.507 0 00-.716.01l-5.648 5.647c-.1.1-.148.234-.143.367.002.124.05.247.143.34l.001.001a.758.758 0 00.008.008l5.64 5.64z"></path></svg></a></li><li class="css-227srf eu4oa1w0"><a data-testid="pagination-page-1" aria-label="1" href="/jobs?q=developer&amp;l=rabat&amp;sort=date" class="css-163rxa6 e8ju0x50">1</a></li><li class="css-227srf eu4oa1w0"><a data-testid="pagination-page-current" aria-current="page" href="#" class="css-1ek5kzj e71d0lh0">2</a></li><li class="css-227srf eu4oa1w0"><a data-testid="pagination-page-3" aria-label="3" href="/jobs?q=developer&amp;l=rabat&amp;sort=date&amp;start=20" class="css-163rxa6 e8ju0x50">3</a></li><li class="css-227srf eu4oa1w0"><a data-testid="pagination-page-next" aria-label="Next Page" href="https://ma.indeed.com/jobs?q=developer&amp;l=rabat&amp;sort=date&amp;start=20&amp;pp=gQAeAAAAAAAAAAAAAAACKcq2cQANAQAAkxapnNtQQXmM5gAA" class="css-akkh0a e8ju0x50"><svg xmlns="http://www.w3.org/2000/svg" focusable="false" role="img" fill="currentColor" viewBox="0 0 24 24" aria-hidden="true" class="css-1xqhio eac13zx0"><path d="M9.888 5.998a.506.506 0 00-.716-.008l-.707.707a.506.506 0 00.01.716L13.06 12l-4.587 4.587c-.2.2-.204.521-.009.716l.707.707a.507.507 0 00.717-.009l5.647-5.648c.1-.1.148-.233.144-.366a.492.492 0 00-.144-.34v-.001a.611.611 0 00-.009-.009L9.888 5.998z"></path></svg></a></li></ul></nav>
"""
# url = "https://ma.indeed.com/jobs?q=developer&l=rabat&sort=date"
# res = requests.get(url, headers=header)
# print("res: ", res)
# html = res.text
# # print(html)

# soup = BeautifulSoup(html, "html.parser")


# parser = HTMLParser(html)

# print(
#     "soup search button:",
#     soup.select(SEARCH_BUTTON_SELECTOR),
# )

# print("selectolax search button", parser.css(SEARCH_BUTTON_SELECTOR))

# -----------------------------------

titles = []

pages = 3
duplication = False

for page in range(pages):
    print("page: ", page)

    url = f"https://ma.indeed.com/jobs?q=stage&l=rabat&sort=date&start={str(page * 10)}"
    print("url: ", url)
    html = requests.get(url, headers=get_header()).text
    parser = HTMLParser(html)

    print("next button ->", parser.css('a[aria-label="Next Page"]'))

    for node in parser.css("ul.css-zu9cdh > li"):
        print("node: ", node)
        if len(node.css("h2.jobTitle > a")) > 0:
            titles.append(get_text(node.html, "h2.jobTitle > a"))
        else:
            print("no more job pages")
            duplication = True
            break

        # if duplication:
        #     print("break loop because finished pagination")
        #     break

print("titles: ", titles)
# job = {
#     "title": get_text(node.html, "h2.jobTitle > a"),
#     "company": get_text(node.html, "span.companyName"),
#     "location": get_text(node.html, "div.companyLocation"),
#     "posted": get_text(node.html, "span.date"),
# }


# ---------------------------------
# Find all <a> tags
# a_tags = soup.find_all(
#     "nav",
#     role="navigation",
# )

# Extract and print the text inside each <a> tag
# for a in a_tags:
# print(a.get_text())
# ---------------------------------


# def get_parser(session, url):
#     parser = session.get(url)
#     return parser


# session = HTMLSession()
# url = "https://ma.indeed.com/jobs?q=stage&l=rabat&sort=date"

# parser = get_parser(session, url)

# print(parser.html.find('a[aria-label="Next Page"]'))

# ---------------------------------



# def get_header():
#     return Headers(
#         browser="chrome",  # Generate only Chrome UA
#         os="mac",  # Generate ony Windows platform
#         headers=True,  # generate misc headers
#     ).generate()


# h = get_header()
# print("h: ", h)

# session = HTMLSession()
# url = "https://ma.indeed.com/jobs?q=stage&l=rabat&sort=date"
# response = session.get(url, headers=h)


# print("response: ", response)

# el = response.html.find('a[aria-label="Next Page"]')
# print("el:", el)

# -------

# header = Headers(
#     browser="chrome",  # Generate only Chrome UA
#     os="mac",  # Generate ony Windows platform
#     headers=True,  # generate misc headers
# )

# for i in range(5):
#     print(header.generate())
