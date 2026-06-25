class Solution(object):
    def largestAltitude(self, gain):
        """
        :type gain: List[int]
        :rtype: int
        """
        m = 0
        alt = 0
        for i in gain:
            alt += i
            m = max(m, alt)
        return m