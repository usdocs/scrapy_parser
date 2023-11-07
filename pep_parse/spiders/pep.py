import re
import scrapy

from pep_parse.constants import ALLOWED_DOMAINS, START_URLS
from pep_parse.items import PepParseItem


class PepSpider(scrapy.Spider):
    name = 'pep'
    allowed_domains = ALLOWED_DOMAINS
    start_urls = START_URLS

    def parse(self, response):
        peps_table = response.css(
            'section[id="numerical-index"] table tbody tr'
        )

        for tr_in_table in peps_table:
            pep_link_str = tr_in_table.css('a').attrib['href']
            yield response.follow(
                pep_link_str + '/', callback=self.parse_pep
            )

    def parse_pep(self, response):
        pep_text = response.css('section[id="pep-content"] h1::text').get()
        number = re.search(r'\d+', pep_text)
        name = re.sub(r'PEP \d+ – ', "", pep_text)
        item = {
            'number': number[0],
            'name': name,
            'status': response.css(
                'dt:contains("Status") + dd abbr::text'
            ).get()
        }
        yield PepParseItem(item)
