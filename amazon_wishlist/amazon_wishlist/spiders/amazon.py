# from amazon_wishlist.items import AmazonWishlistItem
import scrapy
import scrapy_playwright
from amazon_wishlist.items import AmazonWishlistItem


class AmazonSpider(scrapy.Spider):
    name = "amazon"
    allowed_domains = ["amazon.co.jp"]
    start_urls = [
        "https://www.amazon.co.jp/hz/wishlist/ls/3VQQS89WB9IIA?ref_=list_d_wl_lfu_nav_7"
    ]

    def parse(self, response):
        book = AmazonWishlistItem()

        book["title"] = response.xpath('//*[@id="productTitle"]/text()').get()
        
        book["author"] = response.xpath(
            '//*[@class="author"]/a[@class="a-link-normal"]/text()'
        ).get()
        book["price"] = response.xpath('//*[@id="price"]/text()').get()
        book["publisher"] = response.xpath(
            '//*[@id="detailBullets_feature_div"]/ul/li[1]/span/span[2]/text()'
        ).get()
        book["release_date"] = response.xpath(
            '//*[@id="detailBullets_feature_div"]/ul/li[2]/span/span[2]/text()'
        ).get()
        book["isbn10"] = response.xpath(
            '//*[@id="detailBullets_feature_div"]/ul/li[5]/span/span[2]/text()'
        ).get()
        print("================", book, "================")
        yield book
