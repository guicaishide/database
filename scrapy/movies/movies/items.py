# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class MoviesItem(scrapy.Item):
    # define the fields for your item here like:
    title = scrapy.Field()
    job = scrapy.Field()
    number = scrapy.Field()
    place = scrapy.Field()
    pub_time = scrapy.Field()

