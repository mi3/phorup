from django.test import TestCase

# Create your tests here.
from phorup.models import My_Photo
from phorup.models import My_Gallery


class My_PhotoTestCase(TestCase):
 
    def test_unicode(self):
        expected = " "
        c1 = My_Gallery(name=expected)
        #actual = unicode(c1)
        #self.assertEqual(expected, actual)


