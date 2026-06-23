class Solution(object):
    def mostWordsFound(self, sentences):
        """
        :type sentences: List[str]
        :rtype: int
        """
        m = 0
        for i in sentences:
            m = max(m,len(i.split()))
        return m