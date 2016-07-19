# -*- coding: utf-8 -*-

from scrapy.loader import ItemLoader
from scrapy.loader import processors

def strip(value):
    return value.strip()

class AduanasItemLoader(ItemLoader):
    default_input_processor = processors.MapCompose(strip)
    default_output_processor = processors.TakeFirst()
    default_item_class = dict
