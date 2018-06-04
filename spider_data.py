import scrapy
import logging
logging.getLogger('scrapy').setLevel(logging.WARNING)

class dataSpider(scrapy.Spider):
	name = 'dataSpider'
        start_urls = ['http://www.vgchartz.com/yearly/2018/Global']
	
	def parse(self, response):
		for e in response.css('td'):
			yield { 'data': ''.join(e.css('::text').extract()).strip() }


    
        
        

