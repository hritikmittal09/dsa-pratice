  def subarraySum(self, nums: List[int], k: int) -> int:
        
        # Sum of subarray from (j+1 to i) = prefix_sum - (prefix_sum - k) = k
        cur = 0
        mp = dict()
        mp[0] =1
        res = 0
        for i in nums:
            cur+=i
         
            if cur - k in mp:
                res+=mp[cur-k]
            if cur not in mp:
                mp[cur] =1
            else:
                mp[cur]+=1

        return res        


        