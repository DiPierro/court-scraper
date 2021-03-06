import requests
from lxml import html
from fake_useragent import UserAgent

from court_scraper.base.request_base_page import RequestsBasePage
from .url import OklahomaURLs

class CaseDetails(RequestsPage):
    
    url = OklahomaURLs.case_details
    
    def _build_payload(self):
        self.payload = {
            'db' : self.county,
            'number' : self.case_number,
                       }
    
    def page_source(self, county, case_number):
        self.county = county
        self.case_number = case_number
        self._build_payload()
        self.output = self.get_html(self.url, payload = self.payload)