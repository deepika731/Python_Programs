n = int(input("enter the length of the array:\t"))
l = []
for i in range(n):
	ele = int(input("enter element:\t"))
	l.append(ele)
r_sum = int(input("enter the sum:\t"))
found = set()
output = set()
for num in l:
	k = r_sum - num
	if k not in found:
		found.add(num)
	else:
		output.add((min(num,k), max(num, k)))
print(output)
