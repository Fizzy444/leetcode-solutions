class Solution(object):
    def minimumCost(self, cost1, cost2, costBoth, need1, need2):
        """
        :type cost1: int
        :type cost2: int
        :type costBoth: int
        :type need1: int
        :type need2: int
        :rtype: int
        """
        check1 = max(need1, need2) * costBoth

        check2 = need1 * cost1 + need2 * cost2

        common = min(need1, need2)

        check3 = ((common * costBoth) + ((need1 - common) * cost1) + ((need2 - common) * cost2))

        return min(check1, check2, check3)