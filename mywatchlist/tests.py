from django.test import TestCase, Client

# Create your tests here.
class Test(TestCase):
    def test_show_mywatchlist_html(self):
        response = Client().get('/mywatchlist/',follow=True)
        self.assertEqual(response.status_code, 200)

    def test_show_mywatchlist_json(self):
        response = Client().get('/mywatchlist/json/',follow=True)
        self.assertEqual(response.status_code, 200)

    def test_show_mywatchlist_xml(self):
        response = Client().get('/mywatchlist/xml/',follow=True)
        self.assertEqual(response.status_code, 200)
