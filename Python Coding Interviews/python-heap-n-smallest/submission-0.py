import heapq
from typing import List


def get_min_element(arr: List[int]) -> int:
    smallest =  heapq.nsmallest(1, arr)
    return smallest[0]
    pass


def get_min_4_elements(arr: List[int]) -> List[int]:
    return heapq.nsmallest(4,arr)
    # Return elements in *increasing* order
    pass


def get_min_2_elements(arr: List[int]) -> List[int]:
    
    arr=heapq.nsmallest(2,arr)
    arr.sort(reverse=True)
    return arr
    # Return elements in *decreasing* order
    pass


# do not modify below this line
print(get_min_element([1, 2, 3]))
print(get_min_element([3, 2, 1, 4, 6, 2]))
print(get_min_element([1, 9, 7, 3, 2, 1, 4, 6, 2]))

print(get_min_4_elements([1, 9, 7, 3, 2, 1, 4, 6, 2]))
print(get_min_4_elements([1, 9, 7, 2, 1, 3, 2, 1, 4, 6, 2, 1]))
print(get_min_4_elements([1, 9, 7, 2, 3, 2, 4, 6, 2]))

print(get_min_2_elements([1, 9, 7, 3, 2, 1, 4, 6, 2]))
print(get_min_2_elements([1, 9, 7, 2, 1, 3, 2, 1, 4, 6, 2, 1]))
print(get_min_2_elements([1, 9, 7, 2, 3, 2, 4, 6, 2]))

