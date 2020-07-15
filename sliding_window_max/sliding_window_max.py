'''
Input: a List of integers as well as an integer `k` representing the size of the sliding window
Returns: a List of integers
'''
def sliding_window_max(nums, k):
    # Your code here
    #New array to append max's to
    maxList = []

    #Window range
    window_start = 0
    window_end = window_start + (k-1)

    #Begin loop that goes until the end of the list
    while window_end != len(nums):
        #create a max variable
        #begin by setting it to the first element in the list
        current_max = nums[window_start]

        #iterate through the window to find the actual max
        for i in range(window_start, window_end + 1):
            #if the element is greater than the current max
            if nums[i] > current_max:
                #current max becomes the element at that index
                current_max = nums[i]

        #Add the max to the maxList
        maxList.append(current_max)

        #move window by incrementing the start and end by 1
        window_start += 1
        window_end += 1
    
    #end loop and return the list
    return maxList


if __name__ == '__main__':
    # Use the main function here to test out your implementation 
    arr = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 3

    print(f"Output of sliding_window_max function is: {sliding_window_max(arr, k)}")
