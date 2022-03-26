class Node:
    ''' Simple node for linked list '''

    def __init__(self, data):
        self.data = data

class QueueNode(Node):
    ''' A Node for queue'''
    def __init__(self,data, next=None):
        super().__init__(data)
        self.next = next

class Structure:
    ''' Standard Sturcture for data structures'''
    def __init__(self):
        self._front = None
        self._tail = None
        self._size = 0

    def size(self):
        return self._size

    def front(self):
        return self._front.data

    def back(self):
        if self._tail:
            return self._tail.data
        else:
            return None

    def empty(self):
        if self._size == 0:
            return True
        else:
            return False

    def clear(self):
        self._front = None
        self._tail = None
        self._size = 0

    def iter(self):
        current = self._front

        while current:
            data = current.data
            current = current.next
            yield data

class Queue(Structure):

    def __init__(self):
        super().__init__()

    def push_back(self, data):
        '''Inserts a new element at the endo fo the queue'''
        node = QueueNode(data)

        #if the tail is None it means that the queue is empty and
        #this piece of code make the first element of the list
        if self._tail == None:
            self._front = node
            self._tail = node
        #if the tail is not None it means that the queue is not empty
        #and this piece of code make the last element of the list
        #so assign the tail to a new node and assign the new node waiting to be used
        else:
            self._tail.next = node
            self._tail = node

        self._size += 1

    #this piece of code is used for removes elements, as we know, the queue only
    #removes the first node that was inserted in the queue, so we pop the front only
    def pop_front(self):
        '''Removes the first element of the queue'''
        current = self._front
        if current.next == None:
            self._front = None
            self._tail = None
        else:
            self._front = current.next
            current.next = None

        self._size -= 1

    def search(self, data):
        '''Search for a node with the given data'''
        current = self._front
        while current:
            if current.data == data:
                return True
            current = current.next
        return False

def _main(consults):
    q = Queue()

    for i in range(consults):
        n = input()

        if n == "1":
            cons = input()
            if q.search(cons):
                print(f"ERROR LA DIMENSION YA A SIDO AGREGADA")
            else:
                q.push_back(cons)
        elif n == "2":
            if q.empty():
                print("-1")
            else:
                print(f"VIAJANDO A {q.front()}")
                q.pop_front()
        elif n == "3":
            if q.empty():
                print("-1")
            else:
                print(q.front())
        elif n == "4":
            if q.empty():
                print("-1")
            else:
                print(q.back())
        elif n == "5":
            if q.empty():
                print("-1")
            else:
                for element in q.iter():
                    print(element)

if __name__ == '__main__':
    consults = int(input())
    _main(consults)