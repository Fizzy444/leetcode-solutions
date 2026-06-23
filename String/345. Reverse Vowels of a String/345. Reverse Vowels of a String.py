class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        a = [i for i in s]
        i = 0
        j = len(a)-1
        v = "AEIOUaeiou"
        while i<=j:
            if a[i] in v and a[j] in v:
                a[i], a[j] = a[j], a[i]
                i += 1
                j -= 1
            elif a[i] in v and a[j] not in v:
                j -= 1
            elif a[i] not in v and a[j] in v:
                i += 1
            else:
                i += 1
                j -= 1
        return "".join(a)