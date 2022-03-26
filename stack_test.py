#import Stack method from the stack.py
from stack import Stack

if __name__ == '__main__':
    t=""
    my_stack = Stack()

    #print the size and is the stack is empty to check if it is empty
    def print_stack(my_stack):
        print(t.center(50,'-'))
        print(f'List Top = {my_stack.top()}')
        print(f'List Size = {my_stack.size()}')
        print(f'If list is empty =  {my_stack.empty()}')
    #show the stack at first
    print_stack(my_stack)
    #add some data in the stack node
    my_stack.push("Joshua")
    my_stack.push("Gustavo")
    my_stack.push("Soco")
    print_stack(my_stack)

    #show the stack again
    for element in my_stack.iter():
        print(element)

    #delete the item of the stack that is the top data
    my_stack.pop()

    #show the stack again
    print_stack(my_stack)
    for element in my_stack.iter():
        print(element)
    #clear the stack
    my_stack.clear()
    #check if the clear method of is working
    print_stack(my_stack)
