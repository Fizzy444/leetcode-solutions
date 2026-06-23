# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[Optional[ListNode]]
        :rtype: Optional[ListNode]
        """
        l = []
        for i in lists:
            temp = i
            while temp:
                l.append(temp.val)
                temp = temp.next
        l.sort()
        head = ListNode(0)
        temp = head
        for i in l:
            temp.next = ListNode(i)
            temp = temp.next
        return head.next