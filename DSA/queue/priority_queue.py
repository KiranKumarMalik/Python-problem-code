import queue
Q = queue.PriorityQueue()
max_length = int(input("Enter the maximum length of the queue: "))

def add():
    if Q.qsize() >= max_length:
        print("Queue is full/Overflow")
    else:
        element = input("Enter the element: ")
        Q.put(element)
        print(f"{element} added to the queue")

def remove():
    if Q.empty():
        print("Queue is empty/Underflow")
    else:
        removed_item = Q.get()
        print(f"{removed_item} removed from queue")

def display_queue():
    if Q.empty():
        print("Queue is empty")
    else:
        temp_items = []
        while not Q.empty():
            item = Q.get()
            temp_items.append(item)
            print(item, end=" ")
        print()
        for item in temp_items:
            Q.put(item)

while True:
    print("Choose your choice")
    print("1. Add")
    print("2. Remove")
    print("3. Display Queue")
    print("4. Exit")

    choice = int(input("Enter your valid choice: "))
    if choice == 1:
        add()
    elif choice == 2:
        remove()
    elif choice == 3:
        display_queue()
    elif choice == 4:
        break
    else:
        print("Enter valid choice")
