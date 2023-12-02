# https://leetcode.com/problems/binary-tree-inorder-traversal


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        self.res = []

    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        self.inorder_traversal(root)

        return self.res

    def inorder_traversal(self, root):
        if root == None:
            return
        self.inorder_traversal(root.left)
        self.res.append(root.val)
        self.inorder_traversal(root.right)
