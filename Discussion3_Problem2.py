import random

def random_partition(A, p, r):
    k = random.choice(list(range(p,r)))
    A[k], A[r-1] = A[r-1], A[k]
    x = A[r-1]

    i = p - 1

    for j in range(p, r-1):
        if A[j] <= x:
            i += 1
            A[i], A[j] = A[j], A[i]
    
    A[i+1], A[r-1] = A[r-1], A[i+1]
    
#     print(f'Partition pivot={A[i+1]}')
#     print(f'Partitioned array = {A[p:r]}')

    return i+1


def deterministic_partition(A, p, r):
    x = A[r-1]
    i = p - 1

    for j in range(p, r-1):
        if A[j] < x:
            i += 1
            A[i], A[j] = A[j], A[i]
    
    A[i+1], A[r-1] = A[r-1], A[i+1]
    
    print(f'Partitioned A={A}')
    
    return i+1

def weighted_median_selection(A,p,r, l_sum=0, r_sum=0, direction=None):
    if p==r-1:
        return A[p]
    
    q = random_partition(A, p, r)
    
    P = A[q]
    print(f'Pivot element q = {q}, A[q] = {A[q]}')

    if direction == 'right':
        l_sum = sum(A[p:q]) + l_sum
        r_sum = 1 - l_sum - P
    elif direction == 'left':
        r_sum = sum(A[q+1:r]) + r_sum
        l_sum = 1 - r_sum - P
    else:
        l_sum = sum(A[p:q])
        r_sum = 1 - l_sum - P
    
    print(f'Left sum = {l_sum}, pivot = {P}, right sum = {r_sum}')
       
    if (l_sum < 1/2) and (r_sum <= 1/2):
        return A[q]
    
    elif l_sum >= 1/2:
        print(f'Search in {A[p:q]}\n')
        r_sum += A[q]
        direction = 'left'
        return weighted_median_selection(A,p,q, l_sum, r_sum, direction)
        
    elif r_sum > 1/2:
        print(f'Search in {A[q+1:r]}\n')
        l_sum += A[q]
        direction = 'right'
        return weighted_median_selection(A,q+1,r, l_sum, r_sum, direction)

    
if __name__ == '__main__':
#     A = [0.35, 0.1, 0.05, 0.2, 0.1, 0.05, 0.15]
    A = [0.35, 0.2, 0.15, 0.1, 0.1, 0.05, 0.05]
#     A = [0.1, 0.35, 0.05, 0.1, 0.15, 0.05, 0.2]
#     A = [0.3,0.2]
    p = 0
    r = len(A)

    wm = weighted_median_selection(A,p,r)
    print(wm)
