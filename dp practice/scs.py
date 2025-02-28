def LengthOfLcs(str1,str2,m,n,t):
    for i in range(m+1):
        for j in range(n+1):
            if n == 0 or m==0:
                t[m][n] = 0
        for i in range(1,m+1):
            for j in range(1,n+1):
                if str1[i-1] == str2[j-1]:
                    t[i][j] = 1 +t[i-1][j-1]
                else :
                    t[i][j] = max(t[i-1][j],t[i][j-1])
        return t[m][n]
def printScs(str1,str2,m,n,t):
    sub = []
    i = m
    j = n
    while i > 0 and j > 0:
        if str1[i-1] == str2[j-1]:  # If characters match, add to result
            sub.append(str1[i-1])
            i -= 1
            j -= 1
        elif t[i-1][j] > t[i][j-1]:  # Move in the direction of larger value
            sub.append(str1[i-1])
            i -= 1
        else:
            sub.append(str2[j-1])
            j -= 1

    while i > 0:  # Add remaining characters from str1
        sub.append(str1[i-1])
        i -= 1

    while j > 0:  # Add remaining characters from str2
        sub.append(str2[j-1])
        j -= 1

    return "".join(reversed(sub))
    



   
class Solution(object):
    def shortestCommonSupersequence(self, str1, str2):
        m = len(str1)
        n = len(str2)
        t = []
        
        for i in range(m+1):
            col =[]
            for j in range(n+1):
                col.append(-1)
            t.append(col)    
        LengthOfLcs(str1,str2,m,n,t)
        ans =printScs(str1,str2,m,n,t)
        return ans



        """
        :type str1: str
        :type str2: str
        :rtype: str
        """
        