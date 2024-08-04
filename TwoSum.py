def TwoSum(num):
    target=6
    n=len(num)
    for i in range(n-1):
        for j in range(i+1,n):
            if num[i]+num[j]==target:
                return([i,j])
num=[3,2,4]
print(TwoSum(num))
