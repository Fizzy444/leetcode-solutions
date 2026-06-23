class Solution(object):
    def checkIfPangram(self, sentence):
        """
        :type sentence: str
        :rtype: bool
        """
        d = {}
        for i in sentence:
            if i not in d:
                d[i] = 1
        return len(d) == 26