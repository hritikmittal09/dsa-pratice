  
t = []




def lcs (x:str , y :str , m , n  ):
    if n ==0 or m ==0 :
        t[m][n]=0
        return 0
    if t[m][n]!= -1:
        return t[m][n]
    if x[m-1]==y[n-1]:
        t[m][n]= 1 + lcs(x,y,m-1,n-1)
        return t[m][n]
    else :
        t[m][n]= max(lcs(x,y,m-1,n),lcs(x,y,m,n-1))
        return t[m][n]
    
def printLcs(x,y,m,n):
    lcs(x,y,m,n)
    #print(t)
   
    i = m
    j =n
    ans = ""
    while i >0 and j>0 :
        if x[i-1] ==y[j-1]:
           # print("working...")
            ans+= x[i-1]
            j -=1
            i-=1
        else :
            if t[i-1][j] > t[i][j-1]:
                i-=1
            else :
                j-=1
    return ans[::-1]                     

a = "abcde"   
b= "abczx"


m = len(a)
n = len(b)



for i in range(m+1):
    col =[]
    for j in range(n+1):
        col.append(-1)
    t.append(col)    
print(lcs(a,b,m,n))
print(printLcs(a,b,m,n)) 