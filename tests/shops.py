#coding=utf-8
import unittest

from shop import Shop


class CommentTest(unittest.TestCase):

    def setUp(self):
        self.wc = Shop()

    def test_ads(self):
        ret = self.wc.ads('1001')
        print ret
        


if __name__=='__main__':
    unittest.main()
