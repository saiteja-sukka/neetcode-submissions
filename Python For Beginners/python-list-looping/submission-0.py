from typing import List # used to add type hint for List

def count_x(nums: List[int], x: int) -> int:
    count=0
    for i in nums:
        if i==x:
            count+=1
    return count
    pass



# do not modify below this line
print(count_x([1, 2, 5, 6, 5], 5))
print(count_x([4, 3, 6, 1, 6], 5))
print(count_x([4, 7, 7, 6, 7, 6], 7))



































""" List Looping
We can also loop through lists similar to how we loop through strings.

By using the length of the list:

my_list = [1, 2, 3, 4, 5]

length = len(my_list)

for i in range(length):
    print(my_list[i])
Or by using the in operator:

my_list = [1, 2, 3, 4, 5]

for element in my_list:
    print(element)
Both of these methods will print each element of the list on a separate line. If we don't need the index of the element, the second method is generally preferred since it is more concise.

Challenge
Implement the function count_x(nums: List[int], x: int) -> int. It accepts a list of integers nums and an integer x. The function should return the number of times the integer x appears in the list nums. """