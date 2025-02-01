def GTR(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        ans =[]
        n = len(temperatures)
        s =  []
        arr = temperatures
        for i in range(n-1,-1,-1):
            if not s :
                ans.append(-1)
            elif s and s[-1] > arr[i]:
                ans.append(s[-1])
            elif s and s[-1] < arr[i]:
                while  s and s[-1] < arr[i]:
                    s.pop()
                if not s:
                    ans.append(-1)
                else :
                    ans.append(s[-1])            


            s.append(temperatures[i])
        return ans[::-1]    
        