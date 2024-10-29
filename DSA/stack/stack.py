class Stack:
    def __init__(self):
        self.stack=[]

    def push(self,item):
        self.stack.append(item)
        print(f"{item} pushed to stack")

    def pop(self):
        if self.is_empty():
            print("Stack is empty, cannot pop")
            return None
        return self.stack.pop()
    
    def is_empty(self):
        return len(self.stack) == 0
    
    def display(self):
        if self.is_empty():
            print("Stack is Empty")
        else:
            print("Stack elements are:", self.stack)


def stack_operations():
    stack = Stack()
    while True:
        print("\nChoose an operation:")
        print("1.Push")
        print("2.Pop")
        print("3.Display stack")
        print("4.Exit")

        choice = int(input("Enter your choice:"))

        if choice==1:
            item=input("Enter item to push: ")
            stack.push(item)
        elif choice==2:
            popped_item=stack.pop()
            if popped_item is not None:
                print("Popped item: {popped_item}")
        elif choice==3:
            stack.display()
        elif choice==4:
            print("Exiting...")
            break
        else:
            print("Invalid choice, please try again")

if __name__=="__main__":
    stack_operations()