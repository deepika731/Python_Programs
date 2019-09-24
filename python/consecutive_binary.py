number = int(input("enter number here:\t"))
count = 0
while(number != 0):
	shift_number = number << 1
	number = number & shift_number
	count = count + 1
print("maximum number of consecutive 1s is ",count)
	
