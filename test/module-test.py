import unittest
from mod.module import *


class Tests(unittest.TestCase):

    def test_add(self):
        assert add(3, 4) == 8
