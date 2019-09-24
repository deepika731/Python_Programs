var_1 = input("enter a string here:\t")
if(var_1.find("an") != -1):
	var_2 = input("enter another string here:\t")
	if(len(var_2) >= 2):
		var_1 = var_1.replace("an", var_2[0:2])
print(var_1)
