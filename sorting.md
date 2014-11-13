# Sort a list (from smallest to largest):

	>>> myList = [1, 3, 2]

	>>> sorted(myList)

	[1, 2, 3]


# Sort a list in reverse (ie, from largest to smallest):

	>>> myList = [1, 3, 2]

	>>> sorted(myList, reverse=True)

	[3, 2, 1]


# Sort a list of tuples by their elements:

	>>> myList = [(1, 4), (2, 3)]

	>>> sorted(myList, key=lambda x: x[1])

	[(2, 3), (1, 4)]

