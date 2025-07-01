class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None
    
    def insert(self, value):
        if self.root is None:
            self.root = TreeNode(value)
        else:
            self._insert_recursive(self.root, value)
    
    def _insert_recursive(self, node, value):
        if value < node.value:
            if node.left is None:
                node.left = TreeNode(value)
            else:
                self._insert_recursive(node.left, value)
        elif value > node.value:
            if node.right is None:
                node.right = TreeNode(value)
            else:
                self._insert_recursive(node.right, value)
    
    def search(self, value):
        return self._search_recursive(self.root, value)
    
    def _search_recursive(self, node, value):
        if node is None:
            return False
        if node.value == value:
            return True
        elif value < node.value:
            return self._search_recursive(node.left, value)
        else:
            return self._search_recursive(node.right, value)
    
    def bfs(self):
        if self.root is None:
            return []
        
        queue = [self.root]
        result = []
        
        while queue:
            current = queue.pop(0)
            result.append(current.value)
            
            if current.left:
                queue.append(current.left)
            if current.right:
                queue.append(current.right)
        
        return result
    
    def preorder(self):
        return self._preorder_recursive(self.root, [])
    
    def _preorder_recursive(self, node, result):
        if node:
            result.append(node.value)
            self._preorder_recursive(node.left, result)
            self._preorder_recursive(node.right, result)
        return result
    
    def inorder(self):
        return self._inorder_recursive(self.root, [])
    
    def _inorder_recursive(self, node, result):
        if node:
            self._inorder_recursive(node.left, result)
            result.append(node.value)
            self._inorder_recursive(node.right, result)
        return result
    
    def postorder(self):
        return self._postorder_recursive(self.root, [])
    
    def _postorder_recursive(self, node, result):
        if node:
            self._postorder_recursive(node.left, result)
            self._postorder_recursive(node.right, result)
            result.append(node.value)
        return result


class AVLNode(TreeNode):
    def __init__(self, value):
        super().__init__(value)
        self.height = 1


class AVLTree(BinaryTree):
    def insert(self, value):
        self.root = self._insert_recursive(self.root, value)
    
    def _insert_recursive(self, node, value):
        if node is None:
            return AVLNode(value)
        if value < node.value:
            node.left = self._insert_recursive(node.left, value)
        elif value > node.value:
            node.right = self._insert_recursive(node.right, value)
        else:
            return node 
        node.height = 1 + max(self._get_height(node.left), 
                             self._get_height(node.right))
        return self._rebalance(node)
    
    def _get_height(self, node):
        if node is None:
            return 0
        return node.height
    
    def _get_balance(self, node):
        if node is None:
            return 0
        return self._get_height(node.left) - self._get_height(node.right)
    
    def _left_rotate(self, z):
        y = z.right
        T2 = y.left
        y.left = z
        z.right = T2
        z.height = 1 + max(self._get_height(z.left), 
                          self._get_height(z.right))
        y.height = 1 + max(self._get_height(y.left), 
                          self._get_height(y.right))
        return y
    
    def _right_rotate(self, z):
        y = z.left
        T3 = y.right
        y.right = z
        z.left = T3
        z.height = 1 + max(self._get_height(z.left), 
                          self._get_height(z.right))
        y.height = 1 + max(self._get_height(y.left), 
                          self._get_height(y.right))
        return y
    
    def _rebalance(self, node):
        balance = self._get_balance(node)
        if balance > 1 and self._get_balance(node.left) >= 0:
            return self._right_rotate(node)
        if balance < -1 and self._get_balance(node.right) <= 0:
            return self._left_rotate(node)
        if balance > 1 and self._get_balance(node.left) < 0:
            node.left = self._left_rotate(node.left)
            return self._right_rotate(node)
        if balance < -1 and self._get_balance(node.right) > 0:
            node.right = self._right_rotate(node.right)
            return self._left_rotate(node)
        return node

if __name__ == "__main__":
    print("Binary Tree Example:")
    bt = BinaryTree()
    for num in [5, 3, 7, 2, 4, 6, 8]:
        bt.insert(num)
    
    print(bt.bfs())
    print(bt.preorder())
    print(bt.inorder())
    print(bt.postorder())
    
    print("\nAVL Tree Example:")
    avl = AVLTree()
    for num in [10, 20, 30, 40, 50, 25]:
        avl.insert(num)
    
    print(avl.bfs())
    print(avl.inorder())