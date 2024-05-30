import scrapy
import re
from no_accent_vietnamese import no_accent_vietnamese as NAV


class CovidSpider(scrapy.Spider):
   name = 'covid'
   allowed_domains = ['web.archive.org']
   start_urls = ['https://web.archive.org/web/20210907023426/https://ncov.moh.gov.vn/vi/web/guest/dong-thoi-gian']
    
   def parse(self, response):
      get_data = response.xpath("//div[@class = 'timeline-detail']")
      for data in get_data :
         # Lấy thời gian
         time = data.xpath(".//div[@class = 'timeline-head']/h3/text()").get()

         #Lấy văn bản chứa thông tin về số ca nhiễm mới
         p2= data.xpath(".//div[@class = 'timeline-content']/p[2]/text()").get()
         p2_strong = data.xpath(".//div[@class = 'timeline-content']/p[2]/strong/text()").get()
         #Lấy thông tin về số ca nhiễm của mỗi thành phố
         p3= data.xpath(".//div[@class = 'timeline-content']/p[3]/text()").get()

         #Thông tin ca nhiễm thuộc thẻ span của p[3]
         
         p3_span= data.xpath(".//div[@class = 'timeline-content']/p[3]/span/text()").get()
         
         #Nav() dùng để loại bỏ dấu tiếng Việt
         convert_p2 = NAV(p2_strong) if p2_strong else NAV(p2)
         if convert_p2[:12] == 'THONG BAO VE':
            #Nếu thông tin nằm trong thẻ p thứ 3 thì lấy p3_span, ngược lại lấy p3
            convert_p3 = NAV(p3_span) if p3_span else NAV(p3)
            #Tìm số ca nhiễm
            case_str =re.search(r'(\d+(?:\.\d+)?)', convert_p2).group(1)
            new_case = case_str.replace(".","")
            #Tìm thành phố và số ca nhiễm theo format: tên tỉnh/Thành phố (<số ca nhiễm>)
            cities = re.findall(r"((TP. )*([A-Z]{1}[a-z]+ (- )*)+)\((\d+(?:\.\d+)?)\)",convert_p3)

            #Trường hợp số ca nhiễm chỉ có trong 1 tỉnh
            if len(cities) == 0:
               cities = re.findall(r"[tai|tia] ((TP. )*([A-Z]{1}[a-z]+() (- )*).+?)[.]",convert_p3)
               cities = cities[0][0].split(', ')
               cities = [[i] for i in cities]
               if len(cities) >= 2:
                  for i in range(0,len(cities)):
                     cities[i].append(1)
               else :
                  cities[0].append(new_case)

            yield{
               'time' : time,
               'new_case' : int(new_case),
               'cities_case' : [{'city' : city[0].replace('.',''),'case' : city[-1]  } for city in cities]
               }   
      link = response.xpath("//ul[@class = 'lfr-pagination-buttons pager']/li[2]/a/@href").get()
      if link is not None :
         yield scrapy.Request(url = link, callback = self.parse)