class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        if n == 0:
            return [""]

        result = []

        for i in range(n):
            left_parts = self.generateParenthesis(i)
            right_parts = self.generateParenthesis(n - 1 - i)

            for left in left_parts:
                for right in right_parts:
                    result.append("(" + left + ")" + right)

        return result