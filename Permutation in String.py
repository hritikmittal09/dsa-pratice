from collections import Counter
def checkInclusion(self, s1, s2):
        c1 = Counter(s1)
        #c2 = Counter(s2)
        #ans = True
        k=len(s1)
        i =0
        j =0
        n = len(s2)
        while j< n : 
            if j-i +1 <k :
                j +=1
            if j-i+1 ==k:
                if Counter(s2[i:j+1]) ==c1:
                    return True
                i +=1
                j+=1
        return False            

