# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class FindElements:

    def __init__(self, root: TreeNode):
        self.root = root
        self.elements = set()
        def recover(root):
            if not root: return 
            if root.left: 
                root.left.val = root.val * 2 + 1
                self.elements.add(root.left.val)
                recover(root.left)
            if root.right: 
                root.right.val = root.val * 2 + 2
                self.elements.add(root.right.val)
                recover(root.right)
        root.val = 0
        self.elements.add(root.val)
        recover(root)

    def find(self, target: int) -> bool:
        if target in self.elements: return True
        else: return False
        # def _find(root, target):
        #     if not root: return False
        #     if root.val == target:
        #         return True
        #     if _find(root.left, target): return True
        #     if _find(root.right, target): return True
        #     return False

        # return _find(self.root, target)

# Your FindElements object will be instantiated and called as such:
# obj = FindElements(root)
# param_1 = obj.find(target)