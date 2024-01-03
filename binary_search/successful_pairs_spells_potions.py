# https://leetcode.com/problems/successful-pairs-of-spells-and-potions
class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:    
        potions.sort()
        
        #initialize
        res= []

        #loop 
        for i in spells :

            l = 0
            r = len(potions)-1

            index = len(potions)

            while l <= r :
                mid = (l+r)//2

                if potions[mid]*i >= success :
                    index = min(index,mid)
                    r = mid -1
                else:
                    l = mid + 1
            
            number_of_pairs = len(potions)-index
            res.append(number_of_pairs)
        
        return res



