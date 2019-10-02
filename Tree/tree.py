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
            while True:
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
        self.pre_order_recursive(root.left,res)
        res.append(root.val)
        self.pre_order_recursive(root.right,res)
        return res

    # 中序遍历(迭代)
    def in_order_iterative(self, root, res=[]):
        if not root:
            return
        self.pre_order_recursive(root.left,res)
        res.append(root.val)
        self.pre_order_recursive(root.right,res)
        return res


if __name__ =='__main__':
    tree = Tree()  # 二叉树类的实例化
    L = [1, 2, 3, 4, 5, 6]
    for i in L:
        tree.addNode(i)
        print('add node ' + str(i))

    res_pre_recu = tree.pre_order_recursive(tree.root)
    print(res_pre_recu)

    res_pre_iter = tree.pre_order_iterative(tree.root)
    print(res_pre_iter)

    in_pre_recu = tree.in_order_recursive(tree.root)
    print(in_pre_recu)

    in_pre_iter = tree.in_order_iterative(tree.root)
    print(in_pre_iter)