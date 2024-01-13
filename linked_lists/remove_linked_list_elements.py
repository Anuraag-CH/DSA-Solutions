# https://leetcode.com/problems/remove-linked-list-elements
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
       
        if head == None :
            return head

        cur = head 

        while cur.next :
            if cur.next.val == val :
                cur.next = cur.next.next
            else:
                cur = cur.next

        
        return head if head.val != val else head.next


#Space Complexity: O(1)
#Time Complexity: O(n)