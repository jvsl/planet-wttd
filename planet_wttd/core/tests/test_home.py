from django.test import TestCase
from planet_wttd.util.status_code import Status


class HomeTest(TestCase):

    def setUp(self):
        self.resp = self.client.get('/')

    def test_home__get__status200(self):
        self.assertEqual(self.resp.status_code, Status.status_200_ok)

    def test_home__get__status404(self):
        # arrange
        invalid_url = '/lol'
        # act
        resp = self.client.get(invalid_url)
        # assert
        self.assertEqual(resp.status_code, Status.status_404_not_found)

    def test_home__template__index(self):
        self.assertTemplateUsed(self.resp, 'index.html')