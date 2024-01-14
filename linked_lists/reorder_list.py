# https://leetcode.com/problems/reorder-list/
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """

        if head.next == None :
            return head
        
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
        
        first = head
        second = prev
        
        while second.next :
            temp = first.next
            first.next = second
            first = temp

            temp = second.next
            second.next = first
            second = temp
        
        return head
            

        
        
        
