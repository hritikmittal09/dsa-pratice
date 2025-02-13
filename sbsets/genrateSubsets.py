

def helprer(index,s,sset,nums):
    if index == len(nums):
        sset.append(s)
        return
    helprer(index +1 ,s+[nums[index]],sset,nums)
    helprer(index +1 ,s,sset,nums)



class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        subsets = []
        subsets = []
        helprer(0,[],subsets,nums)
        return subsets