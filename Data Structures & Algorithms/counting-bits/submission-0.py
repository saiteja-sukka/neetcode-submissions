class Solution:
    def countBits(self, n: int) -> List[int]:
        count=[]
        for i in range(n+1):
            sum=0

            while i :


                if i&1==1:
                   sum+=1
                i=i>>1
            count.append(sum)
            
        return count
        
        