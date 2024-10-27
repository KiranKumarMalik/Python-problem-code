import queue
stack=queue.LifoQueue()

def push():
    element=input("Enter an element: ")
    stack.put(element)
    print(f"Pushed element: {element}")

def pop():
    if not stack:
        print("Stack is empty")
    else:
        popped_item=stack.get()
        print(f"Popped item: {popped_item}")
    
def peek():
    if not stack:
        print("Stack is empty")
    else:
        top_item=stack[-1]
        print(f"Top element: {top_item}")
    
def display_stack():
    if not stack:
        print("Stack is empty")
    else:
        print(f"Current stack: {stack}")

while True:
    print("Choose your choices: ")
    print("1. Push")
    print("2. Pop")
    print("3. Peek")
    print("4. Display")
    print("5. Exit")

    choice=int(input("Enter your choice number: "))
    if choice==1:
        push()
    elif choice==2:
        pop()
    elif choice==3:
        peek()
    elif choice==4:
        display_stack()
    elif choice==5:
        break
    else:
        print("Enter a valid choice...")