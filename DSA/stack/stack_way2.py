Stack = []

def push():
    element = input("Enter an element: ")
    Stack.append(element)
    print(f"{element} pushed to stack")
    return element

def pop():
    if not Stack:
        print("Stack is Empty")
    else:
        popped_element = Stack.pop()
        print(f"Popped item: {popped_element}")
        return popped_element

def peek():
    if not Stack:
        print("Stack is Empty")
    else:
        top_element = Stack[-1]
        print(f"Top item: {top_element}")
        return top_element

def display_stack():
    if not Stack:
        print("Stack is Empty")
    else:
        print("Current Stack:", Stack)
        return Stack

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
