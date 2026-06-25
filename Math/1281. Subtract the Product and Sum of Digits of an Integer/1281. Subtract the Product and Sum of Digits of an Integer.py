class Solution(object):
    def subtractProductAndSum(self, n):
        """
        :type n: int
        :rtype: int
        """
        p = 1
        s = 0
        while n:
            t = n % 10
            p *= t
            s += t
            n //= 10
        return p-s