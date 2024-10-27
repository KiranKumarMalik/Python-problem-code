import collections
stack=collections.deque()

def push():
    element=input("Enter an element: ")
    stack.append(element)
    print(f"Pushed item: {element}")
    return stack
def pop():
    if not stack:
        return "Stack is empty"
    else:
        popped_item=stack.pop()
        print(f"Popped item: {popped_item}")
    
def peek():
    if not stack:
        return "Stack is empty"
    else:
        peek_item=stack[-1]
        print(f"Top item: {peek_item}")

def display_stack():
    if not stack:
        return "Stack is empty"
    else:
        print(f"Current stack is: {stack}")
    
while True:
    print("\nChoose your choice")
    print("1. Push")
    print("2. Pop")
    print("3. Peek")
    print("4. Display Stack")
    print("5. Exit")
    
    choice = int(input("Enter your choice number: "))
    if choice == 1:
        push()
    elif choice == 2:
        pop()
    elif choice == 3:
        peek()
    elif choice == 4:
        display_stack()
    elif choice == 5:
        break
    else:
        print("Enter a valid choice.")