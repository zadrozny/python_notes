# I asked on SO: http://stackoverflow.com/q/26982312/1366410

# Is there a way to assign a condition to a variable in Python?

# Specifically, I am writing a generator that is infinite by default, limited by choice. This code works but the duplication is ugly:


def generate(start=0, stop=None):
    i = start

    if stop == None:
        while True:
            yield i
            i += 1
    else:
        while i <= stop:
            yield i
            i += 1


# Specifically, I would like to express something like this:

def generate(start=0, stop=None):
    i = start

    if stop == None:
        condition = True
    else:
        condition = 'i <= stop' # Of course, this will throw an error

    while condition:
        yield i
        i += 1


# What is the best way to accomplish this?



# @dano recommended using 'or':

def generator4(start=0, stop=None):
	i = start

	while stop is None or i <= stop:
		yield i
		i += 1

# @anders-waldenborg recommended using lambda

def generator3(start=0, stop=None):
	i = start

	if stop == None:
		condition = True
	else:
		condition = lambda x: x <= stop 

	while condition(i):
		yield i
		i += 1

# @dano cautioned: Also, I think the only other alternatives would involve adding a function call to the while loop. Function calls are very expensive in Python, and probably add more overhead than an extra check to the while loop.