class Solution:
    def calPoints(self, operations: List[str]) -> int:
        
        list1=[]
        for i in operations:
            if i=="+":
                list1.append(list1[-1] + list1[-2])
            elif i=="D":
                list1.append(2*list1[-1])
            elif i=="C":
                list1.pop()
            else:
                list1.append(int(i))
        result = 0
        for i in list1:
            result+=i
        return result