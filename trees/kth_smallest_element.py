#https://leetcode.com/problems/kth-smallest-element-in-a-bst/

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        res = []

        def inorder(root):
            if not root :
                return 
            
            inorder(root.left)
            res.append(root.val)
            inorder(root.right)
        
        inorder(root)
        return res[k-1]

#space complexity: O(n)
#time complexity: O(n)