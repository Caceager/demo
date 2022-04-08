# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class TeletiendaItem(scrapy.Item):
    name = scrapy.Field()
    usual_price = scrapy.Field()
    actual_price = scrapy.Field()
