class Solution:
    def validPalindrome(self, s: str) -> bool:

        l = 0
        r = len(s) -1 

        while l <=r :
            if s[l] != s[r] :
                break
            l += 1
            r -= 1
        
        l_new = l+1
        r_new = r-1

        while l_new <= r :
            if s[l_new] != s[r]:
                break
            l_new += 1
            r -= 1
        
        if l_new >= r :
            return True
        
        while l <= r_new :
            if s[l] != s[r_new] :
                return False
            
            l += 1
            r_new -= 1
        
        return True

#Space complexity: O(1)
#Time complexity: O(n)
