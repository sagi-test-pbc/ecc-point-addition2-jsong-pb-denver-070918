from unittest import TestCase
from ipynb.fs.full.index import *

class PointTest(TestCase):

    def test_add2(self):
        a = Point(x=-1, y=1, a=5, b=7)
        self.assertEqual(a+a, Point(x=18, y=-77, a=5, b=7))