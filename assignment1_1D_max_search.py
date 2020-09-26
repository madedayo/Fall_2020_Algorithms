def local_maximum(A, p, r):
    mid = (r + p + 1) // 2
    print(f'p={p}, r={r}, mid={mid}')
    
    if (mid < r) and (mid > p):
        if (A[mid]-A[mid-1]) > 0 and (A[mid]-A[mid+1]) > 0:
            print(f'p={p}, r={r}, mid={mid}')
            return mid    

        elif A[mid]-A[mid-1] > 0:
            print('Going right')
            print(f'p={p}, r={r}, mid={mid}')
            p = mid
            x = local_maximum(A, p, r)

        elif A[mid]-A[mid+1] > 0:
            print('Going left')
            print(f'p={p}, r={r}, mid={mid}')
            r = mid
            x = local_maximum(A, p, r)
            
    else:
        if (mid == r) and (p != 0):
            x = r
            return x
        elif (mid == r) and (p == 0):
            x = p
            return x
    return x

if __name__ == '__main__':
	# A = [1,8,11,12,15,18,19,29,37,55,66,71,72]
	# A = [33,28,21,12,11,9,8,7,4,3,2,1,0]
	# A = [1,21,28,12,11,9,8,7,4,3,2,1]
	A = [1,8,11,12,15,18,19,29,37,55,166,111,72]
	print(A, '\n')
	max_point = local_maximum(A, 0, len(A)-1)    
	print(f'Local maximum index: {max_point}')