from random import randint

def generate_graph(n, out):
    """
    This function generates edges for a random graph of a given number of edges.
    n: desired number of edges
    out: full path to the utput .txt file
    """
    l = []
    v = []
    for edge in range(n):
        a = randint(0,n)
        b = randint(0,n)
        while b == a:
            b = randint(0,n)
        v.append(a)
        v.append(b)
        l.append((a, b))
        
    l = list(set(l))
    v = set(v)
    print(f'Number of vertecies: {len(v)}')
    print(f'Number of edges: {len(l)}')
    
    with open(out, "w") as fp: 
        # Writing data to a file 
        for i in range(len(l)):
            fp.write(str(l[i])+'\n')
if __name__ == '__main__':
    out = './output.txt'

    generate_graph(20000, out)
