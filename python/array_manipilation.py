n = int(input("enter the length of the array:\t"))
l = []
m = int(input("enter no of queries:\t"))
temp = [0] * (n + 2)
for i in range(m):
	left = int(input("enter left index:\t"))
	right = int(input("enter right index:\t"))
	k = int(input("enter k value:\t:"))
	temp[left] += k
	temp[right + 1] -= k
for i in range(1, n+1):
	temp[i] += temp[i - 1]
print(temp)
print("the max number is:\t",max(temp))

