# -*- coding: utf-8 -*-
import json
from scrapy.loader import ItemLoader
from scrapy.loader import processors

def strip(value):
    return value.strip()

class AduanasItemLoader(ItemLoader):
    default_item_class = dict
    default_input_processor = processors.MapCompose(strip)
    default_output_processor = processors.TakeFirst()
    links_out = processors.Identity()

    def add_item_links(self, selector):
        data = json.loads(self.selector.css(selector).extract_first())
        sub = json.loads(data.get('Subfile1ContainerData', '{}'))
        self.add_value(
            'links',
            [sub[str(index)]['Props'][0][4] for index in range(sub.get('Count'))])
