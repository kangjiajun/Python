import unittest
from People.HuaweiEmployee import *

class HuaweiEmployeeTest(unittest.TestCase):
    def setUp(self):
        self.__employee = HuaweiEmployee("kangjiajun")

    def tearDown(self):
        pass

    def testSetJobId(self):
        self.assertNotEqual(self.__employee.jobId(), "00382525")
        self.__employee.setJobId("00382525")
        self.assertEqual(self.__employee.jobId(), "00382525")


if __name__ == "__main__":
    unittest.main()
