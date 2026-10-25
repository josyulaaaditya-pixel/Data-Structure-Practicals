# Expression Tree from Prefix Expression

# Enter single-letter or single-digit operands, e.g. *+AB-CD

 

class Node:

    def __init__(self, data):

        self.data = data

        self.left = None

        self.right = None

 

 

def build_tree(prefix):

    stack = []

    operators = '+-*/^'

    for ch in reversed(prefix):

        if ch.isalnum():

            stack.append(Node(ch))

        elif ch in operators:

            if len(stack) < 2:

                return None

            root = Node(ch)

            root.left = stack.pop()

            root.right = stack.pop()

            stack.append(root)

        else:

            return None

    if len(stack) != 1:

        return None

    return stack[0]

 

 

def inorder(root):

    if root:

        if root.left:

            print('(', end='')

        inorder(root.left)

        print(root.data, end='')

        inorder(root.right)

        if root.right:

            print(')', end='')

 

 

def preorder(root):

    if root:

        print(root.data, end='')

        preorder(root.left)

        preorder(root.right)

 

 

def postorder(root):

    if root:

        postorder(root.left)

        postorder(root.right)

        print(root.data, end='')

 

 

while True:

    prefix = input('Enter prefix expression (or EXIT): ').strip().replace(' ', '')

    if prefix.upper() == 'EXIT':

        print('Program ended.')

        break

    root = build_tree(prefix)

    if root is None:

        print('Invalid prefix expression.')

    else:

        print('Inorder: ', end='')

        inorder(root)

        print('\nPreorder: ', end='')

        preorder(root)

        print('\nPostorder: ', end='')

        postorder(root)

        print()

