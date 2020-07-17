'''
Input: an integer
Returns: an integer
'''
import functools

@functools.lru_cache()
def eating_cookies(n):
    # Your code here
    #Base cases


    if n == 0:
        return 1
    #Only one way to eat 1 cookie
    if n == 1:
        return 1
    #Only 2 ways to eat 2 cookies
    if n == 2:
        return 2
    #Only 4 different ways to eat 3 cookies
    if n == 3:
        return 4

    #Use recursion to simulate 1 , 2 , or 3 at a time and combine the combinations
    return eating_cookies(n-1) + eating_cookies(n-2) + eating_cookies(n-3)


if __name__ == "__main__":
    # Use the main function here to test out your implementation
    num_cookies = 5

    print(f"There are {eating_cookies(num_cookies)} ways for Cookie Monster to eat {num_cookies} cookies")
