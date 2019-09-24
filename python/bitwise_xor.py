n = int(input())
ans = 0
idx = [0 for i in range(50)]
arr = [1, 2, 3, 4, 5]
def solve(arr):
    answer = 0
    subarrays = []
    for x in arr:
        subarrays.append(0)
        subarrays2 = []
        for y in subarrays:
            subarrays2.append(x|y)
            answer += x|y
        subarrays = subarrays2
    return answer
print(solve(arr))

