class Solution(object):
    def twoSum(self, numbers, target):
    
        
        s = set()
        n = len(numbers)
        for i in range(n):
            x= target-numbers[i]
            if x in s :
                ans= [i+1,numbers.index(x)+1]
                ans.sort()
                return ans
            else :
                s.add(numbers[i])    

        