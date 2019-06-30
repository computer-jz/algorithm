# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        cur = root
        node_list = []
        node_stack = []
        while cur or node_stack:
            if cur:
                node_stack.append(cur)
                cur = cur.left
            elif node_stack:
                cur = node_stack.pop()
                node_list.append(cur.val)
                cur = cur.right
        return node_list



