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

    def search(self):
        resp = requests.get(Shop.URL + '/1/search.php')
        return as_json(resp)
