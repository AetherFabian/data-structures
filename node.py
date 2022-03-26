#The class Node is used to create a node for the lists
class Node:
    ''' Simple node for linked list '''

    def __init__(self, data):
        self.data = data

#the class ListNode is a subclass of the class Node that has a next attribute
#this not only save data in a blanck space, it save a data in a node an refeers to the next node
class ListNode(Node):
    ''' A Node for singly linked list'''
    def __init__(self,data,next=None):
        super().__init__(data)
        self.next = next

#the class is a structure that contains a constructor and setter that extends from the
#class Node and ListNode them. It new feature is that it has a previous reference
#to the node
class ListDoubleNode(ListNode):
    ''' A Node for double linked list'''
    def __init__(self,data, next=None, prev=None):
        super().__init__(data,next)
        self.prev = prev

#the class extends the Node class to use data as a key and a value to save the data of the node
#and we create a prev as reference of the previous node that will be the top of the stack
class StackNode(Node):
    ''' A Node for stack'''
    def __init__(self,data, prev=None):
        super().__init__(data)
        self.prev = prev

#the class is a structure that contains a constructor and setter that extends from the
#class Node and ListNode them. the dunction of this extend is for use the next reference
#that will be the new front and delete the first element of the queue
class QueueNode(ListNode):
    ''' A Node for queue'''
    def __init__(self,data, next=None):
        super().__init__(data,next)

#The BinarySearchTree class is a structure that contains a constructor and setter that extends from the
#class Node to use the data as a key and a value to save the data of the nodes.
#This class is diferent, because it has a reference of the left and right nodes.
class BinaryTreeNode(Node):
    ''' A Node for binary tree'''
    def __init__(self,data, left=None, right=None):
        super().__init__(data)
        self.left = left
        self.right = right