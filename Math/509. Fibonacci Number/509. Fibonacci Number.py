class Solution(object):
    def fib(self, n):
        """
        :type n: int
        :rtype: int
        """
        a = 0
        b = 1
        for i in range(n):
            t = a + b
            b = a
            a = t
        return a