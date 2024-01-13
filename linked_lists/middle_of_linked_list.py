# https://leetcode.com/problems/middle-of-the-linked-list/
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:

        slow = head 
        fast = head

        while fast and fast.next :
            fast = fast.next.next
            slow = slow.next
        
        return slow

# Space Complexity : O(1)
# Time Complexity : O(n)