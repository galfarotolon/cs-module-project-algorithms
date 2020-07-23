'''
Input: a List of integers
Returns: a List of integers
'''

# Psuedocode
# define new array
# for i in range(len(array))
    # define product as 1
    # for j in range(len(array))
        # if i != j
            # product *= array[j]
    # new array.append(product)
# return new array

def product_of_all_other_numbers(arr):

    # make a new array that contains the product
    # of all elements in the array except i

#  A brute force approach: would use two loops to multiply the integer at every index by the integer at every nestedIndex, 
# unless index == nestedIndex.

# This would give us a runtime of O(n^2)

    # this will be the list to hold final values 
    product_array = []

    #loop through original array
    for i in range(len(arr)):
        # start the variable to hold the product of all
        # numbers except the number itself

        # this value gets restarted every time the loop begins
        product = 1

        # for each number in the original array,

        for j in range(len(arr)):

            #if j is different from the current number, 
            # then multiply it by the product, else ignore

            if i != j:
                # if they are not, multiply all elements except that value and store it in the new array in its original index
                product *= arr[j]
        
        # add product to the product array
        product_array.append(product)
    return product_array




if __name__ == '__main__':
    # Use the main function to test your implementation
    # arr = [1, 2, 3, 4, 5]
    arr = [2, 6, 9, 8, 2, 2, 9, 10, 7, 4, 7, 1, 9, 5, 9, 1, 8, 1, 8, 6, 2, 6, 4, 8, 9, 5, 4, 9, 10, 3, 9, 1, 9, 2, 6, 8, 5, 5, 4, 7, 7, 5, 8, 1, 6, 5, 1, 7, 7, 8]

    print(f"Output of product_of_all_other_numbers: {product_of_all_other_numbers(arr)}")
