class Node:
    def __init__(self, key, left=None, right=None):
        self.key = key
        self.left = left
        self.right = right


def bst_walk(x, pred):
    if x == None:
        return True

    l = bst_walk(x.left, pred)
    print(f'pred = {pred.key}, curr = {x.key}')
    if x.key < pred.key:
        return False

    pred.key = x.key

    r = bst_walk(x.right, pred)

    return (l and r)
    

if __name__ == "__main__":
    # Create initial -ingf node:
    prev = Node(float('-inf'), None, None)
    
    # Create a false sample BST tree:
    test_not_bst = Node(3, None, None)
    node1 = Node(1, None, None)
    node0 = Node(0, None, None)
    node8 = Node(8, None, None)
    node9 = Node(9, None, None)
    
    test_not_bst = Node(3, node1, Node(7, Node(4, node1, Node(5, node0, node9)), node8))
    prev = Node(float('-inf'), None, None)
    print(f'{bst_walk(test_not_bst, prev)}')
    
    # Create a true sample BST tree:
    node1 = Node(1, None, None)
    node4 = Node(4, None, None)
    node11 = Node(11, None, None)
    node9 = Node(9, None, None)

    true_bst_tree = Node(5, Node(3, node1, node4), Node(6, None, Node(10, node9, node11)))
    prev = Node(float('-inf'), None, None)
    print(f'{bst_walk(true_bst_tree, prev)}')
