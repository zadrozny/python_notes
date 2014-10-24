# Four differnt ways of taking the product of a list, 
# tested for running time.

def multiply_1(lst):
	'''Return the product of a list using a for loop.'''
	product = 1 
	for term in lst:
		product *= term
	return product 



def multiply_2(lst):
	'''Return the product of a list using while and pop.'''
	product = 1
	while lst:
		product *= lst.pop()
	return product



def multiply_3(lst):
	'''Return the product of a list using reduce and lambda.'''
	return reduce(lambda x, y: x*y, lst)



def multiply_4(lst):
	'''Return the product of a list using reduce, lambda, and operator.mul.'''
	from operator import mul
	return reduce(lambda x, y: mul(x, y), lst)


