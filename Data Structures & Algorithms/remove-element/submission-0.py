class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        n=len(nums)
        k=0
        for i in range(len(nums)):
            if nums[i]!=val:
                nums[k]=nums[i]
                k+=1
        return k
        
        """i = 0
        n = len(nums)
        while i < n:
            if nums[i] == val:
                # Replace current element with the last element
                nums[i] = nums[n - 1]
                n -= 1  # Reduce effective size
            else:
                i += 1  # Only move forward if element is kept
        return n  """

                

        
        