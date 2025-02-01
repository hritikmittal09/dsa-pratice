# in unbouned knapak we cantake intence as many as we wanr and once we reject item we cannot take it
def ropecutting(n : int , price : list[int],length: list[int]):
    # when we fixiably to cut rod from 1-n we can from a dp tale of n+1xn+1
    # else we cam form size +1 x n+1
    t = []
    for i in range(n+1):
        col = []
        for j in range(n+1):
            col.append(-1)
        t.append(col)
    for i in range(n+1):
        for j in range(n+1):
            if i ==0 or j ==0 :
                t[i][j] =0
    for i in range(1,n+1):
        for j in range(1,n+1):
            if length[n-1] <= j:
                t[i][j] = max(price[i-1]+t[i][j-length[i-1]],t[i-1][j])
            else :
                t[i][j] = t[i-1][j]
    return t[n][n]
length = [1,2,3,4,5,6,7,8]
price = [1,5,8,9,10,17,17,20]
n =8
res = ropecutting(n,price,length)
print(res)
                                   


