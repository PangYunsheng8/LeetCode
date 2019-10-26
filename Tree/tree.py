    class TreeNode(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class Tree(object):
    def __init__(self):
        self.root = None
        self.queue = []

    # 为二叉树逐个添加结点
    def addNode(self, val):
        node = TreeNode(val)
        if self.root == None:
            self.root = node
            self.queue.append(node)
        else:
            point = self.queue[0]
            if point.left == None:
                point.left = node 
                self.queue.append(node)
                return
            elif point.right == None:
                point.right = node
                self.queue.pop(0)
                self.queue.append(node)
                return

    # 前序遍历(递归)
    def pre_order_recursive(self, root, res=[]):
        if not root:
            return 
        res.append(root.val)
        self.pre_order_recursive(root.left,res)
        self.pre_order_recursive(root.right,res)
        return res

    # 前序遍历(迭代)
    def pre_order_iterative(self, root, res=[], stack=[]):
        if not root:
            return
        stack.append(root)
        while stack:
            node = stack.pop()
            res.append(node.val)
            if node.right != None:
                stack.append(node.right)
            if node.left != None:
                stack.append(node.left)
        return res

    # 中序遍历(递归)
    def in_order_recursive(self, root, res=[]):
        if not root:
            return
        self.in_order_recursive(root.left,res)
        res.append(root.val)
        self.in_order_recursive(root.right,res)
        return res

    # 中序遍历(迭代)
    def in_order_iterative(self, root, res=[], stack=[]):
        if not root:
            return
        node = root
        while stack or node:
            while node:
                stack.append(node)
                node=node.left
            node=stack.pop()
            res.append(node.val)
            node=node.right
        return res

    # 后序遍历(递归)
    def post_order_recursive(self, root, res=[]):
        if not root:
            return
        self.post_order_recursive(root.left,res)
        self.post_order_recursive(root.right,res)
        res.append(root.val)
        return res

    # 后序遍历(迭代)
    def post_order_iterative(self, root, res=[], stack=[]):
        stack.append(root)
        while stack:
            node = stack.pop()
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
            res.append(node.val)
        return res[::-1]

    # 层序遍历
    def level_order(self, root, res=[], stack=[]):
        if not root:
            return
        stack.append(root)
        res.append(root.val)    
        while stack != []:
            node = stack.pop(0)
            if node.left != None:
                res.append(node.left.val)
                stack.append(node.left)
            if node.right != None:
                res.append(node.right.val)
                stack.append(node.right)
        return res


if __name__ =='__main__':
    tree = Tree()  # 二叉树类的实例化
    L = [1, 2, 3, 4, 5, 6]
    for i in L:
        tree.addNode(i)
        print('add node ' + str(i))

    res_pre_recu = tree.pre_order_recursive(tree.root)
    print("pre order with recursiving: ", res_pre_recu)

    res_pre_iter = tree.pre_order_iterative(tree.root)
    print("pre order with iterating: ", res_pre_iter)

    res_in_recu = tree.in_order_recursive(tree.root)
    print("pre order with recursiving: ", res_in_recu)

    res_in_iter = tree.in_order_iterative(tree.root)
    print("pre order with iterative: ", res_in_iter)

    res_post_recu = tree.post_order_recursive(tree.root)
    print("post order with recursive: ", res_post_recu)

    res_post_iter = tree.post_order_iterative(tree.root)
    print("post order with iterative: ", res_post_iter)

    res_level = tree.level_order(tree.root)
    print("level order: ", res_level)

