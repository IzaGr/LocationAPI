import urllib.request
import json

api = 'https://elevation-api.io/api/elevation?points='

               
def elevation(long, lati):
    try:
        elev_request = '({},{})'.format(long,lati)
        request = api + elev_request
        response = urllib.request.urlopen(request).read()
        elevation = json.loads(response)
        elev_result = elevation['elevations'][0]['elevation']
    except:
        print("Problem with collecting your elevation")
    return elev_result                 

 
    
    
