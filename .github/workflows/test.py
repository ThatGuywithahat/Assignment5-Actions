import unittest
import task
import math
import datetime


class TestCase(unittest.TestCase):

    def test1(self):
        expected = "success"
        self.assertEqual(expected, task.firstrun())

    def test2(self):
        expected = "failure"
        self.assertNotEqual(expected, task.firstrun())

    def test_radius(self):
        C = 60
        expected = C / (2 * math.pi)
        self.assertEqual(expected, task.radius(C))

    def test_list(self):
        list = [1, 2, 3]
        expected = "First:1 Last:3"
        self.assertEqual(expected, task.getlist(list))

    def test_date(self):
       date1 = datetime.datetime(2020,5,15)
       date2 = datetime.datetime(2020, 5, 13)
       expected = datetime.timedelta(days=2)
       self.assertEqual(expected, task.getdate(date1,date2))


if __name__ == '__main__':
    unittest.main()
