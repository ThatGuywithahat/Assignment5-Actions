import unittest
import task
import math


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


if __name__ == '__main__':
    unittest.main()
