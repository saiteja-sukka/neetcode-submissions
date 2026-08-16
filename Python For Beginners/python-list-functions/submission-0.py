from typing import List # this is used to add type hints for List type

def get_sum(nums: List[int]) -> int:
    return sum(nums)
    pass

def get_min(nums: List[int]) -> int:
    return min(nums)
    pass

def get_max(nums: List[int]) -> int:
    return max(nums)
    pass

# do not modify below this line
print(get_sum([1, 2, 3, 4, 5]))
print(get_sum([5, 4, 5, 6]))

print(get_min([7, 3, 4, 5]))
print(get_min([5, 4, 5, 6]))

print(get_max([7, 3, 4, 5]))
print(get_max([5, 4, 5, 6]))






























""" List Functions
Python also provides some built in functions to get the sum, minimum, and maximum of a list:

my_list = [1, 2, 3, 4, 5]

print(sum(my_list))  # Output: 15
print(min(my_list))  # Output: 1
print(max(my_list))  # Output: 5
The sum() function returns the sum of all the elements in the list.
The min() function returns the smallest element in the list.
The max() function returns the largest element in the list.
Challenge
Implement the following functions on the right:

get_sum(my_list: List[int]) -> int should return the sum of all the elements in the list.
get_min(my_list: List[int]) -> int should return the smallest element in the list.
get_max(my_list: List[int]) -> int should return the largest element in the list.
You may assume the list passed in will always have at least one element.

If you want a challenge, try to implement these functions without using the built-in sum(), min(), and max() functions. Instead, you can use a loop to iterate through the list and keep track of the sum, minimum, and maximum.

Hint: It's generally not wise to name variables sum, min, or max since these are built-in functions. If you do, you will overwrite the built-in functions and won't be able to use them anymore. """