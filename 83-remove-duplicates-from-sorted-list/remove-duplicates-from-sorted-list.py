
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head # temp head
        while curr and curr.next: # while curr and curr.next are true
            if curr.val == curr.next.val: # if the values are equal
                curr.next = curr.next.next # set the next pointer to the next node
            else:
                curr = curr.next # if not equal, move to the next
        return head
