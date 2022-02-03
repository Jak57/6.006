def count_long_subarray(A):
    '''
    Input:  A     | Python Tuple of positive integers
    Output: count | number of longest increasing subarrays of A
    '''
    count = 0
    ##################
    # YOUR CODE HERE #
    ##################
    
    max_len = 0
    arr = []
    
    for i in range(len(A)):
        temp_count = 0
        j = i
        k = i + 1
        
        while (j < len(A) and k < len(A)):
            
            if A[j] < A[k]:
                temp_count += 1
            else:
                break
            
            j += 1
            k += 1

        max_len = max(max_len, temp_count + 1)
        arr.append(temp_count + 1)

    for i in range(len(arr)):
        if arr[i] == max_len:
            count += 1
    
    return count
