import sys
import traceback
#import pretty_errors

def exc_func():
    1 / 0

def traceback_test():
    try:
        exc_func()
    except:
        e_type, e_value, tb_obj = sys.exc_info()
        print(e_type, e_value, tb_obj)
        print ("===========")
        traceback.print_tb(tb_obj, 2, sys.stdout)
        print ("=====  print_exception  ======")
        traceback.print_exception(e_type, e_value, tb_obj, 3, sys.stdout)
        print ("=====  print_exc  ======")
        traceback.print_exc()
        print ("=====  format_exc  ======")
        print (traceback.format_exc())

class MyException(Exception):
    def __init__(self, ErrorInfo):
        super().__init__(self, ErrorInfo)
        self.errorinfo = ErrorInfo

    def __str__(self):
        return self.errorinfo

def my_exc_test():
    try:
        raise MyException("What are you doing?")
    except Exception as e:
        #print (e)
        traceback.print_exc()

class c_a(object):
    def __init__(self):
        1 / 0
        pass

    def call(self):
        print("call a.call()")

    def exc(self):
        print ("raise a exception")
        #1 / 0

class ctx_mag:
    def __enter__(self):
        print ("enter")
        a = c_a()
        #1 / 0
        
        return a
        
    def __exit__(self, exc_type, exc_value, traceback):
        print ("exit")

    def __call__(self):
        print ("run call")
        pass

def ctx_test():
    with ctx_mag() as ctx:
        ctx.call()
        ctx.exc()    


import pymysql
class connDB(object):
    def __init__(self, db_info, sqls):
        self.host = db_info["host"]
        self.port = db_info["port"]
        self.user = db_info["user"]
        self.password = db_info["password"]
        self.db = db_info["db"]
        self.sqls = sqls

    def run(self):
        conn = pymysql.connect(host=self.host, port=self.port,
                               user=self.user, password=self.password, db=self.db)
        cur = conn.cursor()

        try:
            for command in self.sqls:
                cur.execute(command)
                result.append(cur.fetchone())

            cur.close()
            conn.commit()
        except:
            conn.rollback()
        conn.close()
        
                
def pymysql_test():
    pass


from fake_useragent import UserAgent
def useragent_test():
    ua = UserAgent(verify_ssl=False)
    print ("=================")
    print (f"chrome:{ua.chrome}")
    print (dir(ua))
    print (ua.random)
    
import requests
def http_post_test():
    r = requests.post("http://httpbin.org/post", data={"key": "value"})
    print(r.json())

import time
def cookies_test():
    s = requests.Session()
    # r = s.get('http://httpbin.org/cookies/set/cookies/123457',
    #          allow_redirects=False)
    r = s.get("https://httpbin.org/cookies/set?freeform=fffff")
    #print (r.text)
    #print (r.headers)
    #print (r.status_code)
    #print (dir(r))
    r = s.get("http://httpbin.org/cookies")
    print (r.text)
    print (r.status_code)


from selenium import webdriver
from selenium.webdriver.common.keys import Keys
def webdriver_test():
    edge = webdriver.Edge("msedgedriver.exe")
    edge.get("http://www.baidu.com")
    print (edge.title)
    #elem = edge.find_element_by_id("kw")
    #elem.send_keys('seleniumhq' + Keys.RETURN)
    
    #elem = edge.find_element_by_xpath('//*[@id="kw"]')
    # elem = edge.find_element_by_link_text()  ????
    # elem = edge.find_element_by_name('wd')
    # elem = edge.find_element_by_tag_name()  ???
    
    elem.send_keys('seleniumhq')
    

def big_file_download(url):
    r = requests.get(url, stream=True)
    with open("download", "wb") as f:
        for chunk in r.iter_content(chunk_size=1024):
            f.write(chunk)
            

def classmethod_test():
    class A(object):
        def __init__(self, arg):
            print ("in __init__, arg=%s" % arg)
            self.name = arg

        def age(self):
            print("age=18")
            return 18
        
        @classmethod
        def callme(cls, who):
            print("who am I?")
            print (who)
            cls.age(cls)
            
            return cls(who)

        def getname(self):
            return self.name

    a = A.callme("nb")
    print (a.getname())

from PIL import Image
import pytesseract
def tesseract_test():
    
    im = Image.open('img_test.jpg')
    im.show()
    
    gray = im.convert('L')
    gray.save('c_gray.jpg')
    im.close()
    
    threshold = 100
    table = []

    for i in range(256):
        if i < threshold:
            table.append(0)
        else:
            table.append(1)

    out = gray.point(table, '1')
    out.save('c_th.jpg')
    
    th = Image.open('c_th.jpg')
    print(pytesseract.image_to_string(th, lang='eng'))
    

    
if __name__ == "__main__":
    # traceback_test()
    # my_exc_test()
    # ctx_test()
    # c = ctx_mag()
    # c()
    # useragent_test()
    # http_post_test()
    # cookies_test()
    # webdriver_test()
    #big_file_download(
    #    "https://msedgedriver.azureedge.net/84.0.522.49/edgedriver_win64.zip")
    # classmethod_test()
    tesseract_test()
    print ("===== end ====")
