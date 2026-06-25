class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        i = 0
        j = 0
        r = []
        while i<len(word1) and j<len(word2):
            r.append(word1[i])
            r.append(word2[j])
            i += 1
            j += 1
        if len(word1) > len(word2):
            r.append(word1[i:])
        else:
            r.append(word2[j:])
        return "".join(r)