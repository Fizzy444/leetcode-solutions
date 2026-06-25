class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s = s.lower()
        r = []
        for i in s:
            if i.isalpha() or i.isdigit():
                r.append(i)
        r = "".join(r)
        return r == r[::-1]