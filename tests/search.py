import unittest

from shop import Shop


class CommentTest(unittest.TestCase):

    def setUp(self):
        self.wc = Shop()

    def test_search(self):
        ret = self.wc.search()
        print ret


if __name__=='__main__':
    unittest.main()
