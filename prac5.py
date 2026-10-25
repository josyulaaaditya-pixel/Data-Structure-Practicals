# Group B - Practical 2: Event Processing using Queue

 

queue = []

 

while True:

    print("\n1. Add Event")

    print("2. Process Next Event")

    print("3. Display Pending Events")

    print("4. Cancel Event")

    print("5. Exit")

 

    choice = input("Enter choice: ")

 

    if choice == "1":

        event = input("Enter event name: ").strip()

        if event:

            queue.append(event)

            print("Event added:", event)

        else:

            print("Event name cannot be empty.")

 

    elif choice == "2":

        if queue:

            print("Processed:", queue.pop(0))

        else:

            print("No events to process.")

 

    elif choice == "3":

        if queue:

            print("Pending events:")

            for event in queue:

                print("-", event)

        else:

            print("No pending events.")

 

    elif choice == "4":

        event = input("Enter event name to cancel: ").strip()

        if event in queue:

            queue.remove(event)

            print("Cancelled:", event)

        else:

            print("Event not found in pending queue.")

 

    elif choice == "5":

        print("Program ended.")

        break

 

    else:

        print("Invalid choice.")

