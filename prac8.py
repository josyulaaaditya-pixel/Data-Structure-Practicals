# Group C - Practical 1: Hashing using Chaining

# Hash table size = 10, hash function = key % 10

 

table = [[] for i in range(10)]

 

while True:

    print("\n1. Insert  2. Search  3. Delete  4. Display  5. Exit")

    choice = input("Enter choice: ")

 

    if choice == "5":

        print("Program ended.")

        break

 

    if choice == "4":

        for i in range(10):

            print(i, ":", table[i])

        continue

 

    if choice not in ("1", "2", "3"):

        print("Invalid choice.")

        continue

 

    try:

        key = int(input("Enter key: "))

    except ValueError:

        print("Please enter a valid integer key.")

        continue

 

    index = key % 10

 

    if choice == "1":

        if any(item[0] == key for item in table[index]):

            print("Key already exists.")

        else:

            value = input("Enter value: ")

            table[index].append((key, value))

            print("Inserted at index", index)

 

    elif choice == "2":

        for item in table[index]:

            if item[0] == key:

                print("Value:", item[1])

                break

        else:

            print("Key not found.")

 

    elif choice == "3":

        for item in table[index]:

            if item[0] == key:

                table[index].remove(item)

                print("Key deleted.")

                break

        else:

            print("Key not found.")

