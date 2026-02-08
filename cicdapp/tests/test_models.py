from django.test import TestCase    
from cicdapp.models import student
class StudentModelTestCase(TestCase):

    def test_student_creation(self):
        student_obj = student.objects.create(name="John Doe", marks=90)
        self.assertEqual(student_obj.name, "John Doe")
        self.assertEqual(student_obj.marks, 90)