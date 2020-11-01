class Node:
    def __init__(self, key, left=None, right=None):
        self.key = key
        self.left = left
        self.right = right    
    
def LocalCheck(node1, node2):
    if node1 == None and node2 == None :
        return True
    elif node1 == None or node2 == None :
        return False
    else:
        return (node1.key == node2.key) and LocalCheck(node1.left, node2.left) and LocalCheck(node1.right, node2.right)

def GlobalCheck(T1, T2):
    if T2 == None:
        return True
    elif T1 == None:
        return False

    elif LocalCheck(T1, T2):
        return True
    else:
        return (GlobalCheck(T1.left, T2) or GlobalCheck(T1.right, T2))


if __name__ == '__main__':
    # Define nodes for T1:
    node7 = Node(7, None, None)
    node8 = Node(8, None, None)
    node9 = Node(9, None, None)
    node12 = Node(12, None, None)            
    node10 = Node(10, None, None)            
    node16 = Node(16, None, None) 
    node13 = Node(13, None, None)
    node18 = Node(18, None, None)
    
    # Build T1:
    T1 = Node(8, node7, Node(9, None, Node(12, node10, Node(16, node13, node18))))
    
    # Define nodes for T2:
    node16_2 = Node(16, None, None) 
    node13_2 = Node(13, None, None)
    node18_2 = Node(18, None, None)
    
    # Build T2:
    T2 = Node(16, node13_2, node18_2)

    B = GlobalCheck(T1, T2)
    print(B)
