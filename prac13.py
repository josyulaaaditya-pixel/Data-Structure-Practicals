# Group D - Practical 3: Binary Search Tree Operations

class Node:

    def __init__(self, data):

        self.data = data

        self.left = None

        self.right = None

 

 

def insert(root, data):

    if root is None:

        return Node(data)

    if data < root.data:

        root.left = insert(root.left, data)

    elif data > root.data:

        root.right = insert(root.right, data)

    return root

 

 

def search(root, data):

    if root is None or root.data == data:

        return root is not None

    if data < root.data:

        return search(root.left, data)

    return search(root.right, data)

 

 

def minimum(root):

    while root.left:

        root = root.left

    return root.data

 

 

def delete(root, data):

    if root is None:

        return None

    if data < root.data:

        root.left = delete(root.left, data)

    elif data > root.data:

        root.right = delete(root.right, data)

    else:

        if root.left is None:

            return root.right

        if root.right is None:

            return root.left

        root.data = minimum(root.right)

        root.right = delete(root.right, root.data)

    return root

 

 

def inorder(root):

    if root:

        inorder(root.left)

        print(root.data, end=" ")

        inorder(root.right)

 

 

def preorder(root):

    if root:

        print(root.data, end=" ")

        preorder(root.left)

        preorder(root.right)

 

 

def postorder(root):

    if root:

        postorder(root.left)

        postorder(root.right)

        print(root.data, end=" ")

 

 

root = None

while True:

    print("\n1.Insert  2.Search  3.Delete  4.Traversals  5.Minimum  6.Exit")

    choice = input("Enter choice: ")

    if choice == "6":

        print("Program ended.")

        break

    if choice == "4":

        if root is None:

            print("Tree is empty.")

        else:

            print("Inorder: ", end="")

            inorder(root)

            print("\nPreorder: ", end="")

            preorder(root)

            print("\nPostorder: ", end="")

            postorder(root)

            print()

    elif choice == "5":

        print("Minimum:", minimum(root) if root else "Tree is empty")

    elif choice in ("1", "2", "3"):

        try:

            value = int(input("Enter number: "))

        except ValueError:

            print("Enter a valid integer.")

            continue

        if choice == "1":

            if search(root, value):

                print("Duplicate not inserted.")

            else:

                root = insert(root, value)

                print("Inserted.")

        elif choice == "2":

            print("Found." if search(root, value) else "Not found.")

        else:

            if search(root, value):

                root = delete(root, value)

                print("Deleted.")

            else:

                print("Not found.")

    else:

        print("Invalid choice.")

