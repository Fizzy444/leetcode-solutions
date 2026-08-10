class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        s1=[]
        a=[]
        for i in s:
            if s1 and i=='#':
                s1.pop()
            elif i!='#':
                s1.append(i)
        for j in t:
            if a and j=='#':
                a.pop()
            elif j!='#':
                a.append(j)
        return s1==a