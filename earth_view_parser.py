from urllib.request import urlopen
from urllib.error import HTTPError
from json import dumps
from bs4 import BeautifulSoup
import time

result = []
file = open('earthview.json','a')

for x in range(1000, 7030):
    x = str(x)
    try:
        response = urlopen('https://earthview.withgoogle.com/' + x)
        if response.getcode() == 200:
            start = time.time()
            
            data = response.read()
            html = BeautifulSoup(data,"html.parser")
            Region = str((html.find("div", class_="content__location__region")).text)
            Country = str((html.find("div", class_="content__location__country")).text)
            Everything = html.find("a", id="globe", href=True)
            GMapsURL = Everything['href']
            Image = 'https://www.gstatic.com/prettyearth/assets/full/' + x + '.jpg'
            result.append({'region': Region, 'country': Country, 'map': GMapsURL, 'image': Image})

            print("Fetched -> | " + x + " | in " + "{0:.3f}".format(time.time() - start) + " sec" )
    
    except (HTTPError,AttributeError):
        continue #If the page is 404, then just continue

final_file = dumps(result,indent=4) #Dump the json file finally
file.write(final_file)            
file.close()
