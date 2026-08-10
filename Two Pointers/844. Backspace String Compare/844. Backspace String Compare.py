class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        s1 = []
        s2 = []
        for i in s:
            if i == "#":
                if s1:
                    s1.pop()
            else:
                s1.append(i)
        for i in t:
            if i == "#":
                if s2:
                    s2.pop()
            else:
                s2.append(i)
        print(s1)
        print(s2)
        return s1 == s2