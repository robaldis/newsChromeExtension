import unittest
import os
import sys

sys.path.insert(0,os.getcwd())

from src.rss.process_article import *

class TestWebScrapping(unittest.TestCase):
    def test_urlToStringReturnStringBBC(self):
        # test if a string is returned BBC 
        res = article_to_string("https://www.bbc.co.uk/news/uk-england-bristol-55173667")
        self.assertEqual(type(res), str)

    def test_urlToStringReturnStringSKY(self):
        # test if a string is returned for sky website
        res = article_to_string("https://news.sky.com/story/brexit-significant-progress-in-talks-over-fishing-rights-during-trade-negotiations-eu-sources-12153801")
        self.assertEqual(type(res), str)

    def test_urlToStringWrongUrl(self):
        res = article_to_string("not a url")
        self.assertEqual(res, "404")


if __name__ == "__main__":
    unittest.main()
