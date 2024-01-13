# https://leetcode.com/problems/merge-two-sorted-lists

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        res= ListNode()
        tail = res
        while list1 !=None and list2 != None :

            if list1.val > list2.val :
                temp = list2
                list2 = list2.next
                temp.next = None
                tail.next = temp
                tail = tail.next
            
            else :
                temp = list1
                list1 = list1.next
                temp.next = None
                tail.next = temp
                tail = tail.next
        
        if list1:
            tail.next = list1
        
        if list2:
            tail.next = list2
        
        return res.next
            

        
#Space Complexity: O(1)
#Time Complexity: O(n)