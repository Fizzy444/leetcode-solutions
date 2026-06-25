class Solution(object):
    def removeStars(self, s):
        """
        :type s: str
        :rtype: str
        """
        r = []
        for i in s:
            if i == '*':
                r.pop()
            else:
                r.append(i)
        return "".join(r)