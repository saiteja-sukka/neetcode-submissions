class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        maximum=0
        sum=0
        for i in nums:
            if i==1:
                sum+=1
            else:
                maximum=max(maximum,sum)
                sum=0
        maximum=max(maximum,sum)
        return maximum
        
            
            
        