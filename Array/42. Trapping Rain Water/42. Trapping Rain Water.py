class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        start = 0
        end = len(height) - 1
        leftmax = 0
        rightmax = 0

        water = 0

        while start <= end:
            leftmax = max(leftmax, height[start])
            rightmax = max(rightmax, height[end])

            if leftmax<rightmax:
                water += leftmax - height[start]
                start += 1
            else:
                water += rightmax - height[end]
                end -= 1
        return water