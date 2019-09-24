def merge(array, left, middle, right):
	len1 = middle - left + 1
	len2 = right - middle
	
	Left_array = [0] * len1
	Right_array = [0] * len2
	
	for i in range(len1):
		Left_array[i] = array[left + i]
	for j in range(len2):
		Right_array[j] = array[middle + 1 + j]
	
	i = 0
	j = 0
	k = left
	
	while(i < len1 and j < len2):
		if(Left_array[i] < Right_array[j]):
			array[k] = Left_array[i]
			i += 1
		else:
			array[k] = Right_array[j]
			j += 1
		k += 1
	while(i < len1):
		array[k] = Left_array[i]
		i += 1
		k += 1
	while(j < len2):
		array[k] = Right_array[j]
		j += 1
		k += 1


def mergeSort(array, left, right):
	if(left < right):
		middle = int((left + (right - 1))/2)
		
		mergeSort(array, left, middle)
		mergeSort(array, middle + 1, right)
		merge(array, left, middle, right)




array = []
length = int(input("enter the size of the array:\t"))
for i in range(length):
	element = int(input("enter element:\t"))
	array.append(element)
print("original array is:")
for i in range(length):
	print(array[i], end = "\t")
print("\n")
mergeSort(array, 0, length - 1)

print("sorted array is:")
for i in range(length):
	print(array[i], end = "\t")
print("\n")

