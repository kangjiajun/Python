import unittest
from Utils import Const

class ConstTest(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_should_set_and_get_attr_when_given_value_for_the_first_time(self):
        Const.numA = 2
        self.assertEqual(Const.numA, 2)
        del Const.numA

    def test_should_return_None_when_trying_to_get_uninitialized_attr(self):
        self.assertEqual(Const.numA, None)

    def test_should_raise_ConstError_when_trying_to_change_value(self):
        Const.numA = 2
        with self.assertRaises(TypeError):
            Const.numA = 3
        del Const.numA

if "__main__" == __name__:
    unittest.main()
