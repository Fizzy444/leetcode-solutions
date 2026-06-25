class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        n = int(a,2)
        m = int(b,2)
        return bin(m+n)[2:]