# #!/usr/bin/python3
# """Defines unittests for base.py.

# Unittest classes:
#     TestBase_instantiation
# """

import unittest
from models.base import Base

class TestBaseInstance(unittest.TestCase):
    def test_no_args(self):
        b1 = Base()
        b2 = Base()
        self.assertEqual(b1.id, b2.id - 1)

    def test_three_instances(self):
        b1 = Base()
        b2 = Base()
        b3 = Base()
        self.assertEqual(b1.id, b3.id - 2)

    def test_arguments(self):
        b1 = Base()
        b2 = Base()
        b3 = Base()
        b4 = Base(12)
        b5 = Base()
        self.assertEqual(b3.id, b5.id - 1)

    def test_unique_id(self):
        b1 = Base(12)
        self.assertEqual(b1.id, 12)
