t = int(input())
for i in range(t):
    l = []
    countx = {}
    county = {}
    for j in range(5):
        x = int(input())
        y = int(input())
        if(x in countx):
            countx[x] = countx[x] + 1
        else:
            countx[x] = 1
        if(y in county):
            county[y] = county[y] + 1
        else:
            county[y] = 1
    print(countx)
    print(county)
    if(3 not in countx.values() and 3 not in county.values()):
        print("NO")
        continue
    temp1 = 0
    sum1 = 0
    for x, val in countx.items():
      if(val != 3):
        sum1 += x
      else:
        temp1 = x
    temp2 = 0
    sum2 = 0
    for x, val in county.items():
      if(val != 3):
        sum2 += x
      else:
        temp2 = x
    if(sum1/2 == temp1 or sum2/2 == temp2):
      print("YES")
    else:
      print("NO")
	
    
    
