from urllib.request import urlopen,urlretrieve
from urllib.error import HTTPError
import time,os

for x in range(1000, 7030):
    x = str(x)
    try:
        response = urlopen('https://earthview.withgoogle.com/' + x)
        if response.getcode() == 200:
            start = time.time()
            Image = 'https://www.gstatic.com/prettyearth/assets/full/' + x + '.jpg'
            if not os.path.isfile(os.path.join('images',Image.split('/')[-1])) : # for download resume
                urlretrieve(Image, os.path.join('images',Image.split('/')[-1]) )
                print("Fetched -> | " + x + " | in " + "{0:.4f}".format(time.time() - start) + " sec" )
            else :
                print("Already fetched! -> | " + x + " | ")
    
    except (HTTPError,AttributeError):
        continue #If the page is 404, then just continue
