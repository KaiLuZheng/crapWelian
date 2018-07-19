#!/usr/local/bin/python3


import sys 
import re
import time

import urllib 
import urllib.request

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

from bs4 import BeautifulSoup as bs

from enum import Enum

class DivClassEvent(Enum):
    Title = 0
    Timerange = 1
    Address = 2
    Sponsor = 3 # 主办 sponsor-wrapper
    Content = 4 

def get_div_classline():
    with open('div.lines', 'r') as f:
        div_class = f.readlines()
    return div_class

def pickContent_soup(func, *argv):
    print(str(func(argv[0], argv[1])))



m_event = [ 'm-event-title-content',
            'm-event-timerange-content',
            'm-event-address-content',
            'm-event-sponsors-content',
            'm-event-detail-content context js-detail'
]

def pickCore(rematch, string):
    return re.findall(rematch, string)

def pickTitle(string):
    return pickCore(r'content">(.*?)<div', str(string[0]))
    pass

def pickTime(string):
    return pickCore(r'content">(.*?)</div', str(string[0]))
    pass

def pickAddress(string):
    return pickCore(r'content">(.*?)</div', str(string[0]))
    pass

def pickSponsors(string):
#    return pickCore(r'<a href=.*?sponsor">(.*?)</a>', string)
    pass

def pickContext(string):
    #return re.findall(r'', string)
    pass

def mainReq(url, headers):
    options = Options()
#    options.add_argument('--headless')
#    options.add_argument('--disable-gpu')

    opener = webdriver.Chrome(chrome_options=options, desired_capabilities=headers)

    opener.implicitly_wait(30)
   
    opener.get(url)

#    time.sleep(1) 
##
    locator = (By.CLASS_NAME, 'm-event-title-content')
    try:
        WebDriverWait(opener, 30, 0.5).until(EC.visibility_of_element_located(locator))
        #print driver.find_element_by_link_text('CSDN').get_attribute('href')
    finally:
        print('successed  ')#, opener.page_source) 
##
    time.sleep(0.5)

    with open('temp.html', 'w') as f:
        f.write(opener.page_source)

    return opener.page_source
  
def exReq_source(html):
    soup = bs(html, 'html.parser')

    div_class = []
    try:
        for i in m_event:
            div_class.append(soup.find_all('div', i)) 
    except Exception as e:
        print('exreq_source: :', e)
    
    funcs = [pickTitle, pickTime, pickAddress, pickSponsors, pickContext]
    for num, i in enumerate(funcs):
        print(funcs[num](div_class[num]))
    

    #event_address = str(soup.find_all('div', 'm-event-title-content')[0])





if __name__ == '__main__':

    url = sys.argv[1] 

    user_agent_='Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'
    headers_ ={'User-Agent':user_agent_
    }

    print(url)       
    html = mainReq(url, headers_)
    exReq_source(html)

'''
    try: 
        exReq_source(mainReq(url, headers_))
    except Exception as e:
        print('main:',e)
    
'''

# ex page
#soup = bs(opener.page_source, 'html.parser')#, from_encoding='utf-8')

#title = str(soup.find_all('div', 'm-event-title-content')[0])
#title = pickContent_soup(soup.find_all, 'div', 'm-event-title-content')

#print(title)





