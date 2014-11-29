>>> 'hello world'[::-1] 
'dlrow olleh'

This is extended slice syntax. It works by doing [begin:end:step] - by leaving
begin and end off and specifying a step of -1, it reverses a string.

answered May 31 '09 at 2:11 
Paolo Bergantino
http://stackoverflow.com/a/931095/1366410


# ***********************************************************************

@Paolo's s[::-1] is fastest; a slower approach (maybe more readable, but
@that's debatable) approach is ''.join(reversed(s)).


answered May 31 '09 at 2:13 
Alex Martelli
http://stackoverflow.com/a/931099/1366410
