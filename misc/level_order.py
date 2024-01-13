class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        from collections import deque 

        if not root:
            return []
        
        queue = deque()

        queue.append(root)
        result = []

        while queue:
            level = []
            for i in range(len(queue)):
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                level.append(node.val)
            result.append(level)
        
        return result
            
