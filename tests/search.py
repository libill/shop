#coding=utf-8
import unittest

from shop import Shop


class CommentTest(unittest.TestCase):

    def setUp(self):
        self.wc = Shop()

    def test_search(self):
        ret = self.wc.search('大衣', '1', '0', '0', '1', '40', '', '', '')
        print ret


if __name__=='__main__':
    unittest.main()
