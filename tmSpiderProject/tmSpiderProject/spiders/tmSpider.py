import scrapy
import logging

logger = logging.getLogger("AppName")
from bs4 import BeautifulSoup


class tmSpider(scrapy.spiders.Spider):
    name = "tmSpider"
    allowed_domains = ["tmall.com"]
    start_urls = [
        "https://list.tmall.com/search_product.htm?q=%D0%AC%D7%D3",
    ]

    def parse(self, response):
        soup = BeautifulSoup(response.text)
        title = soup.select("title")[0].get_text()
        productList = soup.select(".product-iWrap")
        for product in productList:
            # 对于专辑可以跳过
            # 这个是每一个商品的循环
            if len(product.select(".pal-resume")) > 0:
                break
            productId = product.select(".product")[0].attrs["data-id"]
            dataId = product.select(".productPrice")[0].select("em")[0].attrs["title"]
            productStatus = product.select(".productStatus")
            monthSales = productStatus[0].select("span em")[0]
            commentsNum = productStatus[0].select(".productStatus > span:nth-child(2) > a")[0].get_text()
            dataAtp = product.select(".ww-small")[0].attrs["data-atp"]
            sellerId = dataAtp.split(",")[-1]
