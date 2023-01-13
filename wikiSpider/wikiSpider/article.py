import scrapy

class ARticleSpider(scrapy.Spider):
    name='article'
    
    def start_requests(self):
        urls=[
            'https://en.wikipedia.org/wiki/Python_'
            '%28programming_language%29',
            'https://en.wikipedia.org/wiki/Functional_programming',
            'https://en.wikipedia.org/wiki/Monty_Python']
        return [scrapy.Request(url=url, callback=self.parse)]
    
    def parse(self, response):
        url = response.url
        title=response.css('h1::text').extract_first()
        print('URL is: {}'.format(url))
        print('Title is: {}'.format(title))
        