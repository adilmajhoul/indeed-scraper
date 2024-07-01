import scrapy
from indeed_scraper.items import IndeedScraperItem
from urllib.parse import urlencode
from fake_headers import Headers

class IndeedSpider(scrapy.Spider):
    name = 'indeed_spider'
    allowed_domains = ['indeed.com']
    

    custom_settings = {
        "DOWNLOAD_DELAY": 4,  
        "CONCURRENT_REQUESTS_PER_DOMAIN": 1, 
        "RETRY_TIMES": 3,  
        "ITEM_PIPELINES": {
            "scrapy_theworldwatch.pipelines.UsersPipeline": 1,
        },
    }

    def __init__(self, queries, location, sort_by=None, country="ma", *args, **kwargs):
        super(IndeedSpider, self).__init__(*args, **kwargs)
        
        self.queries = queries
        self.location = location
        self.sort_by = sort_by
        self.country = country
        self.INDEEED_SEARCH_BASE_URL = f"https://{country}.indeed.com/jobs"
        self.headers = Headers(browser="chrome", os="mac", headers=True).generate()

    def start_requests(self):
        for query in self.queries:
            url = self.build_url(query)
            yield scrapy.Request(url, headers=self.headers, callback=self.parse)

    def build_url(self, query):
        params = {"q": query, "l": self.location}
        if self.sort_by:
            params["sort"] = self.sort_by
        url = f"{self.INDEEED_SEARCH_BASE_URL}?{urlencode(params)}"
        return url

    def parse(self, response):
        job_cards = response.css("#mosaic-provider-jobcards > ul > li")
        for job in job_cards:
            item = IndeedScraperItem()
            item['title'] = job.css("h2.jobTitle::text").get()
            item['company'] = job.css('span[data-testid="company-name"]::text').get()
            item['location'] = job.css('div[data-testid="text-location"]::text').get()
            item['date'] = job.css('span[data-testid="myJobsStateDate"]::text').get()
            job_link = job.css("a.jcs-JobTitle::attr(data-jk)").get()
            
            if job_link:
                item['link'] = f"https://{self.country}.indeed.com/viewjob?jk={job_link}"
            yield item

        next_page = response.css('a[aria-label="Next Page"]::attr(href)').get()
        
        if next_page:
            next_page_url = f"https://{self.country}.indeed.com{next_page}"
            yield scrapy.Request(next_page_url, headers=self.headers, callback=self.parse)
