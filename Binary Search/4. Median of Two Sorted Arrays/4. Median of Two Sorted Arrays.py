class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        r = sorted(nums1+nums2)
        l = len(r)
        if l%2==0:
            return (float(r[l//2] + r[l//2-1]) / 2)
        else:
            return float(r[l//2])