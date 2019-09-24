n = int(input("enter the length of the array:"))
l = []
for i in range(n):
	ele = int(input("enter element:"))
	l.append(ele)


def mergeSort(arr):
	if len(arr) == 1:
		return arr, 0
	else:
		k = int(len(arr)/2)
		a = arr[:k]
		b = arr[k:]
		a, ai = mergeSort(a)
		b, bi = mergeSort(b)
		
		c = []
		i = 0
		j = 0
		inversions = 0 + ai + bi
		while i < len(a) and j < len(b):
			if a[i] < b[j]:
				c.append(a[i])
				i = i + 1
			else:
				c.append(b[j])
				j = j + 1
				inversions += len(a) - i
		c += a[i:]
		c += b[j:]
	return c, inversions
l = mergeSort(l)
print(l)
