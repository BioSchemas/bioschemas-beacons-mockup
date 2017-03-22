import scrapy
from extruct.w3cmicrodata import MicrodataExtractor

class BeaconsSpider(scrapy.Spider):
    name="beacons_links"

    def start_request(self):
        urls=[
            'http://localhost/beacons_pages_schema/EGA_Beacon_service.htm',
            'http://localhost/beacons_pages_schema/GA4GH_Beacon.htm',
        ]

    def parse(self, response):
        for beacon_page in response:
            mde = MicrodataExtractor()
            beacon_data=mde.extract(html_content)
            yield{
                beacon_data
            }
