class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1:
            return s
        r = [""] * numRows
        c = 0
        ud = 0
        for i in s:
            r[c] += i
            if c == 0:
                ud = 1
            elif c == numRows - 1:
                ud = -1
            c += ud
        return "".join(r) 