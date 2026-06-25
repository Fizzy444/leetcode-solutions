class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        m = 0
        i = 0
        j = len(height) - 1
        while i < j:
            t = height[i] if height[i] < height[j] else height [j]
            d = j - i
            m = max(m, t*d)
            if height [i] < height[j]:
                i += 1
            else:
                j -= 1
        return m