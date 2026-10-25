# Group B - Practical 3: Call Center Queue

 

calls = []

 

while True:

    print('\n1. Add Call')

    print('2. Answer Call')

    print('3. View Queue')

    print('4. Check if Queue is Empty')

    print('5. Exit')

    choice = input('Enter choice: ')

 

    if choice == '1':

        customer_id = input('Enter customer ID: ').strip()

        if not customer_id:

            print('Customer ID cannot be empty.')

            continue

        if any(call[0] == customer_id for call in calls):

            print('Customer ID already in queue.')

            continue

        try:

            call_time = float(input('Enter call time (minutes): '))

            if call_time <= 0:

                print('Call time must be positive.')

                continue

        except ValueError:

            print('Please enter a valid number.')

            continue

        calls.append([customer_id, call_time])

        print('Call added successfully.')

 

    elif choice == '2':

        if calls:

            call = calls.pop(0)

            print('Answered call from', call[0], '- Time:', call[1], 'minutes')

        else:

            print('No calls to answer.')

 

    elif choice == '3':

        if calls:

            print('Waiting calls (first to last):')

            for call in calls:

                print('Customer:', call[0], '| Time:', call[1], 'minutes')

        else:

            print('Queue is empty.')

 

    elif choice == '4':

        if not calls:

            print('Yes, queue is empty.')

        else:

            print('No, queue has', len(calls), 'call(s).')

 

    elif choice == '5':

        print('Program ended.')

        break

    else:

        print('Invalid choice. Try again.')

