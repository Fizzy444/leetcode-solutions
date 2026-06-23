class Solution(object):
    def calPoints(self, operations):
        """
        :type operations: List[str]
        :rtype: int
        """
        s = []
        for i in operations:
            if i not in "+DC":
                s.append(int(i))
            elif i == "+":
                s.append(s[-1]+s[-2])
            elif i == "D":
                s.append(s[-1]*2)
            elif i == "C":
                s.pop()

        return sum(s)