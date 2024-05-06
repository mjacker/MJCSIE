
# class Solution:
# def twoSum(self, nums: List[int], target: int) -> List[int]:

import unittest

class TestSum(unittest.TestCase):
        # test cases?

    def test_sum(self):
        nums = [2,7,11,15]
        a = 0
        b = 1
        target = 9
        result = nums[a] + nums[b]
        self.assertEqual(result, target)
    
    def test_sum2(self):
        nums = (2,7,11,15)
        a = 0
        b = 1
        target = 9
        result = nums[a] + nums[b]
        self.assertEqual(result, target)


#    def main():
#        print("programa principal cargado.")

if __name__ == '__main__':
    # test_sum(0, 1)
    unittest
    unittest.main()
