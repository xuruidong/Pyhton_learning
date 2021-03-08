import random

def random_test():
    print (random.random())
    print (random.random())
    
    print (random.randrange(0, 100, 2))
    print (random.randrange(0, 100, 2))
    
    print (random.choice(["qq", "ww", "ee"]))
    print (random.choice(["qq", "ww", "ee"]))
    
    print (random.sample(["qq", "ww", "ee"], 2))
    print (random.sample(["qq", "ww", "ee"], 2))
    
    
import pathlib
def pathlib_test():
    p = pathlib.Path()
    print (p.resolve())
    
    testpath = 'C:/Users/Public/basic.py.bak'
    p = pathlib.Path(testpath)
    print (p.name)
    print (p.stem)
    print (p.suffix)
    print (p.suffixes)
    print (p.parent)
    for pa in p.parents:
        print (pa)
    
    print(p.parts)
    
import os
def ospath_test():
    print (os.path.abspath('basic.py'))
    testpath = 'C:/Users/Public/basic.py.bak'
    print (os.path.basename(testpath))
    print (os.path.dirname(testpath))
    print (os.path.exists(testpath))
    print (os.path.isfile(testpath))
    print (os.path.isdir(testpath))
    print (os.path.join('a/b', 'c/d'))
    

import re
def re_test():
    content = '13311112222'
    print(re.match('.{11}', content))
    print(re.match('.{12}', content))
    print(re.match('.{7}', content).group())
    print(re.match('.{7}', content).span())
    
    email = '123@456.com'
    print (re.match('.*@.*com', email))
    
    print (re.match('(.*)@(.*)com', email).group(1))
    print (re.match('(.*)@(.*).com', email).group(2))
    
    print (re.search('@', email))
    print (re.findall('123', '123@1234.com'))
    
    print (re.sub('123', 'abc', '123@1234.com'))
    print (re.sub('\d', 'a', '123@1234.com'))
    
    print (re.split('@', email))
    print (re.split('(@)', email))
    
import daemon

if __name__ == "__main__":
    re_test()
