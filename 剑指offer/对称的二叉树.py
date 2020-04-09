class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if not root: return True
        
        def recu(t1, t2):
            if not t1 and not t2: return True
            if not t1 or not t2 or t1.val != t2.val: return False
            return recu(t1.left, t2.right) and recu(t1.right, t2.left)

        return recu(root.left, root.right)