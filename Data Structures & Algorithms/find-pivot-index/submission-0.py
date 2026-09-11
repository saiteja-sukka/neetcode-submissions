class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        total=0
        list1=[]
        for i in nums:
            total+=i
            list1.append(total)
        n=len(list1)
        for i in range(len(list1)):
            left=list1[i-1]
            right=total-list1[i]
            if i ==0:
                left=0
                if right==left:
                    return 0
            
            if left==right:
                return i
        return -1
            

        