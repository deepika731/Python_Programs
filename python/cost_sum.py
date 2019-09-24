n = int(input())
c1 = int(input())
c2 = int(input())
i = 1
d = {}
while(i * i <= n):
	if(n%i == 0):
		d[i] = int(n/i)
	i = i + 1
print(d)
m = len(d)
ans = [0 for i in range(m)]
wys = [0 for i in range(m)]

ans[0] = 0
ans[1] = 1
k =  list(d.keys())
for last in range(1,len(k)):
	for prev in range(last):
		if(d[k[last]] % d[k[prev]] == 0):
			cost = ans[prev] + c1 + c2 * (d[k[last]] / d[k[prev]] -1)
			if(cost == ans[last]):
				wys[last] += wys[prev]
			elif(cost < ans[last]):
				wys[last] = wys[prev]
				ans[last] = cost
print(ans[m-1])
print(wys[m-1])
