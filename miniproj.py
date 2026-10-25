class Queue:

    def __init__(self):

        self.stack1 = []

        self.stack2 = []

 

    def enqueue(self, item):

        self.stack1.append(item)

        print(item, "added to queue.")

 

    def dequeue(self):

        if not self.stack2:

            while self.stack1:

                self.stack2.append(self.stack1.pop())

        if not self.stack2:

            print("Queue is empty.")

        else:

            print(self.stack2.pop(), "removed from queue.")

 

    def display(self):

        items = self.stack2[::-1] + self.stack1

        if items:

            print("Queue:", items)

        else:

            print("Queue is empty.")

 

q = Queue()

while True:

    print("\n1. Enqueue  2. Dequeue  3. Display  4. Exit")

    choice = input("Enter choice: ")

 

    if choice == "1":

        item = input("Enter item: ")

        q.enqueue(item)

    elif choice == "2":

        q.dequeue()

    elif choice == "3":

        q.display()

    elif choice == "4":

        print("Program ended.")

        break

    else:

        print("Invalid choice.")

