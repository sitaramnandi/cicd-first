from django.test import TestCase

class HomeViewTest(TestCase):
    def test_home_page(self):
        response = self.client.get('/students/')
        self.assertEqual(response.status_code, 200)
