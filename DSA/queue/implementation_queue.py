queue = []
max_length = int(input("Enter the maximum length of the queue: "))

def add():
    if len(queue) >= max_length:
        print("Queue is full")
    else:
        element = input("Enter an element: ")
        queue.append(element)
        print(f"{element} added to queue")

def remove():
    if not queue:
        print("Queue is empty")
    else:
        popped_element = queue.pop(0)
        print(f"Removed element: {popped_element}")

def display_queue():
    if not queue:
        print("Queue is empty")
    else:
        print("Current Queue:", queue)

while True:
    print("\nChoose your option:")
    print("1. Add")
    print("2. Remove")
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