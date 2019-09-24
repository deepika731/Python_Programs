n = int(input("enter the length of the array:\t"))
l = []
for i in range(n):
	ele = int(input("enter element:\t"))
	l.append(ele)
sum_l = []
sum = 0
for i in range(n):
	sum = sum + l[i]
	sum_l.append(sum)
flag = 0
for i in range(1,n):
	left = sum_l[i - 1]
	print("left",left)
	right = abs(sum_l[n-1] - sum_l[i])
	print("right",right)
	if(left == right):
		flag = 1
		print("the equilibrium point is : {}".format(l[i]))
		break
if(flag == 0):
	print("There is no equilibrium point")

