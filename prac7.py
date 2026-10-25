class Node:

    def __init__(self, roll, name, marks):

        self.roll = roll

        self.name = name

        self.marks = marks

        self.next = None

 

head = None

 

def find(roll):

    temp = head

    while temp:

        if temp.roll == roll:

            return temp

        temp = temp.next

    return None

 

def add(roll, name, marks):

    global head

    if find(roll):

        print("Roll number already exists.")

        return

    new = Node(roll, name, marks)

    new.next = head

    head = new

    print("Student added.")

 

def delete(roll):

    global head

    if head is None:

        print("List is empty.")

        return

    if head.roll == roll:

        head = head.next

        print("Student deleted.")

        return

    temp = head

    while temp.next and temp.next.roll != roll:

        temp = temp.next

    if temp.next:

        temp.next = temp.next.next

        print("Student deleted.")

    else:

        print("Student not found.")

 

def display(sort_by="roll", reverse=False):

    records = []

    temp = head

    while temp:

        records.append((temp.roll, temp.name, temp.marks))

        temp = temp.next

    if not records:

        print("No student records.")

        return

    if sort_by == "marks":

        records.sort(key=lambda x: x[2], reverse=reverse)

    else:

        records.sort(key=lambda x: x[0], reverse=reverse)

    print("Roll  Name  Marks")

    for roll, name, marks in records:

        print(roll, name, marks)

 

while True:

    print("\n1.Add  2.Delete  3.Update  4.Search  5.Display/Sort  6.Exit")

    choice = input("Choice: ")

    if choice == "6":

        print("Program ended.")

        break

    if choice not in ("1", "2", "3", "4", "5"):

        print("Invalid choice.")

        continue

    if choice == "5":

        field = input("Sort by (1.Roll / 2.Marks): ")

        order = input("Order (1.Ascending / 2.Descending): ")

        if field not in ("1", "2") or order not in ("1", "2"):

            print("Invalid sorting option.")

        else:

            display("roll" if field == "1" else "marks", order == "2")

        continue

    try:

        roll = int(input("Roll number: "))

    except ValueError:

        print("Enter a valid roll number.")

        continue

    if choice == "1":

        name = input("Name: ")

        try:

            marks = float(input("Marks: "))

            add(roll, name, marks)

        except ValueError:

            print("Enter valid marks.")

    elif choice == "2":

        delete(roll)

    elif choice == "3":

        student = find(roll)

        if student:

            name = input("New name: ")

            try:

                marks = float(input("New marks: "))

                student.name = name

                student.marks = marks

                print("Student updated.")

            except ValueError:

                print("Invalid marks. Record unchanged.")

        else:

            print("Student not found.")

    elif choice == "4":

        student = find(roll)

        if student:

            print(student.roll, student.name, student.marks)

        else:

            print("Student not found.")

