class Solution(object):
    def findContentChildren(self, g, s):
        """
        :type g: List[int]
        :type s: List[int]
        :rtype: int
        """
        cookie = len(s)
        if cookie == 0:
            return 0

        g.sort()
        s.sort()

        cookie = cookie - 1
        child = len(g) - 1
        c = 0
        while cookie >= 0 and child >= 0:
            if s[cookie] >= g[child]:
                c += 1
                cookie -= 1
                child -= 1
            else:
                child -= 1
        return c