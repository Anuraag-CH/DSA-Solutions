# https://leetcode.com/problems/maximum-depth-of-binary-tree

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:

        if root == None :
            return 0

        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))


#Time complexity: O(n)
#Space complexity: O(n)

