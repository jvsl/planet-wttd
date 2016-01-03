from time import struct_time
from django.test import TestCase
from feedparser import parse
from planet_wttd.util.status_code import Status


class FeedTest(TestCase):

    @classmethod
    def setUpClass(self):
        self.rss = parse('http://pythonclub.com.br/feeds/all.atom.xml')

    def test_feed__get_feed___status200(self):
        self.assertEqual(Status.status_200_ok, self.rss['status'])

    def test_feed__title_not_empty__true(self):
        self.assertTrue(self.rss['feed']['title'] is not '')

    def test_feed__last_updated_time__object_struct_time(self):
        self.assertIsInstance(self.rss['updated_parsed'], struct_time)

    @classmethod
    def tearDownClass(self):
        pass
