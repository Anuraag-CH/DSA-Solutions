# https://leetcode.com/problems/binary-tree-preorder-traversal


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        self.res = []

    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        self.preorder_traversal(root)

        return self.res

    def preorder_traversal(self, root):
        if root == None:
            return
        self.res.append(root.val)
        self.preorder_traversal(root.left)
        self.preorder_traversal(root.right)
