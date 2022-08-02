# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class AmazonWishlistItem(scrapy.Item):
    title = scrapy.Field()
    author = scrapy.Field()
    price = scrapy.Field()
    publisher = scrapy.Field()
    release_date = scrapy.Field()
    isbn10 = scrapy.Field()

