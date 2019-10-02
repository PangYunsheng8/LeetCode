class TreeNode{
    constructor(left, val, right){
        this.left = left;
        this.val = val;
        this.right = right;
    }
}

let tree = new TreeNode(null, 3, null)

tree.left = new TreeNode(null, 8, null)

tree.right = new TreeNode(null, 9, null)