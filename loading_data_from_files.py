# Calculate the average household income in NYS from
# a dataset containing a bunch of extraneous crap

# The problem is trivial. The question is, for a large dataset, 
# is there any way to load it row by row without 
# without overhwelming memory? 

# The generator in the second approach presumably does nothing
# because the file must still be opened, loaded, and closed 
# (not to mention, the code is incredibly verbose). 


data ='data.txt'


incomes = [int(line.split("|")[-1].strip()) # Household income last element
			for line in open(data,'r').readlines()[2:] # Skip headers
			if line.split("|")[-1].strip().isalnum()]  # Skip bullshit entries

avg_income = sum(incomes) / len(incomes)

print avg_income




# Second approach: using a generator

with open(data) as f:
	x = (line for line in f.readlines()[2:])


sum_of_incomes = 0
i = 0
while True:

	try: 
		val = next(x).split("|")[-1].strip()

		if val.isalnum():
			sum_of_incomes += int(val)
			i += 1

	except StopIteration: 
		break 


avg_income = sum_of_incomes / i

print avg_income




# Third approach: iterate over the file line by line

sum_of_incomes = 0
i = 0
with open(data) as f:
	for line in f:
		val = line.split("|")[-1].strip()
		if val.isalnum():
			try: 
				sum_of_incomes += int(val)
				i += 1
			except ValueError:
				pass

avg_income = sum_of_incomes / i

print avg_income


