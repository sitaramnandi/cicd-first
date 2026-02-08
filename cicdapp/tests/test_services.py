from django.test import TestCase
from cicdapp.services import calculate_grade    

class ServicesTestCase(TestCase):

    def test_calculate_grade(self):
        self.assertEqual(calculate_grade(90), 'A')
        self.assertEqual(calculate_grade(75), 'B')
        self.assertEqual(calculate_grade(55), 'C')
        self.assertEqual(calculate_grade(40), 'F')