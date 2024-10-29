queue = []

def add():
    element = input("Enter an element: ")
    queue.append(element)
    print(f"{element} Added to queue")
    return element

def remove():
    if not queue:
        print("Queue is Empty")
    else:
        popped_element = queue.pop(0)
        print(f"Removed element: {popped_element}")

def display_queue():
    if not queue:
        print("Queue is Empty")
    else:
        print("Current Queue:", queue)
        return queue

while True:
    print("\nChoose your choice")
    print("1. Add")
    print("2. remove")
    print("3. Display Queue")
    print("4. Exit")
    
    choice = int(input("Enter your choice number: "))
    if choice == 1:
        add()
    elif choice == 2:
        remove()
    elif choice == 3:
        display_queue()
    elif choice == 4:
        break
    else:
        print("Enter a valid choice.")
