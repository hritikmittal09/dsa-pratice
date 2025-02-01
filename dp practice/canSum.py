def canSum(nums :list[int] , x : int,n : int, memo = {}, pos =0):
    if x in memo :
        return memo[x]
    if x ==0 :
        return True
    elif x <0 :
        return False
    for i in nums :
        reminder = x - i
        if( canSum(nums,reminder,n,memo)) :
            memo[x ] =True
            return True
    memo [x] =False
    return False        

                

nums = [5,3,4,7]
target =7
n =len(nums)
result : bool = canSum(nums,target,n )
if result :
    print("subset exist with sum")
else :
    print("sum dost exist")    