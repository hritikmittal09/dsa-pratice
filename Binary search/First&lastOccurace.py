class Solution(object):
    
    def BsF(self,arr,key):
        ans =-1
        l = 0
        h = len(arr)-1
        while l <=h :
            mid =(l+h) //2
            if arr[mid] ==key:
                ans = mid
                h = mid - 1
            elif arr[mid] < key :
                l =mid +1
            else :
                h = mid -1
        return ans
    def BsL(self,arr,key):
        ans =-1
        l = 0
        h = len(arr)-1
        while l <=h :
            mid =(l+h) //2
            if arr[mid] ==key:
                ans = mid
                l = mid + 1
            elif arr[mid] < key :
                l =mid +1
            else :
                h = mid -1
        return ans                     
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        i =self.BsF(nums,target)
        j = self.BsL(nums,target)
        print(i)
        print(j)
        return [i,j]
        