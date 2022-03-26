from node import BinaryTreeNode as Node

class BinarySearchTree:

    def __init__(self):
        self._root = None
        self._size = 0
    '''the function insert given a data, it will insert the data in the tree as a node with
    references of left and right childs, if the data is already in the tree it will not insert it.
    The data will be inserted in the tree depending if the data is smaller or bigger than the current node.
    '''
    def insert(self, data):
        node = Node(data)
        if self._root:
            current = self._root
            while current:
                if node.data > current.data:
                    if current.right:
                        current = current.right
                    else:
                        current.right = node
                        self._size+=1
                        return current.right.data
                else:
                    if current.left:
                        current = current.left
                    else:
                        current.left = node
                        self._size+=1
                        return current.left.data
        else:
            self._root = node
            self._size+=1
            return self._root.data

    '''
    inorder function prints the tree in order of the minour value to the max value.
    It is like a check the most minous value on the left, then I print myself and then check
    the minour value on the right until it's over.
    '''
    def inorder(self, current):
        if current:
            self.inorder(current.left)
            print(current.data, end=' ')
            self.inorder(current.right)

    '''
    preorder function prints first it's self and then it's left child, then it's right child
    '''
    def preorder(self, current):
        if current:
            print(current.data, end=' ')
            self.preorder(current.left)
            self.preorder(current.right)
    '''
    postorder function checks all the tree first the left child, then the right child and for
    the last prints the data of the node.
    '''
    def postorder(self, current):
        if current:
            self.postorder(current.left)
            self.postorder(current.right)
            print(current.data, end=' ')
    '''
    the root function returns the root of the tree if it exists, if not it returns None
    '''
    def root(self):
        if self._root:
            return self._root
        else:
            return None
    '''
    this function returns the size of the tree
    '''
    def size(self):
        return self._size
    '''
    the function min returns the min value of the tree, it goes to the last left child of
    the root and returns the data of the node.
    '''
    def min(self, current):
        while current:
            if current.left:
                current = current.left
            else:
                return current.data
    '''
    the function max returns the max value of the tree, it goes to the last right child of
    the root and returns the data of the node.
    '''
    def max(self, current):
        while current:
            if current.right:
                current = current.right
            else:
                return current
    '''
    the function remove, has 2 parameters, the current node and the data to remove.
    But, not only is it enough to delete the data, but we are going to overwrite it.
    So before removing the node, we check if where is the node, in the left side or in the right side,
    for that we calls back the function remove and overwrite the Node until it is found.
    '''
    def remove(self, current, data):
        if current is None:
            return current

        if data < current.data:
            current.left = self.remove(current.left, data)
        elif data > current.data:
            current.right = self.remove(current.right, data)
        #Once we found the node, before deleting it, we check if it has left or right childs
        #if it doesn't has a left child, the left node of the current node is remplaced by the right node
        #of the current node, and is the same if it doesn't has a right child.
        #If it has a left and right child, we go to the min data child of the right node and we overwrite the node
        #with the min data child of the right node.
        else:
            if current.left is None:
                temp = current.right
                current = None
                self._size -= 1
                return temp

            elif current.right is None:
                temp = current.left
                current = None
                self._size -= 1
                return temp

            current.data = self.min(current.right)
            current.right = self.remove(current.right, current.data)
        return current

    '''
    the function search, has 2 parameters, the current node and the data to search. If the current Node is None,
    it returns False, because doesn't exists any other branch in the tree if the data is equal to the data of
    the current node, it returns True, if the data is smaller than the data of the current node, it calls back the
    function search with the left node, if the data is bigger than the data of the current node, it calls back the
    function search with the right node.
    '''
    def search(self, current, data):
        if current is None:
            return False
        if data == current.data:
            return current.data
        elif data < current.data:
            return self.search(current.left, data)
        else:
            return self.search(current.right, data)