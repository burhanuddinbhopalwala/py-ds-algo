# Definition for a binary tree node.


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        height_left = self.maxDepth(root.left)
        height_right = self.maxDepth(root.right)
        return 1 + max(height_left, height_right) if root else 0

    def invertTree(self, root):
        if root:
            root.left = self.invertTree(root.right)
            root.right = self.invertTree(root.left)
        return root

    def isSameTree(self, p, q):
        if p is None and q is None:
            return True
        if p is not None and q is not None:
            c1 = p.val == q.val
            c2 = self.isSameTree(p.left, q.left)
            c3 = self.isSameTree(p.right, q.right)
            return c1 and c2 and c3
        return False

    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        res, st = [], [root]
        while st:
            res.append([node.val for node in st])
            st = [child for node in st for child in (
                node.left, node.right) if child]
        return res

    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        return self.inorderTraversal(root.left) + [root.val] + self.inorderTraversal(
            root.right) if root else[]
