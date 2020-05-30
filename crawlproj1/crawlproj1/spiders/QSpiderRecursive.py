import scrapy


class QSpiderRecursive(scrapy.Spider):
    name= 'QSpiderRecursive'

    def start_requests(self):
        url='http://quotes.toscrape.com/page/1/'

        yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, Response ):

        for q in Response.css('div.quote'):
            text= q.css('span.text::text').get()
            author= q.css('small.author::text').get()
            tags= q.css('a.tag::text').get()

            yield {
                'text': text,
                'author': author,
                'tags': tags
            }


        url_nextpage= Response.css('li.next a::attr(href)').get()
        if url_nextpage is not None:
            url_nextpage= Response.urljoin(url_nextpage)
            yield scrapy.Request(url=url_nextpage,callback=self.parse)
