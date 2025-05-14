def slove(s , l ,r,res ):
    if l ==r:
        res.append(s[:])

        return
    for i in range(l,len(s)):
        s[l] ,s[i] = s[i],s[l]
        slove(s,l+1,r ,res)
        s[l] ,s[i] = s[i],s[l]


class Solution(object):
    def permute(self, nums):
        res = []
        slove(nums,0,len(nums)-1  ,res)
        return res

