'''
Input: a List of integers as well as an integer `k` representing the size of the sliding window
Returns: a List of integers

'''

def sliding_window_max(nums, k):
    # Your code here

    # define current_index index as 0
    current_index = 0
    # create an empty array 
    max_array = []

    # k is the size of the window, or the 'sub array' inside the main array
    while current_index + k - 1 < len(nums):
        max_array.append(max(nums[current_index:current_index+k])) # slice from current index to the index + k 
        # move the index to the next value so the window also moves one up
        current_index += 1
        # return max values of each sub-array stored in the new array 
    return max_array


if __name__ == '__main__':
    # Use the main function here to test out your implementation 
    arr = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 3

    print(f"Output of sliding_window_max function is: {sliding_window_max(arr, k)}")
