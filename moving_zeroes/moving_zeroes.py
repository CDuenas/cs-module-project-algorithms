'''
Input: a List of integers
Returns: a List of integers
'''

def moving_zeroes(arr):
    # Your code here
    #Create a new arr 
    newArr = []

    #traverse the array
    for i in range(0, len(arr)):
        #if the element is a zero push it onto the array
        if arr[i] == 0:
            newArr.append(0)
        #if it is not a zero insert it to the front of the array
        else:
            newArr.insert(0, arr[i])

    return newArr


if __name__ == '__main__':
    # Use the main function here to test out your implementation
    arr = [0, 3, 1, 0, -2]

    print(f"The resulting of moving_zeroes is: {moving_zeroes(arr)}")