# https://leetcode.com/problems/maximum-twin-sum-of-a-linked-list/
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        
        fast = head
        slow = head

        while fast and fast.next :
            slow = slow.next
            fast = fast.next.next 
        
        prev = None

        while slow :
            temp = slow.next
            slow.next = prev
            prev = slow
            slow = temp
        
        res = float('-inf')

        while prev :
            res = max(res,prev.val+head.val)
            prev = prev.next
            head = head.next
        
        return res

# Space Complexity : O(1)
# Time Complexity : O(n)