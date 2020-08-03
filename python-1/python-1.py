
import requests
from bs4 import BeautifulSoup as bs

def requests_test(target_url):
    user_agent = "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36 Edg/83.0.478.64"

    h = {'user-agent': user_agent}

    #target_url = "https://movie.douban.com/top250"
    
    response = requests.get(target_url, headers=h)

    #print (response.text)
    print (response.status_code)
    return response.text


def bs4_test():
    text = requests_test("https://movie.douban.com/top250")
    soup = bs(text, 'html.parser')


import lxml.etree
def xpath_test():
    text = requests_test("https://movie.douban.com/subject/1292052/")
    selector = lxml.etree.HTML(text)

    film_name = selector.xpath('//*[@id="content"]/h1/span[1]/text()')
    print("film name is %s" % (film_name))
    
    date = selector.xpath('//*[@id="info"]/span[11]/text()')
    print("date: %s" % date)
    
    summary = selector.xpath('//*[@id="link-report"]/span[1]/span/text()')
    print ("summary: %s" % summary)

    return [film_name, date, summary]

import pandas as pd
def pandas_test():
    d = xpath_test()
    movie_info = pd.DataFrame(data=d)
    movie_info.to_csv("./movie.csv", encoding='gbk',
                      index=False, header=False)

 
def page_turn():
    urls = tuple(f"https://movie.douban.com/top250?start={ page * 25 }&filter=" for page in range(0, 10))
    print (urls)

    for url in urls:
        print (url)
        text = requests_test(url)
        selector = lxml.etree.HTML(text)
        name = selector.xpath(
            '//*[@id="content"]/div/div[1]/ol/li[2]/div/div[2]/div[1]/a/span[1]/text()')
        print (name)

def yield_test():
    def chain():
        for i in range(5):
            yield i

    v = chain()
    print (v)  # <generator object yield_test.<locals>.chain at 0x000000000CF00318>
    v2 = next(v)
    print (v2)  # 0
    v3 = next(v)
    print (v3)  # 1
    v4 = list(v)
    print (v4)  # [2, 3, 4]
      
    try:
        v5 = next(v)
        print (v5)
    except Exception as e:
        print (e.__class__)
        # <class 'StopIteration'>
    
if __name__ == "__main__":
    # requests_test()
    # xpath_test()
    # pandas_test()
    # page_turn()
    yield_test()
    print ("end")