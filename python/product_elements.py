n = int(input("enter the length of the array:\t"))
l = []
for i in range(n):
	ele = int(input("enter element:\t"))
	l.append(ele)
product_array = 1
for i in l:
	product_array = product_array * i
output_l = []
for i in range(0,len(l)):
	output_l.append(product_array // l[i])
print(output_l)
