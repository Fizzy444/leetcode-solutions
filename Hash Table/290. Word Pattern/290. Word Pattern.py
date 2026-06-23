class Solution(object):
    def wordPattern(self, pattern, s):
        """
        :type pattern: str
        :type s: str
        :rtype: bool
        """
        d1 = {}
        d2 = {}
        s = s.split()
        if len(s)!=len(pattern):
            return False
        for p,w in zip(pattern,s):
            if p not in d1:
                d1[p] = w
            if w not in d2:
                d2[w] = p
            if d1[p] != w or d2[w] != p:
                return False
        return True