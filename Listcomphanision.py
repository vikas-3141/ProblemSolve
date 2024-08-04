x=int(input("Enter the x number"))
y=int(input("Enter the y number"))
z=int(input("Enter the z number"))
n=int(input("Enter the number to print"))

result=[[i,j,k] for i in range(x+1) for j in range(y+1)  for k in range(z+1)  if i+j+k != n ]
print(result)