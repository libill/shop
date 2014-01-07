#coding=utf-8
import unittest

from shop import Shop


class CommentTest(unittest.TestCase):

    def setUp(self):
        self.wc = Shop()

    def test_search(self):
        #ret = self.wc.search('大衣 男', '1', '0', '0', '1', '1', '', '', '')
        #print ret
        print 1

    def test_detail(self):
        #ret = self.wc.detail('10218381', '')
        #print ret
        print 2

    def test_itemcats(self):
        ret = self.wc.itemcats('20')
        print ret
        


if __name__=='__main__':
    unittest.main()
