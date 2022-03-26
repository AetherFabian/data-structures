from stack import Stack

my_stack = Stack()

def if_its_correct(arr):
    if len(arr)%2 == 0:

        for parentesis in arr:

            if parentesis == '(' or parentesis == '{' or parentesis == '[':
                my_stack.push(parentesis)

            else:
                element = my_stack.top()
                if element == '(':
                    if parentesis == ')':
                        my_stack.pop()
                    else:
                        return False
                elif element == '{':
                    if parentesis == '}':
                        my_stack.pop()
                    else:
                        return False
                elif element == '[':
                    if parentesis == ']':
                        my_stack.pop()
                    else:
                        return False
                else:
                    return False
        if my_stack.size() == 0:
            return True
    else:
        return False

if __name__ == '__main__':
    parentesis = input()
    arr = []
    for parent in parentesis:
        arr.append(parent)

    print(if_its_correct(arr))