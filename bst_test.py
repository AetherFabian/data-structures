from bst import BinarySearchTree

if __name__ == '__main__':

    bst = BinarySearchTree()

    bst.insert(10)
    bst.insert(8)
    bst.insert(12)
    bst.insert(5)
    bst.insert(9)
    bst.insert(11)
    bst.insert(15)
    bst.insert(3)
    bst.insert(8)
    bst.insert(10)

    print('Size', bst.size())
    print('Inorder:')
    bst.inorder(bst.root())
    print('\nPreorder:')
    bst.preorder(bst.root())
    print('\nPostorder:')
    bst.postorder(bst.root())
    print()

    bst.remove(bst.root(),12)
    print('Inorder:')
    bst.inorder(bst.root())
    print()
    print(bst.size())
    bst.insert(12)
    print('Inorder:')
    bst.inorder(bst.root())
    print()
    bst.remove(bst.root(),10)
    bst.insert(11)
    print('Inorder:')
    bst.inorder(bst.root())
    print()
    print('root', bst.root().data)
    print(bst.size())
    print('\nPreorder:')
    bst.preorder(bst.root())
    print()

    bst.insert(2)
    print('\nPreorder:')
    bst.preorder(bst.root())
    print()

    bst.remove(bst.root(),3)
    print('\nPreorder:')
    bst.preorder(bst.root())
    print()

'''    if bst.search(bst.root(), 3):
        element = bst.search(bst.root(), 3)
        print(f'{element} exists in the list')
    else:
        print("Element not exists")'''
