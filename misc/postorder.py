# https://leetcode.com/problems/binary-tree-postorder-traversal


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        self.res = []

    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        self.postorder_traversal(root)

        return self.res

    def postorder_traversal(self, root):
        if root == None:
            return
        self.postorder_traversal(root.left)
        self.postorder_traversal(root.right)
        self.res.append(root.val)
