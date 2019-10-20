import scrapy

class ITSpider(scrapy.Spider):
    name = "ITSpider"
    def start_requests(self):
        start_urls= "http://cec.jmu.edu.cn"
        yield scrapy.Request(start_urls)

    def parse(self, response):

        urls=response.xpath('//@href').getall()

        for url in urls :
            next_url="http://cec.jmu.edu.cn/"+url


            self.log(next_url)
            yield scrapy.Request(next_url, callback=self.parse)

        with open("spider_run.txt","a+") as f:
            f.write("\n")
            f.write(response.url+"标题："+"".join(response.xpath('//td[@class="titlestyle124904"]/text()').getall()))
            f.write("\n")
            f.write("内容："+response.xpath().getall())
        f.close()



        #filename = response.xpath('//h3[@class="con-jj-title fl"]/text()').getall()
       # self.log(filename)
   # def get_info(self,response):









