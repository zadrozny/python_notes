# THE CONJUNCTION OF SORTED AND ENUMERATE

# Start with an unsorted list:
lst = (1, 2, 1)


# Iterating over it, the order is preserved
for element in lst: 
	print element


# Sorting then iterating, we get the sorted order
for element in sorted(lst): 
	print element


# However if we both sort and enumerate, we get the new order, 
# while the indices continue to point to the original list. Strange.
for i, element in enumerate(sorted(lst)): 
	print element, lst[i]