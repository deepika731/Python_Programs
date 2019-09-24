# Enter your code here. Read input from STDIN. Print output to STDOUT
def sum_subset(array, num):
    if num < 0:
        return
    if len(array) == 0:
        if num == 0:
            yield []
        return
    for solution in sum_subset(array[1:], num):
        yield solution
    for solution in sum_subset(array[1:], num - array[0]):
        yield [array[0]] + solution
    

def minimum_sum(n):
    if(n <= 8):
        return -1
    elif(n % 9 == 0):
        return int(n/9)
    elif(n % 10 == 9):
        return 1
    else:
        r = n % 10
        k = 9 - r
        f = (n - 10 + k)
        l = []
        print(f)
        for i in range(f,8,-10):
            l.append(i)
        return len(list(sum_subset(l,n))[0])
        
        
        

        
        
t = int(input())
for i in range(t):
    n = int(input())
    minimum = minimum_sum(n)
    print(minimum)
