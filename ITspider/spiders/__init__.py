import scrapy
import elasticsearch
from ITspider import items
class ITSpider(scrapy.Spider):
    name = "ITSpider"
    es = elasticsearch.Elasticsearch()
    def start_requests(self):
        start_urls= "http://cec.jmu.edu.cn"
        yield scrapy.Request(start_urls)

    def parse(self, response):

        urls=response.xpath('//@href').getall()

        for url in urls :
            next_url="http://cec.jmu.edu.cn/"+url


            item = items.ItspiderItem()

            item['title'] = "".join(response.xpath('//td[@class="titlestyle124904"]/text()').getall())
            item['create_date'] = "".join(response.xpath('//td/span[@class="timestyle124904"]/text()').getall())
            item['url'] = response.url
            item['content'] = "".join(response.xpath('//div[@class="v_news_content"]/p/text()').getall())

            yield item
            yield scrapy.Request(next_url, callback=self.parse)

    def hello(self):
        pass

        #with open("spider_run.txt","a+") as f:
           # f.write("\n")
           # f.write(response.url+"标题："+"".join(response.xpath('//td[@class="titlestyle124904"]/text()').getall()))
           # f.write("\n")
          #  f.write("内容："+response.xpath().getall())
      #  f.close()



        #filename = response.xpath('//h3[@class="con-jj-title fl"]/text()').getall()
       # self.log(filename)
   # def get_info(self,response):









