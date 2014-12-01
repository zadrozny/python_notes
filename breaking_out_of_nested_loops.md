# Breaking out of nested loops [duplicate]

http://stackoverflow.com/q/653509/1366410

    Possible Duplicate:
    How to break out of multiple loops in Python?

Is there an easier way to break out of nested loops than throwing an exception? (In Perl, you can give labels to each loop and at least continue an outer loop.)

for x in range(10):
    for y in range(10):
        print x*y
        if x*y > 50:
            "break both loops"

I.e., is there a nicer way than:

class BreakIt(Exception): pass

try:
    for x in range(10):
        for y in range(10):
            print x*y
            if x*y > 50:
                raise BreakIt
except BreakIt:
    pass



asked Mar 17 '09 at 9:24 by Michael Kuhn





It has at least been suggested, but also rejected. I don't think there is another way, short of repeating the test or re-organizing the code. It is sometimes a bit annoying.

In the rejection message, Mr van Rossum mentions using return, which is really sensible and something I need to remember personally. :)




for x in xrange(10):
    for y in xrange(10):
        print x*y
        if x*y > 50:
            break
    else:
        continue  # executed if the loop ended normally (no break)
    break  # executed if 'continue' was skipped (break)

The same works for deeper loops:

for x in xrange(10):
    for y in xrange(10):
        for z in xrange(10):
            print x,y,z
            if x*y*z == 30:
                break
        else:
            continue
        break
    else:
        continue
    break




	
answered Mar 17 '09 at 12:27 by Markus Jarderot

