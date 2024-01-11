from django.test import TestCase


class TestUrl(TestCase):
    def test_urlhome(self):
        response=self.client.get('/login/')
        print(response)
        self.assertEqual(response.status_code, 200)


                                                          