def isP(s):
    l = 0
    e = len(s) -1
    while l <= e :
        if s[l] !=s[e]:
            return False
        l+=1
        e-=1
    return True
def back(index ,inp, res , sub ):
    if index == len(inp):
        res.append(sub[:])
        return 
    for i in range(index,len(inp)):
        if isP(inp[index:i+1]):
            sub.append(inp[index: i+1])
            back(i+1,inp,res,sub)
            sub.pop()        

class Solution(object):
    def partition(self, s,):
        res =[]
        sub =[]
        back(0,s,res,sub)
        return res

        """
        :type s: str
        :rtype: List[List[str]]
        """
        