from urllib.request import urlopen,urlretrieve
from urllib.error import HTTPError
from bs4 import BeautifulSoup
import time,os

for x in range(1000, 7030):
    x = str(x)
    try:
        response = urlopen('https://earthview.withgoogle.com/' + x)
        if response.getcode() == 200:
            start = time.time()
            
            data = response.read()
            html = BeautifulSoup(data,"html.parser")
            Everything = html.find("a", id="globe", href=True)
            GMapsURL = Everything['href']
            Image = 'https://www.gstatic.com/prettyearth/assets/full/' + x + '.jpg'
            if not os.path.isfile(os.path.join('images',Image.split('/')[-1])) : # for download resume
                urlretrieve(Image, os.path.join('images',Image.split('/')[-1]) )

            print("Fetched -> | " + x + " | in " + "{0:.3f}".format(time.time() - start) + " sec" )
    
    except (HTTPError,AttributeError):
        continue #If the page is 404, then just continue
