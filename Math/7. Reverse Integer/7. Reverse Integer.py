class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        n = True if x < 0 else False
        t = int(str(abs(x))[::-1])
        if n:
            t = -t
        if t < -2**31 or t > 2**31 - 1:
            return 0
        return t