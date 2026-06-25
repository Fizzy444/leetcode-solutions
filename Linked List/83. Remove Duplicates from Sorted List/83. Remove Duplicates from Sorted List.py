# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if head is None:
            return head
        temp = head
        l = []
        while temp:
            if temp.val not in l:
                l.append(temp.val)
            temp = temp.next
        res = ListNode(0)
        dummy = res
        l.sort()
        for i in l:
            dummy.next = ListNode(i)
            dummy = dummy.next
        return res.next