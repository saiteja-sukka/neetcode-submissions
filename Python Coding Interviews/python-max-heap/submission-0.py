import heapq
from typing import List


def get_reverse_sorted(nums: List[int]) -> List[int]:
    max_heap=[]
    list1=[]
    for num in nums:
        heapq.heappush(max_heap, -num)
    while max_heap:
        list1.append(-heapq.heappop(max_heap))
    return list1
    pass





# do not modify below this line
print(get_reverse_sorted([1, 2, 3]))
print(get_reverse_sorted([5, 6, 4, 2, 7, 3, 1]))
print(get_reverse_sorted([5, 6, -4, 2, 4, 7, -3, -1]))
