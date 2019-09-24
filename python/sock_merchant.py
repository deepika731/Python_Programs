n = int(input("enter lenght of the array:"))
l = []
for i in range(n):
	ele = int(input("enter element:"))
	l.append(ele)
d = {}
sock_count = 0
for i in l:
	if i in d.keys():
		d[i] = d[i] + 1
	else:
		d[i] = 1
	if(d[i] == 2):
		sock_count += 1
		d[i] = 0
print(sock_count)
