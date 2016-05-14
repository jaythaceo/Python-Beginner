squared = 2
cubed = 3
stringer = "People are stupid!"

def cubing(numbers):
	numbers = numbers ** squared
	return numbers

def square(numbers):
	numbers = numbers ** cubed
	return numbers

def slicer(something):
	something = something[2:-8]
	return something

print(slicer(stringer))