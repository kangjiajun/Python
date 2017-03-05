import unittest
from People.HuaweiEmployee import *

class HuaweiEmployeeTest(unittest.TestCase):
    def setUp(self):
        self.__employee = HuaweiEmployee("kangjiajun")

    def tearDown(self):
        pass

    def test_should_set_jobId(self):
        self.assertNotEqual(self.__employee.jobId(), "00382525")
        self.__employee.setJobId("00382525")
        self.assertEqual(self.__employee.jobId(), "00382525")

    def test_should_return_huawei_when_calling_company(self):
        self.assertEqual(self.__employee.company(), "Huawei")

    def test_should_set_name_when_init(self):
        self.assertEqual(self.__employee.name(), "kangjiajun")

if __name__ == "__main__":
    unittest.main()
