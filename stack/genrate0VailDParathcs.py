# https://www.youtube.com/watch?v=0OS8705nB40
res =[]
n = 2
def dfs(l,r,s):
    if len(s) ==2*n:
        res.append(s)
        return
    if l <n :
         dfs(l+1,r,s+'(')
    if r <l :
         dfs(l,r+1,s+')')
dfs(0,0,"")  
print(res)  
    
    
