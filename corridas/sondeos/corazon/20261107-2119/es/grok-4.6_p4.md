def inorderTraversal(root):
    result = []
    def inorder(node):
        if node is not None:
            inorder(node.left)
            result.append(node.val)
            inorder(node.right)
    inorder(root)
    return result