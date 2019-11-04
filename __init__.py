# This package will contain the spiders of your Scrapy project
#
# Please refer to the documentation for information on how to create and manage
# your spiders.
import scrapy
import elasticsearch


from realITspider import items
from realITspider import BsUtil
from realITspider import elasticSearchUtils
class ITSpider(scrapy.Spider):
    name = "ITSpider"
    elasticSearchUtils.add_index("itartical")
    def start_requests(self):
        elasticSearchUtils.add_index("artical")
        start_urls= "http://cec.jmu.edu.cn/list.jsp?urltype=tree.TreeTempUrl&wbtreeid="
        for i in range(1041,1200):
            url = start_urls+str(i)
            yield scrapy.Request(url)
    def parse(self, response):
        urls = BsUtil.get_all_url(response.body.decode("utf-8"))
        next_page = BsUtil.to_next_page(response.body.decode("utf-8"))
        if urls != []:
            self.log(urls)
        if BsUtil.to_next_page(response.body.decode("utf-8")) != None:
            yield scrapy.Request(BsUtil.to_next_page(response.body.decode("utf-8")), callback=self.parse)
        for i in urls:
            #self.log(i)
            yield scrapy.Request(i,callback=self.get_detail)
    def get_detail(self,response):
        item = items.RealitspiderItem()
        item['title'] =BsUtil.get_title(response.body.decode("utf-8"))
        item['url']=response.url
        item['type']=BsUtil.getType(response.body.decode("utf-8"))
        item['content']=BsUtil.getContent(response.body.decode("utf-8"))
        item['date']=BsUtil.getDate(response.body.decode("utf-8"))
        yield item











