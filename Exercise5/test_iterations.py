#unit test practice - May 15

import unittest
import iterations

class TestIterations(unittest.TestCase):

    print ("running test file")

    def test_odd(self):
        print("running test code")
        list = [1,2,3,4,5]
        result = iterations.find_odd_numbers(list)
        print(result)
        self.assertEquals(result,3)

    def test_something(self):
        print("Running test")
