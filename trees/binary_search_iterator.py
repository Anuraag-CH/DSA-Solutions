# https://leetcode.com/problems/binary-search-tree-iterator

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.res = []
        self.in_order(root)
        

    def next(self) -> int:
        return self.res.pop()
        

    def hasNext(self) -> bool:
        if self.res :
            return True
    

    def in_order(self,root) :
        if not root :
            return 
        
        self.in_order(root.left)
        self.res.insert(0,root.val)
        self.in_order(root.right)

        

# Time Complexity: O(n)
# Space Complexity: O(n)

