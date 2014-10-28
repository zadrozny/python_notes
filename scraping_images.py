'''
Notes on scraping images

Sources: 
	Answer to "How to download image using request": 
		http://stackoverflow.com/a/13137873/1366410
'''


# This needs to be dynamic, 
# otherwise successive images will overwrite. 
# Need to write a regular expression to extract image name / description

url = r'http://metmuseum.com/~/media/Images/Exhibitions/2014/Treasures%20from%20India/JewelsIndia_WEB_2.jpg?mw=481'

path = 'image.jpg' 

'''

You can either use the response.raw file object, or .iter_content(), and iterate over the response.

To use the response.raw file-like object will not, by default, decode 
compressed responses (with GZIP or deflate). You can force it to decompress 
for you anyway by setting the decode_content attribute to True (requests sets
	it to False to control decoding itself). You can then use shutil.copyfileobj() to have Python stream the data to a file object:
'''

def method_1(url, path):
	import requests
	import shutil
	r = requests.get(url, stream=True)
	if r.status_code == 200:
	    with open(path, 'wb') as f:
	        r.raw.decode_content = True
	        shutil.copyfileobj(r.raw, f)  


method_1(url, path)

'''
To iterate over the response with respones.iter_content() use a loop; the method ensures that data is decompressed by this stage:
'''

def method_2():
	import requests
	r = requests.get(url, stream=True)
	if r.status_code == 200:
	    with open(path, 'wb') as f:
	        for chunk in r.iter_content():
	            f.write(chunk)

'''
This'll read the data in 128 byte chunks; if you feel another 
chunk size works better, do use .iter_content() with a custom chunk size:
'''
def method_3(url):
	r = requests.get(settings.STATICMAP_URL.format(**data), stream=True)
	if r.status_code == 200:
	    with open(path, 'wb') as f:
	        for chunk in r.iter_content(1024):
	            f.write(chunk)

'''
Note that you need to open the destination file in binary mode to ensure 
python doesn't try and translate newlines for you. We also set stream=True 
so that requests doesn't download the whole image into memory first.
'''