from collections import deque


def levelOrder(root):
    if not root:
        return []
    
    result = []
    queue = deque([root])  # Initialize queue with root

    while queue:
        level = []
        for _ in range(len(queue)):  # Process all nodes in the current level
            node = queue.popleft()
            level.append(node.val)
            
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        
        result.append(level)  # Store current level

    return result