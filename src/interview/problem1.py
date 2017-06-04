

def add_nums(a, b):
	if a is None or b is None or a < 0 and b < 0:
		return False
	if b == 0:
		print a
		return 
	sum = a ^ b 
	car = (a & b) << 1
	add_nums(sum, car)

add_nums(123,1)