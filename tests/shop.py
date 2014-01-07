# You will need to create a settings.py file in this same directory
# it's contents should looks like:
# SHOP_SNS_URL_DEBUG = "http://127.0.0.1/shop"
# SHOP_SNS_URL_PRODUCTION = "http://127.0.0.1/shop"


import json
import requests
import settings

from simplejson.scanner import JSONDecodeError


def as_json(resp):
    try:
        return resp.json()
    except JSONDecodeError:
        if len(resp.text) > 0:
            print "\n* [ERROR] json decode error, response content is: "
            print resp.text, '\n'
        else:
            print "\n* [ERROR] Server error, see server log for detail info!\n"


class Shop(object):

    URL = settings.SHOP_SNS_URL_DEBUG


    def __init__(self):
        self.token = ''
        self.uid = ''
        self.mode = "debug"


    def debug(self):
        WineSNSClient.URL = settings.SHOP_SNS_URL_DEBUG
        self.mode = "debug"


    def production(self):
        WineSNSClient.URL = settings.SHOP_SNS_URL_PRODUCTION
        self.mode = "production"

    def search(self, keyword, has_taobao, cid, sid, page_no, page_size, star_price, end_price, sort):
        resp = requests.post(Shop.URL + '/1/goods/search.php',
                            data={'keyword': keyword, 'has_taobao': has_taobao, 'cid':cid,
                                  'sid':sid, 'page_no':page_no, 'page_size':page_size,
                                  'star_price':star_price, 'end_price':end_price, 'sort':sort})
        return as_json(resp)


    def detail(self, iids, urls):
        resp = requests.post(Shop.URL + '/1/goods/detial.php',
                             data={'iids':iids, 'urls':urls})
        return as_json(resp)

    def itemcats(self, cids):
        resp = requests.post(Shop.URL + '/1/goods/itemcats.php',
                             data={'cids':cids})
        return as_json(resp)




        
