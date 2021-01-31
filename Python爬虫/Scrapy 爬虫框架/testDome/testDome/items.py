# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class TestdomeItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    subname = scrapy.Field() #字母的名字
