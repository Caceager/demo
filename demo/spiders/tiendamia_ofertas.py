#!/usr/bin/env python3

import items
import scrapy


class TeletiendaOfertas(scrapy.Spider):
    name = "ofertas"

    start_urls = ["https://www.teletiendauy.com/collections/ofertas-web/"]


    def parse(self, response):
        page = response.url

        elementos = response.xpath(
            '//div[@class="grid__item small--one-half medium-up--one-fifth"]'
        )


        for elemento in elementos:
            item = items.TeletiendaItem()

            title = elemento.xpath(
                './/div[@class="product-card__name"]/text()'
            ).get()

            usual_price = elemento.xpath(
                './/s[@class="product-card__regular-price"]/text()'
            ).get()

            actual_price = elemento.xpath(
                './/div[@class="product-card__price"]/text()'
            ).getall()[3].strip()


            item["name"] = title
            item["usual_price"] = usual_price
            item["actual_price"] = actual_price

            yield item


        next_page = response.xpath('//span[@class="next"]/a/@href').get()
        next_page = response.urljoin(next_page)
        if next_page:
            yield scrapy.Request(url=next_page, callback=self.parse)
