from collections import deque
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def is_operator(c):
    return c in ['∧', '∨', '→', '¬']

# Function to create binary tree from propositional formula
def build_tree(formula):
    stack_nodes = []
    stack_ops = []

    def apply_operator():
        op = stack_ops.pop()
        node = Node(op)
        if op == '¬':   # unary operator
            node.right = stack_nodes.pop()
        else:           # binary operator
            right = stack_nodes.pop()
            left = stack_nodes.pop()
            node.left = left
            node.right = right
        stack_nodes.append(node)

    i = 0
    while i < len(formula):
        c = formula[i]

        if c == ' ':
            i += 1
            continue

        if c == '(':
            stack_ops.append(c)

        elif c.isalpha():   # operands like p, q, r
            stack_nodes.append(Node(c))

        elif is_operator(c):
            # Handle multi-char operator "→"
            if c == '→':
                stack_ops.append("→")
            elif c == '¬':
                stack_ops.append("¬")
            else:
                stack_ops.append(c)

        elif c == ')':
            while stack_ops and stack_ops[-1] != '(':
                apply_operator()
            stack_ops.pop()  # remove '('

        i += 1

    while stack_ops:
        apply_operator()

    return stack_nodes[-1]


# Inorder traversal to check correctness
def inorder(root):
    if root:
        if root.left or root.right:
            print("(", end="")
        inorder(root.left)
        print(root.value, end="")
        inorder(root.right)
        if root.left or root.right:
            print(")", end="")


# Level-order (BFS) traversal for visualization
def print_tree_levels(root):
    if not root:
        return
    q = deque([root])
    level = 0
    while q:
        size = len(q)
        print("Level", level, ":", end=" ")
        for _ in range(size):
            node = q.popleft()
            print(node.value, end=" ")
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        print()
        level += 1


# ---------------- Main ----------------
if __name__ == "__main__":
    formula = "(p∧q)∨(¬r)"
    print("Formula:", formula)

    tree = build_tree(formula)

    print("\nInorder traversal (reconstructed):", end=" ")
    inorder(tree)
    print()

    print("\nBinary Tree Representation:")
    print_tree_levels(tree)
