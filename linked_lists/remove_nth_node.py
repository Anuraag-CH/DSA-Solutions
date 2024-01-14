# https://leetcode.com/problems/remove-nth-node-from-end-of-list

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        len_list = 0    
        
        cur = head

        while cur :
            len_list += 1
            cur = cur.next
        
        index = len_list - n

        if index == 0 :
            return head.next
        
        cur = head

        while index > 1 :
            cur = cur.next
            index -= 1
        
        cur.next = cur.next.next

        return head

# Time Complexity : O(n)
# Space Complexity : O(1)