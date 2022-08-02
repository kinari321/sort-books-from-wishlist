# from amazon_wishlist.items import AmazonWishlistItem
import scrapy
import scrapy_playwright
from amazon_wishlist.items import AmazonWishlistItem


class AmazonSpider(scrapy.Spider):
    name = "amazon"
    allowed_domains = ["amazon.co.jp"]
    start_urls = [
        "https://www.amazon.co.jp/%E3%82%A8%E3%82%AF%E3%82%B9%E3%83%88%E3%83%AA%E3%83%BC%E3%83%A0%E3%83%97%E3%83%AD%E3%82%B0%E3%83%A9%E3%83%9F%E3%83%B3%E3%82%B0-%E3%82%B1%E3%83%B3%E3%83%88-%E3%83%99%E3%83%83%E3%82%AF/dp/4274217620/"
    ]

    def parse(self, response):
        sample = AmazonWishlistItem()

        sample["title"] = response.xpath('//*[@id="productTitle"]/text()').get()
        sample["author"] = response.xpath(
            '//*[@class="author"]/a[@class="a-link-normal"]/text()'
        ).get()
        sample["price"] = response.xpath('//*[@id="price"]/text()').get()
        sample["publisher"] = response.xpath(
            '//*[@id="detailBullets_feature_div"]/ul/li[1]/span/span[2]/text()'
        ).get()
        sample["release_date"] = response.xpath(
            '//*[@id="detailBullets_feature_div"]/ul/li[2]/span/span[2]/text()'
        ).get()
        sample["isbn10"] = response.xpath(
            '//*[@id="detailBullets_feature_div"]/ul/li[5]/span/span[2]/text()'
        ).get()
        print("================", sample, "================")
        yield sample
