n = int(input("enter the length of array:\t"))
l = []
for i in range(n):
	ele = int(input("enter element:\t"))
	l.append(ele)
for i in range(1,n):
	l[i] = l[i] + l[i - 1]
print(l)
left = int(input("enter left element:\t"))
right = int(input("enter right element:\t"))
if(left == 0):
	print("the sum is :\t",l[right])
else:
	print("the sum is:\t",l[right] - l[left - 1])
