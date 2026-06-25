class Solution(object):
    def letterCombinations(self, digits):
        if not digits:
            return []

        phone = {
            "2": "abc", "3": "def", "4": "ghi",
            "5": "jkl", "6": "mno", "7": "pqrs",
            "8": "tuv", "9": "wxyz"
        }

        res = [""]

        for digit in digits:
            temp = []
            for combo in res:
                for char in phone[digit]:
                    temp.append(combo + char)
            res = temp

        return res