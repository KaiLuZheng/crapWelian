#!/usr/local/bin/python3


import sys 
import re

import urllib 
import urllib.request

from urllib import parse

import requests
import json

def mainReq(url, headers):
    pass 


def exJs(json):
    pass


if __name__ == '__main__':
    
    referer = sys.argv[1] 

#    'Referer':'http://h5.welian.com/event/detail/MjY1MzM3NzE0MiYxMjg3MjM=?wltk=0dH5Kfm',

    headers_ ={ 'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36',
                'Cookie':'Hm_lvt_f430a726aa13a0d9a7de431b2ac735c6=1529390251,1529638387,1530077685,1530082720; UM_distinctid=1644406ff6c483-01e0189b3bbbe8-163b6953-13c680-1644406ff6e244; CNZZDATA1255131222=347707702-1530149664-http%253A%252F%252Fh5.welian.com%252F%7C1530149664; Hm_lvt_66766bb5705f8b1d4983f9b1c8d65253=1528373019,1530853028; Hm_lpvt_66766bb5705f8b1d4983f9b1c8d65253=1530853037; Hm_lpvt_f430a726aa13a0d9a7de431b2ac735c6=1531908314; ci_session=hb6imr09grinek729jq4ukq5agibbtf5',
                'Host':'h5.welian.com',
                'Origin':'http://h5.welian.com',
                'deviceId': '1.6.0',
                'Content-Type': 'application/json',
                'Content-Length':'48',
                'Accept':'application/json, text/plain, */*',
                'Referer':referer

    }


    longCode = re.findall(r'detail/(.*?)\?', referer)[0]

# application/json
    data = json.dumps({'uniqueKey': longCode, 'uid':0})
    data = bytes(data, 'utf8')
    req = urllib.request.Request(url='http://h5.welian.com/rest/cloudevent-server/signup/getdetailbykey', headers=headers_)#, data=data)
    rjson = urllib.request.urlopen(req, data=data)

#    data = {'uniqueKey': longCode, 'uid':0}
#    req = requests.post(url='http://h5.welian.com/rest/cloudevent-server/signup/getdetailbykey', data=json.dumps(data), headers=headers_)
#    print(req.text)


    sjson = rjson.read().decode('utf8')

    with open('temp.json', 'w') as f:
        f.write(sjson)

    exjson = json.loads(sjson)
   
    needData = ['title','resultUrl','dateTimeRange','address','sponsors'] 
    contents = []
    for num, i in enumerate(needData):
        contents.append(exjson['data'][needData[num]])

    #contents.append(exjson['data']['title'])
    #contents.append(exjson['data']['resultUrl'])
    #contents.append(exjson['data']['dateTimeRange'])
    #contents.append(exjson['data']['address'])
    #contents.append(exjson['data']['sponsors'])

    filename = contents[0].replace(' ','-')

    with open(filename+'.html', 'w') as f:
        for i in contents:
            if i['name'] is not null:
                for i in exjson['data']['sponsors']:
                    f.write('<p>'+i['name']+'</p>')
            else:
                f.write('<p>'+i+'</p>')
        f.write(exjson['data']['detail'])





