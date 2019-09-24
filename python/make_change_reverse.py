def div_mod(a,b):
	d = a // b
	r = a % b
	return (d,r)
def make_change(cents):
	quarter, remain_cents = div_mod(cents, 25)
	dimes, remain_cents = div_mod(remain_cents, 10)
	nickels, remain_cents = div_mod(remain_cents, 5)
	pennies, remain_cents = div_mod(remain_cents, 1)
	print("quaters {}, dimes {}, nickels {}, pennies {}".format(quarter,dimes,nickels,pennies))
def append_ones(num, ones):
	return (num * 10 + ones)
def reverse_int(num):
	reverse_num = 0
	while(num > 0):
		num, r = div_mod(num, 10)
		reverse_num = append_ones(reverse_num, r)
	return reverse_num
def main():
	cents = int(input("enter number of cents:\t"))
	make_change(cents)
	make_change(reverse_int(cents))
main()
