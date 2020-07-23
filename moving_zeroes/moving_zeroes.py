'''
Input: a List of integers
Returns: a List of integers
'''
def moving_zeroes(arr):
    # Your code here


    count = 0 # Count how many non-zero elements 
      
    # Traverse the array. If element encountered is non-zero, then 
    # replace the element at index 'count' with this element 
    for i in range(len(arr)): 
        if arr[i] != 0: 
              
            # here count is incremented when element is not 0 

            # if the element is not 0, it stays at its original position, then increase count to traverse to next element
            # even if there is a 0 between the elements, it will set the non-zero element to take the place of the zero element index
            arr[count] = arr[i] 
            count+=1
      
    # Now all non-zero elements have been 
    # shifted to front
    # check length of array, as long as 
    # count is smaller, it means  that the leftovers or the difference
    # will be filled with 0 until the end of the array
    while count < len(arr): 
        arr[count] = 0
        count += 1

    return arr

if __name__ == '__main__':
    # Use the main function here to test out your implementation
    arr = [0, 3, 1, 0, -2]

    print(f"The resulting of moving_zeroes is: {moving_zeroes(arr)}")