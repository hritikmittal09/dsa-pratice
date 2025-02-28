class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def recoverFromPreorder(traversal: str):
    nodes = []
    i = 0
    while i < len(traversal):
        depth = 0
        while i < len(traversal) and traversal[i] == '-':  # Count dashes
            depth += 1
            i += 1
        num_start = i
        while i < len(traversal) and traversal[i].isdigit():  # Read number
            i += 1
        value = int(traversal[num_start:i])
        nodes.append((depth, TreeNode(value)))

    stack = []
    for depth, node in nodes:
        while len(stack) > depth:  # Find parent
            stack.pop()
        if stack:
            if not stack[-1].left:
                stack[-1].left = node
            else:
                stack[-1].right = node
        stack.append(node)
    
    return stack[0]  # Root of the tree
