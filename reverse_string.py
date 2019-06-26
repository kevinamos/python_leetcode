import unittest


class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        list_str = [i for i in s.strip().split(' ') if i]
        list_str.reverse()
        return ' '.join(list_str)


class Test_reverse(unittest.TestCase):
    def test_reverse_words(self):
        self.assertEqual(Solution().reverseWords(
            'i am kevin'), 'kevin am i', 'invalid results')

    def test_reverse_words_with_spaces(self):
        self.assertEqual(Solution().reverseWords(
            'i am  kevin   '), 'kevin am i', 'invalid results')


if __name__ == '__main__':
    unittest.main()
