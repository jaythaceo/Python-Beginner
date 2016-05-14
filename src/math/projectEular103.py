
def scale(data, factor):
	"""Multiply all entries of numeric data list by the given factor"""
	for j in range(len(data)):
		data[j] *= factor

lister = [11,32,42]
print(scale(lister))