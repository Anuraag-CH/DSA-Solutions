# https://leetcode.com/problems/find-the-town-judge

import List


class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:

        #trust someone not a judge

        l = set()

        for i in trust :
            l.add(i[0])
        
        res = []

        for i in range(1,n+1):
            if i not in l :
                res.append(i)
        
        if len(res) !=1 :
            return -1
        
        count = 0
        for i in trust :
            if res[0] == i[1] :
                count+=1
        
        return res[0] if count == n-1 else -1

# Time Complexity : O(n)
# Space Complexity : O(n)