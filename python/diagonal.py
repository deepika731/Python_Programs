def diagonalDifference(arr):
    # Write your code here
    diagonal1 = 0
    diagonal2 = 0
    for i in range(len(arr)):
        for j in range(len(arr)):
            if(i == j):
                diagonal1 += arr[i][j]
            if(i + j == len(arr) - 1):
                diagonal2 += arr[i][j]
    print(diagonal1)
    print(diagonal2)
    difference = abs(diagonal1 - diagonal2)
    return difference
arr = []
n = int(input("enter size:\t"))
for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))
result = diagonalDifference(arr)
print(result)
	
