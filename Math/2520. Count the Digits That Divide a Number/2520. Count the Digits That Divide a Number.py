class Solution(object):
    def countDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        c = 0
        t = str(num)
        for i in t:
            if num % int(i) == 0:
                c += 1
        return c