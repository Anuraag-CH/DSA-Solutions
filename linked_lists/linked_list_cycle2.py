# https://leetcode.com/problems/linked-list-cycle-ii/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        slow = head
        fast = head
        slow2 = head

        while fast and fast.next :
            fast = fast.next.next
            slow = slow.next

            if fast == slow :
                break
        if not fast or not fast.next:
            return None
        
        while slow != slow2 :
            slow = slow.next
            slow2 = slow2.next
        return slow
    