from binarytree import Node, build

def dfs_map(tree, func):
    """
    Given a binary tree and a function, applies the function to each element of the tree
    using a depth-first search traversal, and yields the result for each element.
    """
    if tree is None:
        return
    
    stack = [tree]
    while stack:
        node = stack.pop()
        yield func(node.value)
        if node.right is not None:
            stack.append(node.right)
        if node.left is not None:
            stack.append(node.left)

tree = Node(1)
tree.left = Node(2)
tree.right = Node(3)
tree.left.left = Node(4)
tree.left.right = Node(5)
tree.right.left = Node(6)
tree.right.right = Node(7)

print('28', 'tree', tree)

generator = dfs_map(tree, lambda x: x*x )
for result in generator:
    print(result)
    
b_tree = build([1, 2, 3, 4, 5, 6, 7, 8, None, 9])
print('35', 'b_tree', b_tree)

