import scrapy
from scrapy.selector import Selector
from smzdm.items import SmzdmItem


class PhoneSpider(scrapy.Spider):
    name = 'phone'
    allowed_domains = ['smzdm.com', '127.0.0.1']
    start_urls = ['https://www.smzdm.com/fenlei/zhinengshouji/h5c4s0f0t0p1/#feed-main/']
    # start_urls = ['http://127.0.0.1/smzdm_phone.html']
    # start_urls = ['http://127.0.0.1/iphone12.html']
    
    def parse(self, response):
        
        phoneSelector = Selector(response = response).xpath('//div[@class="z-feed-content "]/h5')
        # //*[@id="feed-main-list"]/li[1]/div/div[2]/h5
        # //*[@id="feed-main-list"]/li[1]/div/div[2]
        for phone in phoneSelector[:10]:
            title = phone.xpath('./a/text()').extract_first()
            link = phone.xpath('./a/@href').extract_first()
            print (title)
            print (link)
            yield scrapy.Request(url=link, meta={'title': title, "entry": link}, callback=self.parse_detail)
    
    def parse_detail(self, response):
        print ("==============")
        link = response.meta['entry']
        paginationSelector = Selector(response = response).xpath('//ul[@class="pagination"]')
        pagination = paginationSelector[0]
        lastpageSelector = pagination.xpath('./li')[-4]
        lastpage = lastpageSelector.xpath('./a/text()').extract_first()
        # print (lastpage)
        lastpage = int(lastpage)
        for p in range(lastpage):
            yield scrapy.Request(url='%s/p%d/#comments' % (link, p), meta=response.meta, callback=self.parse_comment)
       
        
    
    def parse_comment(self, response):
    
    # def parse(self, response):
        title = response.meta['title']
        # //*[@id="li_comment_172402745"]/div[2]/div[2]/div[1]/p
        # //*[@id="li_comment_172422152"]/div[2]/div[3]/div[1]/p
        # //*[@id="commentTabBlockNew"]/ul[1]
        i = 1
        items = []
        commentListBoxSelector = Selector(response = response).xpath('//div[@id="commentTabBlockNew"]/ul[@class="comment_listBox"]')
        for commentSelector in commentListBoxSelector:
            # print (commentSelector.xpath('./li/div/div/div[@class="comment_con"]/p/text()').extract_first())
            print ("~~~~")
            for li in commentSelector.xpath('./li'):
                item = SmzdmItem()
                comment = li.xpath('./div[@class="comment_conBox"]/div[@class="comment_conWrap"]/div[1]/p/span/text()').extract()
                # print (i, comment)
                i += 1
                item['title'] = title
                item['comment'] = ",".join(comment)
                items.append(item)
                
        return items
