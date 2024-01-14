# https://leetcode.com/problems/reverse-linked-list/

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        if head == None or head.next == None:
            return head
        
        prev = None 

        while head :
            temp = head.next
            head.next = prev
            prev = head
            head = temp

        return prev
    
        
        
        
        