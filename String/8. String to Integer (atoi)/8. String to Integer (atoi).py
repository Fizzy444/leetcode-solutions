class Solution(object):
    def myAtoi(self, s):
        s = s.lstrip()
        if not s:
            return 0

        i = 0
        sign = 1
        n = len(s)

        if s[i] == '+' or s[i] == '-':
            if s[i] == '-':
                sign = -1
            i += 1

        num = 0
        INT_MAX = 2**31 - 1
        INT_MIN = -2**31

        while i < n and s[i].isdigit():
            digit = int(s[i])

            if num > (INT_MAX - digit) // 10:
                return INT_MAX if sign == 1 else INT_MIN

            num = num * 10 + digit
            i += 1

        return sign * num