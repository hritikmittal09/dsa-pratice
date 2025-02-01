def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        ans = []
        n = len(temperatures)
        s = []
        arr = temperatures

        for i in range(n - 1, -1, -1):
            if not s:
                ans.append(0)
            elif s and arr[s[-1]] > arr[i]:  # Compare values using stored indices
                ans.append(s[-1] - i)  # Store index difference
            elif s and arr[s[-1]] <= arr[i]:
                while s and arr[s[-1]] <= arr[i]:
                    s.pop()
                if not s:
                    ans.append(0)
                else:
                    ans.append(s[-1] - i)  # Store index difference

            s.append(i)  # Store index instead of value

        return ans[::-1]