# RECURSION EXAMPLES

# Example 1: Factorial
# Source: Hetland

def factorial(n):
	result = n
	for i in range(1,n):
		result *= i
	return result

def factorial(n):
	if n == 1:
		return 1
	else:
		return n * factorial(n-1)


# Example 2: Power
# Source: Hetland

def power(x, n):
	result = 1
	for i in range(n):
		result *= x
	return result

def power(x, n):
	if n == 0:
		return 1
	else:
		return x * power(x, n-1)


# Example 3: Binary Search
# Hetland

def search(sequence, number, lower, upper):
	if lower == upper:
		assert number == sequence[upper]
		return upper
	else:
		middle = (lower + upper) // 2
		if number > sequence[middle]:
			return search(sequence, number, middle+1, upper)
		else:
			return search(sequence, number, lower, middle)
