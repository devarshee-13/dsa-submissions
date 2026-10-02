# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow,fast = head, head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        second_half = slow.next
        slow.next = None
        
        new_curr = None
        
        while second_half:
            temp = second_half.next
            second_half.next = new_curr
            new_curr =second_half
            second_half = temp
        
        curr = head

        while new_curr:
            temp = curr.next
            temp2 = new_curr.next
            curr.next = new_curr
            new_curr.next = temp
            curr = temp
            new_curr = temp2
