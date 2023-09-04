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
        books = response.xpath('//*[@class="a-fixed-right-grid"]')
        
        for book_elem in books:
            book = AmazonWishlistItem()
            book["title"] = book_elem.xpath('.//a[@class="a-link-normal"]/@title').get()
            book["author"] = book_elem.xpath('.//span[@class="a-size-base"]/text()').get().strip()
            book["price"] = response.xpath('.//span[@class="a-price-whole"]/text()').get()
            book["publisher"] = ""
            # response.xpath('//*[@id="detailBullets_feature_div"]/ul/li[1]/span/span[2]/text()').get()
            book["review_star"] = response.xpath('.//span[@class="a-icon-alt"]/text()').get()
            
            book["release_date"] = ""
            # response.xpath('//*[@id="detailBullets_feature_div"]/ul/li[2]/span/span[2]/text()').get()
            book["isbn10"] = ""
            # response.xpath('//*[@id="detailBullets_feature_div"]/ul/li[5]/span/span[2]/text()').get()
            
            yield {
                "title": book["title"],
                "author": book["author"],
                "price": book["price"],
                "publisher": book["publisher"],
                "review_star": book["review_star"],
                "release_date": book["release_date"],
                "isbn10": book["isbn10"],
            }

            print("================", book, "================")
