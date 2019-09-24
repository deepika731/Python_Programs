n = int(input("enter the size of the array:\t"))
l = []
for i in range(n):
	ele = int(input("enter element:"))
	l.append(ele)
d = int(input("enter day:\t"))
m = int(input("enter month:\t"))
left = 0
right = 0
t = []
count = 0
for i in range(0,n-m+1):
	k = l[i:i+m]
	print(k)
	if(sum(l[i:i+m]) == d):
		count += 1
print(count)	
