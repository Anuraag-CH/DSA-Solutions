# https://leetcode.com/problems/subtree-of-another-tree/

class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        if self.isSameTree(root,subRoot) :
            return True
        
        left = self.isSubtree(root.left,subRoot) if root.left else False
        right = self.isSubtree(root.right,subRoot) if root.right else False

        return left or right
    
    def isSameTree(self, root,subRoot):

        if not root and not subRoot :
            return True
        
        root_val = root.val if root else None
        subRoot_val = subRoot.val if subRoot else None

        if root_val != subRoot_val :
            return False
        
        return self.isSameTree(root.left,subRoot.left) and self.isSameTree(root.right,subRoot.right)


# Time complexity: O(n*m)
# Space complexity: O(n)