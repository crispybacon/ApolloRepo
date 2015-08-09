#!/usr/bin/env python
#Tools to widgetize for NASA Open Data
import pandas, matplotlib, json, urllib, numpy, PIL
from PIL import Image as img
import matplotlib.pyplot as plt
from IPython.display import SVG, Image, HTML
from PIL.ExifTags import TAGS
#APOD
def APOD(date, concept_tags):
    """
    One of the most popular websites at NASA is the Astronomy Picture of the Day. In fact, this website is one of the most popular websites across all federal agencies. It has the popular appeal of a Justin Bieber video. This endpoint structures the APOD imagery and associated metadata so that it can be repurposed for other applications. In addition, if the concept_tags parameter is set to True, then keywords derived from the image explanation are returned. These keywords could be used as auto-generated hashtags for twitter or instagram feeds; but generally help with discoverability of relevant imagery.
    APOD

    GET https://api.data.gov/nasa/planetary/apod

    Query Parameters

    Paramter        Type        Default     Description
    date	        YYYY-MM-DD	today	    The date of the APOD image to retrieve
    concept_tags	bool	    False	    Return an ordered dictionary of concepts from the APOD explanation
    api_key	        string	    DEMO_KEY	api.data.gov key for expanded usage

    EXAMPLE QUERY

    https://api.data.gov/nasa/planetary/apod?concept_tags=True&api_key=DEMO_KEY
    """
    request='https://api.data.gov/nasa/planetary/apod'
    key=''
    form={'date': date, 'concept_tags': concept_tags, 'api_key': key}
    query=urllib.urlencode(form)
    APOD_request=urllib.urlopen(request+"?"+query)
    print(APOD_request.info())
    response=json.loads(APOD_request.read())
    print('Title: ' + response['title'])
    print('Date: ' + response['date'])
    print('Explanation: '+ response['explanation'])
    print('URL : ' + response['url'])
    fname=str('APOD'+'_'+date+'.jpg')
    apod_img=urllib.urlretrieve(response['url'], fname)
    im=img.open(fname)
    display=plt.imread(fname)
    plt.imshow(display)
    PIL_format=PIL.Image.open(fname)
    exif_data = PIL_format._getexif()
    #print(exif_data)
    ret = {}
    for tag, value in exif_data.items():
        decoded = TAGS.get(tag, tag)
        ret[decoded] = value
    return ret
def geocode(address):
    """
    Return Lat/Long of an Address from Google
    """
    form = {"address": address, "sensor": "false",}
    google_req = "https://maps.googleapis.com/maps/api/geocode/json"
    query = urllib.urlencode(form)
    base_req=(google_req+"?"+query)
    geocode=urllib.urlopen(base_req)
    print(geocode.headers)
    response=json.loads(geocode.read().decode('UTF-8'))
    print('Address: '+ response['results'][0]['formatted_address'])
    point=response['results'][0]['geometry']['location']
    print(point)
    return point['lat'], point['lng']
def landsat8(lat, lon, dim, cloud_score, target_date):
    """
    Imagery
    This endpoint retrieves the Landsat 8 image for the supplied location and date. The response will include the date and URL to the image that is closest to the supplied date. The requested resource may not be available for the exact date in the request. You can retrieve a list of available resources through the assets endpoint.
    The cloud score is an optional calculation that returns the percentage of the queried image that is covered by clouds. If False is supplied to the cloud_score parameter, then no keypair is returned. If True is supplied, then a keypair will always be returned, even if the backend algorithm is not able to calculate a score. Note that this is a rough calculation, mainly used to filter out exceedingly cloudy images.
    QUERY PARAMETERS
    Parameter	Type	    Default	    Description
    lat	        float	    n/a	        Latitude
    lon	        float	    n/a	        Longitude
    dim	        float	    0.025	    width and height of image in degrees
    cloud_score	bool	    False	    calculate the percentage of the image covered by clouds
    api_key	    string	    DEMO_KEY	api.data.gov key for expanded usage
    date	    YYYY-MM-DD	today	    date of image; if not supplied, then the most recent image (i.e., closest to today) is returned
    landsat8('34.183578', '-118.9491215', '0.07', 'True', '2014-07-31')
    x=geocode('700 Pennsylvania Avenue NW DC')
    landsat8(x[0], x[1], '0.07', 'True', '2014-07-31')
    """
    request='https://api.data.gov/nasa/planetary/earth/imagery'
    key=''
    form={'lat': str(lat), 'lon': str(lon), 'dim': dim, 'cloud_score': cloud_score, 'date': target_date, 'api_key': key}
    query=urllib.urlencode(form)
    landsat8_request_string=urllib.urlopen(request+"?"+query)
    print(landsat8_request_string.info())
    response=json.loads(landsat8_request_string.read())
    print('date: ' + response['date'])
    print('cloud score: ' + str(response['cloud_score']))
    print('Planet: ' + response['resource']['planet'])
    print('Data Set: ' + response['resource']['dataset'])
    print('ID: ' + str(response['id']))
    print('URL: ' + str(response['url']))
    fname=str('landsat8'+'_'+target_date+'.png')
    landsat8_img=urllib.urlretrieve(response['url'], fname)
    im=img.open(fname)
    display=plt.imread(fname)
    plt.imshow(display)
    PIL_format=PIL.Image.open(fname)
def Assets(lat, lon, begin, end):
    """
    Hey, Charlie, when was the last time a NASA image was taken of my house? This endpoint retrieves the date-times and asset names for available imagery for a supplied location. The satellite passes over each point on earth roughly once every sixteen days. This is an amazing visualization of the acquisition pattern for Landsat 8 imagery. The objective of this endpoint is primarily to support the use of the imagery endpoint.
    GET https://api.data.gov/nasa/planetary/earth/assets

    QUERY PARAMETERS

    Parameter	Type	    Default	    Description
    lat	        float	    n/a	        Latitude
    lon	        float	    n/a	        Longitude
    begin	    YYYY-MM-DD	n/a	        beginning of date range
    end	        YYYY-MM-DD	today	    end of date range
    api_key	    string	    DEMO_KEY	api.data.gov key for expanded usage

    EXAMPLE QUERY
 https://api.data.gov/nasa/planetary/earth/assets?lon=100.75&lat=1.5&begin=2014-02-01&api_key=DEMO_KEY
    """
    request='https://api.data.gov/nasa/planetary/earth/assets'
    key=''
    form={'lat': str(lat), 'lon': str(lon), 'begin': begin, 'end': end, 'api_key': key}
    query=urllib.urlencode(form)
    landsat8_request_string=urllib.urlopen(request+"?"+query)
    print(landsat8_request_string.info())
    response=json.loads(landsat8_request_string.read())
    #print(response.keys())
    #print(response.values())
    print('From: '+ begin)
    print('To: ' + end)
    print('Number of Satellite passes: ' + str(response['count']))
    print('Planet: ' + response['resource']['planet'])
    print('Data Set: ' + response['resource']['dataset'])
    for item in response['results']:
        print('date: ' + item['date'])
        print('id: ' + item['id'])
 def temperature_anomolies_address(begin, end, text):
    """
    There is no doubt that, on average, the earth is warming. However, the warming is spatially heterogenous. How much warmer (or cooler) is your hometown? This endpoint reports local temperature anomalies from the Goddard Institute for Space Studies Surface Temperature Analysis via the New Scientist web application to explore global temperature anomalies. This endpoint restructures the query and response to correspond to other APIs on api.nasa.gov. The developer supplies a location and date range, and the returned object is a list of dictionaries that is ready for visualization in the d3 framework.
    Address
    The location can be specified as an address string.

    HTTP REQUEST

    GET https://api.data.gov/nasa/planetary/earth/temperature/address

    QUERY PARAMETERS

    Parameter	Type	Default	    Description
    text        string	n/a	        Address string
    begin	    int	    1880	    beginning year for date range, inclusive
    end	        int	    2014	    end year for date range, inclusive
    api_key	    string	DEMO_KEY	api.data.gov key for expanded usage

    EXAMPLE QUERY

    https://api.data.gov/nasa/planetary/earth/temperature/address?text=1800 F Street, NW, Washington DC&begin=1990
    
    temperature_anomolies_address('1880', '2015', '20110')
    """
    request='https://api.data.gov/nasa/planetary/earth/temperature/address'
    key=''
    form={'begin':  str(begin), 'end': str(end), 'text': text, 'api_key': key}
    query=urllib.urlencode(form)
    temp_address_request_string=urllib.urlopen(request+"?"+query)
    print(temp_address_request_string.info())
    response=json.loads(temp_address_request_string.read())
    #print(response.keys())
    #print(response.values())
    return response
def plot_temps(begin, end, text):
    """
    Plot temperature variations to a line chart
    """
    response=temp_data=temperature_anomolies_address(begin, end, text)
    z=response['results']
    x=[]
    y=[]
    for item in z:
        y.append(item['anomaly'])
        x.append(item['year'])
    plt.ylabel('Temp Variation')
    plt.xlabel('Years')
    plt.plot(x,y)
 def temperature_anomolies_coordinates(begin, end, lat, lon):
    """
    Coordinates
    Alternatively, you can supply the precise latitude and longitude as the location.

    HTTP REQUEST

    GET https://api.data.gov/planetary/earth/temperature/coords

    QUERY PARAMETERS

    Parameter	Type	Default	    Description
    lat	        float	n/a	        Latitude
    lon	        float	n/a	        Longitude
    begin	    int	    1880	    beginning year for date range, inclusive
    end	        int	    2014	    end year for date range, inclusive
    api_key	    string	DEMO_KEY	api.data.gov key for expanded usage
    
    EXAMPLE QUERY

    https://api.data.gov/nasa/planetary/earth/temperature/coords?lon=100.3&lat=1.6&begin=1990&end=2005&api_key=DEMO_KEY
    """
    request='https://api.data.gov/nasa/planetary/earth/temperature/coords'
    key=''
    form={'begin':  str(begin), 'end': str(end), 'lat': lat, 'lon': lon, 'api_key': key}
    query=urllib.urlencode(form)
    temp_point_request_string=urllib.urlopen(request+"?"+query)
    print(temp_point_request_string.info())
    response=json.loads(temp_point_request_string.read())
    #print(response.keys())
    #print(response.values())
    return response
def plot_temps_points(begin, end, lat, lon):
    """
    Plot temperature variations to a line chart
    """
    response=temp_data=temperature_anomolies_coordinates(begin, end, lat, lon)
    z=response['results']
    x=[]
    y=[]
    for item in z:
        y.append(item['anomaly'])
        x.append(item['year'])
    plt.ylabel('Temp Variation')
    plt.xlabel('Years')
    plt.plot(x,y)
def patents(text, concept_tags):
    """
    The NASA patent portfolio is available to benefit US citizens. Through partnerships and licensing agreements with industry, these patents ensure that NASA’s investments in pioneering research find secondary uses that benefit the economy, create jobs, and improve quality of life. This endpoint provides structured, searchable developer access to NASA’s patents that have been curated to support technology transfer.

    HTTP REQUEST

    GET https://api.data.gov/nasa/patents

    QUERY PARAMETERS

    Parameter	    Type	 Default	Description
    query	        string	 None	    Search text to filter results
    concept_tags	bool	 False	    Return an ordered dictionary of concepts from the patent abstract
    limit	        int	     all	    number of patents to return
    api_key	string	DEMO_KEY	        api.data.gov key for expanded usage

    EXAMPLE QUERY

    https://api.data.gov/nasa/patents/content?query=temperature&limit=5&api_key=DEMO_KEY
    """
    request='https://api.data.gov/nasa/patents/content'
    key=''
    form={'query': text,'concepte_tags': concept_tags, 'api_key': key}
    query=urllib.urlencode(form)
    patent_request_string=urllib.urlopen(request+"?"+query)
    print(patent_request_string.info())
    response=json.loads(patent_request_string.read())
    #print(response.keys())
    #print(response.values())
    return response
