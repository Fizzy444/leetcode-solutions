class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        w = s.split()[::-1]
        return " ".join(w)