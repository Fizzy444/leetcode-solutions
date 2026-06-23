class Solution(object):
    def reverseOnlyLetters(self, s):
        """
        :type s: str
        :rtype: str
        """
        a = [i for i in s]
        i = 0
        j = len(s)-1
        while i<=j:
            if a[i].isalpha() and a[j].isalpha():
                a[i], a[j] = a[j], a[i]
                i += 1
                j -= 1
            elif a[i].isalpha() and not a[j].isalpha():
                j -= 1
            elif not a[i].isalpha() and a[j].isalpha():
                i += 1
            else:
                i += 1
                j -= 1
        return "".join(a)