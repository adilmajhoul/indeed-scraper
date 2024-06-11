from selectolax.parser import HTMLParser

from requests_html import HTMLSession
from fake_headers import Headers


NEXT_PAGE_BUTTON_SELECTOR = 'a[aria-label="Next Page"]'
CURRENT_PAGE_BUTTON_SELECTOR = ""
PREVIOUS_PAGE_BUTTON_SELECTOR = ""
JOB_CARDS_LIST_SELECTOR = "#mosaic-provider-jobcards > ul"
JOB_CARD_SELECTOR = "#mosaic-provider-jobcards > ul > li"

JOB_TITLE_SELECTOR = "h2.jobTitle"
JOB_COMPANY_SELECTOR = 'span[data-testid="company-name"]'
JOB_LOCATION_SELECTOR = 'div[data-testid="text-location"]'
JOB_DATE_SELECTOR = 'span[data-testid="myJobsStateDate"]'
JOB_LINK_SELECTOR = "a.jcs-JobTitle"


INDEEED_BASE_URL = "https://ma.indeed.com"


def get_header():
    return Headers(
        browser="chrome",  # Generate only Chrome UA
        os="mac",  # Generate ony Windows platform
        headers=True,  # generate misc headers
    ).generate()


def get_parser(session, url):
    parser = session.get(url)
    return parser


starting_url = f"{INDEEED_BASE_URL}/jobs?q=developer&l=casablanca"


session = HTMLSession()
job_titles = []
i = 0
while True:
    print("-------->", "Page:", i, "<--------")
    if i == 0:
        print("starting_url: ", starting_url)
        parser = get_parser(session, starting_url)

    next_page = parser.html.find('a[aria-label="Next Page"]')

    for job in parser.html.find(JOB_CARD_SELECTOR):
        if len(job.find(JOB_TITLE_SELECTOR)) > 0:
            job_titles.append(job.find(JOB_TITLE_SELECTOR)[0].text)

    job_titles.append("************")

    if len(next_page) > 0 and next_page is not None:
        url = INDEEED_BASE_URL + next_page[0].attrs["href"]
        parser = get_parser(session, url)
    else:
        break

    print("url: ", url)

    i += 1

print(job_titles)
