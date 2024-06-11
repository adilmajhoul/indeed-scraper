from selectolax.parser import HTMLParser
from requests_html import HTMLSession
from urllib.parse import urlencode
import csv
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

APPLY_BUTTON_SELECTOR = 'button[newtabwarningtext="opens in a new tab"]'


JOB_LINK_SELECTOR = "a.jcs-JobTitle"


class Scraper:
    def __init__(self, queries, location, sort_by=None, country="ma"):
        self.queries = queries
        self.location = location
        self.sort_by = sort_by
        self.INDEEED_SEARCH_BASE_URL = f"https://{country}.indeed.com/jobs"
        self.INDEEED_BASE_URL = f"https://{country}.indeed.com"
        self.INDEED_JOB_PAGE_BASE_URL = f"https://{country}.indeed.com/viewjob?jk="
        self.jobs = []
        self.session = HTMLSession()
        self.headers = Headers(
            browser="chrome",
            os="mac",
            headers=True,
        ).generate()

    def build_url(self, query):
        # Define the query parameters
        params = {
            "q": query,
            "l": self.location,
        }

        # If sort_by is not None, add it to the params
        if self.sort_by is not None:
            params["sort"] = self.sort_by

        # Encode the parameters and join them with the base URL
        url = f"{self.INDEEED_SEARCH_BASE_URL}?{urlencode(params)}"

        return url

    def get_parser(self, url):
        parser = self.session.get(url, headers=self.headers)
        return parser

    def does_elment_exist(self, element):
        return len(element) > 0

    def get_header():
        return Headers(
            browser="chrome",  # Generate only Chrome UA
            os="mac",  # Generate ony Windows platform
            headers=True,  # generate misc headers
        ).generate()

    def is_job_in_indeed(self, job_link):
        if not job_link:
            return False

        parser = self.get_parser(job_link)
        apply_button = parser.html.find(APPLY_BUTTON_SELECTOR)

        if apply_button:
            return True

        return False

    def get_element_text(self, node, selector):

        text = (
            node.find(selector)[0].text
            if self.does_elment_exist(node.find(selector))
            else "None"
        )
        return text

    def get_element_attribute(self, node, selector, attribute):
        attribute = (
            node.find(selector)[0].attrs[attribute]
            if self.does_elment_exist(node.find(selector))
            else "None"
        )
        return attribute

    # this filter needs auth
    # def is_already_aplied(self, job_link):
    #     pass

    def scrape(self):
        for query in self.queries:
            starting_url = self.build_url(query)

            i = 0
            while True:
                print("-------->", "Page:", i, "<--------")
                if i == 0:
                    print("starting_url: ", starting_url)
                    parser = self.get_parser(starting_url)

                next_page = parser.html.find('a[aria-label="Next Page"]')

                for job in parser.html.find("#mosaic-provider-jobcards > ul > li"):
                    if len(job.find(JOB_TITLE_SELECTOR)) > 0:
                        job_link = (
                            self.INDEED_JOB_PAGE_BASE_URL
                            + job.find(JOB_LINK_SELECTOR)[0].attrs["data-jk"]
                            if self.does_elment_exist(job.find(JOB_LINK_SELECTOR))
                            else False
                        )

                        if self.is_job_in_indeed(job_link):
                            print("inside job")
                            job_dict = {
                                # TODO: create dict builder function that takes func(title=JOB_TITLE_SELECTOR)
                                "title": job.find(JOB_TITLE_SELECTOR)[0].text,
                                "company": (
                                    self.get_element_text(job, JOB_COMPANY_SELECTOR)
                                ),
                                "location": (
                                    self.get_element_text(job, JOB_LOCATION_SELECTOR)
                                ),
                                "date": (self.get_element_text(job, JOB_DATE_SELECTOR)),
                                "link": (
                                    self.INDEED_JOB_PAGE_BASE_URL
                                    + self.get_element_attribute(
                                        job, JOB_LINK_SELECTOR, "data-jk"
                                    )
                                ),
                            }
                            # if self.is_job_in_indeed(job_dict.link):
                            # self.jobs.append(job_dict)
                            self.export_to_csv(
                                filename=f"scraped_data/{query}_{self.location}.csv",
                                job=job_dict,
                            )

                        else:
                            print("outside job")

                # Get the next page URL if its None break loop
                if len(next_page) > 0:
                    url = self.INDEEED_BASE_URL + next_page[0].attrs["href"]
                    parser = self.get_parser(url)
                else:
                    break

                print("url: ", url)

                i += 1

            # Export the jobs for the current query to the CSV file
            # self.export_to_csv(filename=f"scraped_data/{query}_{self.location}.csv")

            print("self.jobs: ", self.jobs)

            # Clear the jobs list for the next query
            self.jobs = []

    # def export_to_csv(self, filename="jobs.csv"):
    #     with open(
    #         filename, "a", newline=""
    #     ) as file:  # Append to the file instead of overwriting it
    #         writer = csv.DictWriter(
    #             file, fieldnames=["title", "company", "location", "date", "link"]
    #         )
    #         if file.tell() == 0:  # If the file is empty, write the header
    #             writer.writeheader()
    #         for job in self.jobs:
    #             writer.writerow(job)

    def export_to_csv(self, filename="jobs.csv", job={}):
        with open(
            filename, "a", newline=""
        ) as file:  # Append to the file instead of overwriting it
            writer = csv.DictWriter(
                file, fieldnames=["title", "company", "location", "date", "link"]
            )
            if file.tell() == 0:  # If the file is empty, write the header
                writer.writeheader()

            writer.writerow(job)


if __name__ == "__main__":

    scraper = Scraper(queries=["developer"], location="rabat", sort_by="date")
    scraper.scrape()
