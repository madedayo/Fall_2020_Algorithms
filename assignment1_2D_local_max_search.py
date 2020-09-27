def local_maximum(B, p, r):
    mid = (r + p + 1) // 2
    print(f'p={p}, r={r}, mid={mid}')
    
    if (mid < r) and (mid > p):

        if (B[mid]-B[mid-1] > 0) and (B[mid]-B[mid+1] > 0):
            print(f'p={p}, r={r}, mid={mid}')
            return mid    

        elif (B[mid]-B[mid-1] > 0) and (B[mid]-B[mid+1] < 0):
            print('Going right')
            print(f'p={p}, r={r}, mid={mid}')
            p = mid
            x = local_maximum(B, p, r)

        elif (B[mid]-B[mid+1] > 0) and (B[mid]-B[mid-1] < 0):
            print('Going left')
            print(f'p={p}, r={r}, mid={mid}')
            r = mid
            x = local_maximum(B, p, r)
            
    else:
        if (mid == r) and (p != 0):
            x = r
            return x
        elif (mid == r) and (p == 0):
            x = p
            return x
    return x

def local_maximum_2d(A, left, right, top, bottom):

    mid_row = (bottom + top + 1) // 2

    column_maximum_index = local_maximum(A[mid_row, left:right+1], left, right)
	# check that we are not on the either top or bottom edge of the array:
    if mid_row > top and mid_row < bottom:
        if (A[mid_row, column_maximum_index] - A[mid_row-1, column_maximum_index]) > 0 and (A[mid_row, column_maximum_index] - A[mid_row+1, column_maximum_index]) > 0:
            print('Local maximum is found.')
            print(f'row={mid_row}, left={left}, right={right}, max_index_col={column_maximum_index}')

            return mid_row, column_maximum_index

        elif (A[mid_row, column_maximum_index] - A[mid_row-1, column_maximum_index]) > 0 and (A[mid_row, column_maximum_index] - A[mid_row+1, column_maximum_index]) < 0:
            print('Move down in rows')
            print(f'row={mid_row}, left={left}, right={right}, max_index_col={column_maximum_index}')

            top = mid_row
            x, y = local_maximum_2d(A, left, right, top, bottom)

        elif (A[mid_row, column_maximum_index] - A[mid_row-1, column_maximum_index]) < 0 and (A[mid_row, column_maximum_index] - A[mid_row+1, column_maximum_index]) > 0:
            print('Move up in rows')
            print(f'row={mid_row}, left={left}, right={right}, max_index_col={column_maximum_index}')

            bottom = mid_row
            x, y = local_maximum_2d(A, left, right, top, bottom)
    else:
        if mid_row != bottom:
            return top, column_maximum_index
        
        elif mid_row != top:
            return bottom, column_maximum_index

    return x, y


if __name__ == '__main__':
        # A = np.array([[1,2,5,4,2,1], [1,55,4,2,1,0], [1,2,7,3,1,0],[1,25,12,10,6,3], [3,7,6,5,4,3]],  ndmin=2)
	# A = np.array([[1,2,5,4,2,1], [1,55,4,2,1,0], [1,2,8,3,1,0],[1,25,7,6,5,1], [3,7,6,5,4,0]],  ndmin=2)
	A = np.array([[3,4,5,6,5,4], [4,55,40,22,10,9], [3,4,5,7,8,6],[2,3,4,6,5,1], [1,2,3,5,4,0]],  ndmin=2)
	# A = np.array([[3,4,5,6,5,4], [64,55,40,22,10,9], [3,4,5,7,8,6],[2,3,4,6,5,2], [1,2,3,5,4,1], [0,1,2,4,3,0]],  ndmin=2)
	# A = np.array([[3,4,5,66,5,4], [4,5,6,18,10,9], [3,4,5,7,8,6],[2,3,4,6,5,2], [1,2,3,5,4,1], [0,1,2,4,3,0]],  ndmin=2)
	print(A,'\n')
	left, right, top, bottom = 0, A.shape[1]-1, 0, A.shape[0]-1
	row, col = local_maximum_2d(A, left, right, top, bottom)
	print(f'A[{row},{col}] is a local maximun in the given 2D array')
