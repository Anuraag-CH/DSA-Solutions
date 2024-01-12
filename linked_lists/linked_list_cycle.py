# https://leetcode.com/problems/linked-list-cycle


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:

        fast = head
        slow = head

        while slow and fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                return True
        
        return False

#Space Complexity: O(1)
#Time Complexity: O(n)