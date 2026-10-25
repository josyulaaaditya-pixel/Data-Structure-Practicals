# Group B - Practical 1: Text Editor using Stacks

 

document = ""

undo_stack = []

redo_stack = []

 

while True:

    print("\n--- TEXT EDITOR ---")

    print("1. Make a Change")

    print("2. Undo")

    print("3. Redo")

    print("4. Display Document")

    print("5. Exit")

 

    choice = input("Enter choice (1-5): ")

 

    if choice == "1":

        print("1. Add text")

        print("2. Replace document")

        action = input("Enter change type (1-2): ")

 

        if action == "1":

            text = input("Enter text to add: ")

            undo_stack.append(document)

            document += text

            redo_stack.clear()

            print("Text added.")

        elif action == "2":

            text = input("Enter new document text: ")

            undo_stack.append(document)

            document = text

            redo_stack.clear()

            print("Document replaced.")

        else:

            print("Invalid change type.")

 

    elif choice == "2":

        if undo_stack:

            redo_stack.append(document)

            document = undo_stack.pop()

            print("Undo successful. Document:", repr(document))

        else:

            print("Nothing to undo.")

 

    elif choice == "3":

        if redo_stack:

            undo_stack.append(document)

            document = redo_stack.pop()

            print("Redo successful. Document:", repr(document))

        else:

            print("Nothing to redo.")

 

    elif choice == "4":

        print("Current document:", repr(document))

 

    elif choice == "5":

        print("Exiting editor.")

        break

 

    else:

        print("Invalid choice.")

