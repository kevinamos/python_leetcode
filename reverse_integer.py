"""
Given a 32-bit signed integer, reverse digits of an integer.

Example 1:

Input: 123
Output: 321
Example 2:

Input: -123
Output: -321
Example 3:

Input: 120
Output: 21
Note:
Assume we are dealing with an environment which could only store 
integers within the 32-bit signed integer range: [−231,  231 − 1]. For 
the purpose of this problem, assume that your function returns 0 when 
the reversed integer overflows."""
import unittest
class Solution(object):
    def reverse(self, x):
        #avoid unnecessary operations because
        #if x (i.e outside +- 2147483647) overflows 
        #the reverse will overflow
        if  x>(pow(2, 31)) or x < -pow(2, 31)+1:
            return 0
        x=str(x)
        slitted_str=x.split('-') 
        if len(slitted_str)>1:
            slitted_str=slitted_str[1]
            rev= int('-'+slitted_str[::-1])
        else:
            rev= int(x[::-1]) 
            
        if  rev>(pow(2, 31)) or rev < -pow(2, 31)+1:
            return 0
        return rev
        
class TestReverse_int(unittest.TestCase):
    "test for reverse method"
    def test_reverse(self):
        s=Solution()
        self.assertEqual(s.reverse(123),321, "incorrect reverse" )   


if __name__=='__main__':
    unittest.main()     