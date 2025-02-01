
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