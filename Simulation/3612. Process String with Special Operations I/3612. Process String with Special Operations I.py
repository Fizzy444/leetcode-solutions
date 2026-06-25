class Solution(object):
    def processStr(self, s):
        """
        :type s: str
        :rtype: str
        """
        r = []
        for i in s:
            if i.isalpha():
                r.append(i)
            elif i == '#':
                r = r * 2
            elif i == '%':
                r = r[::-1]
            elif i == '*':
                if r:
                    r.pop()
        return "".join(r)