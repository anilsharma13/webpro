import scrapy

#
# class ProwebSpider(scrapy.Spider):
#     name = 'proweb'
#     allowed_domains = ['www.pythonscraping.com']
#     start_urls = ['https://pythonscraping.com']
#
#     def parse(self, response):
#         for body in response.xpath("//h3"):
#             name=body.xpath(".//text()").get
#             # Heading=response.xpath("//h3").get()
#             yield{
#                 'name':body
#             }
# #
# class ProwebSpider(scrapy.Spider):
#     name = 'proweb'
#     allowed_domains = ['www.pythonscraping.com']
#     start_urls = ['https://pythonscraping.com/about']
#
#     def parse(self, response):
#         for body in response.xpath("//h3"):
#             home = body.xpath(".//text()").get
#             # Heading=response.xpath("//h3").get()
#             yield {
#                  'name': body,
#             }

#
# class ProwebSpider(scrapy.Spider):
#     name = 'proweb'
#     allowed_domains = ['www.pythonscraping.com']
#     start_urls = ['https://pythonscraping.com/contact']
#
#     def parse(self, response):
#         for body in response.xpath("//h3"):
#             name = body.xpath(".//text()").get
#             # Heading=response.xpath("//h3").get()
#             yield {
#                  'name': body
#             }


# class ProwebSpider(scrapy.Spider):
#     name = 'proweb'
#     allowed_domains = ['www.pythonscraping.com']
#     start_urls = ['https://pythonscraping.com/processes']
#
#     def parse(self, response):
#         for body in response.xpath("//h3"):
#             name = body.xpath(".//text()").get
#             # Heading=response.xpath("//h3").get()
#             yield {
#                  'name': body
#             }



class ProwebSpider(scrapy.Spider):
    name = 'proweb'
    allowed_domains = ['www.pythonscraping.com']
    start_urls = ['https://pythonscraping.com/blog']

    def parse(self, response):
        for body in response.xpath("//h5"):
            name = body.xpath(".//text()").get
            # Heading=response.xpath("//h3").get()
            yield {
                 'name': body
            }
