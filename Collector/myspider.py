import scrapy
class Myspider(scrapy.Spider):
    name = 'blogspider'
    start_urls = ['https://wx.5i5j.com/ershoufang/']

    def parse(self, response):
        for title in response.css('.listTit'):
            yield {'title': title.css('a ::text').get()}

        # for next_page in response.css('a.next-posts-link'):
        #     yield response.follow(next_page, self.parse)