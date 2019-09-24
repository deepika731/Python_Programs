x1 = int(input("starting diatance of kangroo 1:\t"))
v1 = int(input("jumps per 1 time of kangaroo 1:\t"))
x2 = int(input("starting distance of kangaroo 2:\t"))
v2 = int(input("jumps per 1 time of kangaroo 2:\t"))
distance = abs(x2 - x1)
time = abs(v2 - v1)
if(distance % time == 0):
	print("YES")
else:
	print("NO")

