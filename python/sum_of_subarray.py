n = int(input("enter the size of the array:\t"))
l = []
for i in range(n):
	ele = int(input("enter element:\t"))
	l.append(ele)
sum = int(input("enter the sum:\t"))
def subarray_sum(l,sum,n):
	left = 0
	right = 0
	currSum = 0
	while(1):
		if(right >= n - 1 and currSum < sum):
			return 0
		if(sum == currSum):
			return l[left:right]
		if(currSum < sum and right <= n-1):
			currSum = currSum + l[right]
			right = right + 1
			print("right",right)
		if(currSum > sum and left <= n-1):
			currSum = currSum - l[left]
			left = left + 1
			print("left",left)
			
if(subarray_sum(l,sum,n) == 0):
	print("There is no subarray with given sum")
else:
	print(subarray_sum(l,sum,n))
	

	
	
	
