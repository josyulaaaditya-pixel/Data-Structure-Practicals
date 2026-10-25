# Group D - Practical 5: City Population using BST

 

class Node:

    def __init__(self, city, population):

        self.city = city

        self.population = population

        self.left = None

        self.right = None

 

def insert(root, city, population):

    if root is None:

        return Node(city, population)

    if city.lower() < root.city.lower():

        root.left = insert(root.left, city, population)

    elif city.lower() > root.city.lower():

        root.right = insert(root.right, city, population)

    else:

        root.population = population

    return root

 

def search(root, city):

    while root:

        if city.lower() == root.city.lower():

            return root

        if city.lower() < root.city.lower():

            root = root.left

        else:

            root = root.right

    return None

 

def display(root):

    if root:

        display(root.left)

        print(root.city, ":", root.population)

        display(root.right)

 

def smallest(root):

    while root.left:

        root = root.left

    return root

 

def delete(root, city):

    if root is None:

        return None

    if city.lower() < root.city.lower():

        root.left = delete(root.left, city)

    elif city.lower() > root.city.lower():

        root.right = delete(root.right, city)

    else:

        if root.left is None:

            return root.right

        if root.right is None:

            return root.left

        next_node = smallest(root.right)

        root.city = next_node.city

        root.population = next_node.population

        root.right = delete(root.right, next_node.city)

    return root

 

root = None

while True:

    print("\n1.Add/Update  2.Search  3.Delete  4.Display  5.Exit")

    choice = input("Choice: ")

    if choice == "5":

        print("Program ended.")

        break

    if choice == "4":

        if root is None:

            print("No city records.")

        else:

            print("Cities in alphabetical order:")

            display(root)

        continue

    if choice not in ("1", "2", "3"):

        print("Invalid choice.")

        continue

    city = input("City name: ").strip()

    if not city:

        print("City name cannot be empty.")

        continue

    if choice == "1":

        try:

            population = int(input("Population: "))

            if population < 0:

                print("Population cannot be negative.")

            else:

                root = insert(root, city, population)

                print("City saved.")

        except ValueError:

            print("Enter a valid whole number.")

    elif choice == "2":

        result = search(root, city)

        if result:

            print(result.city, ":", result.population)

        else:

            print("City not found.")

    elif choice == "3":

        if search(root, city):

            root = delete(root, city)

            print("City deleted.")

        else:

            print("City not found.")

