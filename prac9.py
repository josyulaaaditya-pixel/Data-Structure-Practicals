# Group C - Practical 2: Linear Probing

SIZE = 10

table = [None] * SIZE

DELETED = 'DELETED'

 

while True:

    print('\n1. Insert  2. Search  3. Delete  4. Display  5. Exit')

    choice = input('Enter choice: ')

 

    if choice == '5':

        print('Program ended.')

        break

    if choice == '4':

        for i in range(SIZE):

            print(i, ':', '-' if table[i] is None or table[i] == DELETED else table[i])

        continue

    if choice not in ('1', '2', '3'):

        print('Invalid choice.')

        continue

    try:

        key = int(input('Enter key: '))

    except ValueError:

        print('Enter a valid integer.')

        continue

 

    index = key % SIZE

    found = -1

    first_deleted = -1

    empty = -1

    for step in range(SIZE):

        pos = (index + step) % SIZE

        if table[pos] == key:

            found = pos

            break

        if table[pos] == DELETED and first_deleted == -1:

            first_deleted = pos

        if table[pos] is None:

            empty = pos

            break

 

    if choice == '1':

        if found != -1:

            print('Key already exists.')

        elif first_deleted != -1 or empty != -1:

            pos = first_deleted if first_deleted != -1 else empty

            table[pos] = key

            print('Inserted at index', pos)

        else:

            print('Hash table is full.')

    elif choice == '2':

        print('Found at index' if found != -1 else 'Key not found.', end='')

        if found != -1:

            print(' ', found, sep='')

        else:

            print()

    elif choice == '3':

        if found != -1:

            table[found] = DELETED

            print('Key deleted.')

        else:

            print('Key not found.')

