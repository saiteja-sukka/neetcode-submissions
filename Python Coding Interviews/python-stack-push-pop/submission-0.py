from typing import List


def reverse_list(arr: List[int]) -> List[int]:
    arr1=[]
    for i in arr:
        arr1.append(i)
    stack=[]
    while len(arr1)>0:
        stack.append(arr1.pop())
    return stack
    pass


# do not modify below this line
print(reverse_list([1, 2, 3]))
print(reverse_list([3, 2, 1, 4, 6, 2]))
print(reverse_list([1, 9, 7, 3, 2, 1, 4, 6, 2]))
