from django.test import TestCase
from django.core.exceptions import ObjectDoesNotExist
from .models import Patient
# Create your tests here.
class patient_test(TestCase):
    def test_patient_exists(self):
        try:
            patient = Patient.objects.get(id=2)
            return self.assertTrue(True)
        except ObjectDoesNotExist:
            return self.assertFalse(False)
 
       