'''
Multiline regular expressions with python requests module

http://stackoverflow.com/questions/26597009/multiline-regular-expressions-with-python-requests-module

I am iterating over a web page line by line using requests, 
but trying # to capture some multi-line regular expressions:
'''

import requests

r = requests.get(url)

for line in r.iter_lines(): 
    pat = re.search(regex, line)
    if pat:
        print pat.group(1)

'''
I have tried concatenating the whole file into one long string, 
but that seems wrong.

What is the best way to capture these mult-line expressions 
(preferably using requests)?
'''

# Rob suggested:

r = requests.get(url)
pat = re.search(regex, r.text)

# It's working as: 

re.search(regex, r.text, re.DOTALL)