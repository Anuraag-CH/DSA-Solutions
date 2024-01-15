# https://leetcode.com/problems/path-sum

class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:

        if root == None :
            return False
        
        if targetSum == root.val and root.left == None and root.right == None :
            return True
        
        return self.hasPathSum(root.left,targetSum-root.val) or self.hasPathSum(root.right,targetSum-root.val)


# Time complexity: O(n)
# Space complexity: O(n)