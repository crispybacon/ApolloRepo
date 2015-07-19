#!/usr/bin/env python
import matplotlib.pyplot as plt
import prettyplotlib as pplt
import plotly.plotly as ply
from plotly.graph_objs import *
import time
import pandas, matplotlib, json, urllib, numpy, PIL
from PIL import Image as img
import matplotlib.pyplot as plt
from IPython.display import SVG, Image, HTML
from PIL.ExifTags import TAGS
import pandas as pd
def nhtsa_makes_for_year(modelYear):
    """
    """
    form = {"format": 'json'}
    base_url = "http://www.nhtsa.gov/webapi/api/Recalls/vehicle/"
    model_year = "modelyear/"+str(modelYear)+'/'
    query = urllib.urlencode(form)
    nhtsa_query=(base_url+model_year+"?"+query)
    print(nhtsa_query)
    raw_response=urllib.urlopen(nhtsa_query)
    response=json.loads(raw_response.read())
    return response
def nhtsa_models_for_year(modelYear, make):
    """
    """
    form = {"format": 'json'}
    base_url = "http://www.nhtsa.gov/webapi/api/Recalls/vehicle/"
    model_year = "modelyear/"+str(modelYear)+'/'
    make = "make/"+str(make)+"/"
    query =urllib.urlencode(form)
    nhtsa_query=(base_url+model_year+make+"?"+query)
    print(nhtsa_query)
    raw_response=urllib.urlopen(nhtsa_query)
    response=json.loads(raw_response.read())
    return response
def nhtsa_year_model(modelYear, make, model):
    """
    """
    form = {'year': modelYear, 'make': make, 'model': model, "format": 'json'}
    base_url = "http://www.nhtsa.gov/webapi/api/Recalls/vehicle"
    #model_year = "modelyear/"+str(modelYear)+'/'
    #make = "make/"+str(make)+"/"
    #model = "model/"+str(model)
    query = urllib.urlencode(form)
    #nhtsa_query=(base_url+model_year+make+model+"?"+query)
    nhtsa_query=(base_url+'?'+query)
    print(nhtsa_query)
    raw_response=urllib.urlopen(nhtsa_query)
    response=json.loads(raw_response.read())
    return response
def plot_year(year):
    ply.sign_in('jessembacon', 'fua03q4wye')
    year_makes=nhtsa_makes_for_year(year)
    makes=[]
    for i in range(len(year_makes['Results'])):
        makes.append(year_makes['Results'][i]['Make'])
    models = []
    trouble_makes=[]
    for make in makes:
        try:
            model=nhtsa_models_for_year(year, make)
            for item in model['Results']:
                models.append([item['Make'], item['Model'], item['ModelYear']])
        except:
            print("Could not retrieve recalls for %s" % make)
            trouble_makes.append([make, year])
    makes_dbs={}
    exclude = set([' ','-','/','\\','&'])
    for item in makes:
        item = str(item).replace(" ","").replace('-','_').replace('\\','').replace('//','').replace('\/','').replace('&','')
        makes_dbs[item]=0
    for item in models:
        try:
            print(item)
            make_name=(str(item[0]).replace(" ","").replace('-','_').replace('\\','').replace('//','').replace('\/','').replace('&',''))
            print(make_name)
            entry=nhtsa_year_model(item[2], item[0], item[1])
            print(entry['Count'])
            makes_dbs[make_name]+=entry['Count']
            time.sleep(0.25)
        except:
            print("Unable to count %s" % make_name) 
    a=makes_dbs.keys()
    b=makes_dbs.values()
    df=pd.DataFrame.from_dict(makes_dbs, 'index')
    df.columns=['Counts']
    fig=plt.figure()
    plt.plot(b, label=year)
    plt.title('Number of Recall Types Per Maker %s'%(year))
    plt.xlabel('Makers')
    plt.ylabel=('Recall Types')
    plt.legend()
    figname=str(year)+'.png'
    plt.savefig( figname, transparent=True)
    trace1 = Scatter(
    x=a,
    y=b
    )
    #trace2 = Scatter(
    #    x=[1, 2, 3, 4],
    #    y=[16, 5, 11, 9]
    #)
    data = Data([trace1])
    plot_url = ply.plot(data, filename='Number of Recall Types Per Maker %s'%(year))
    return trace1
def plot_year_no_web(year):
    year_makes=nhtsa_makes_for_year(year)
    makes=[]
    for i in range(len(year_makes['Results'])):
        makes.append(year_makes['Results'][i]['Make'])
    models = []
    trouble_makes=[]
    for make in makes:
        try:
            model=nhtsa_models_for_year(year, make)
            for item in model['Results']:
                models.append([item['Make'], item['Model'], item['ModelYear']])
        except:
            print("Could not retrieve recalls for %s" % make)
            trouble_makes.append([make, year])
    makes_dbs={}
    exclude = set([' ','-','/','\\','&'])
    for item in makes:
        item = str(item).replace(" ","").replace('-','_').replace('\\','').replace('//','').replace('\/','').replace('&','')
        makes_dbs[item]=0
    for item in models:
        try:
            print(item)
            make_name=(str(item[0]).replace(" ","").replace('-','_').replace('\\','').replace('//','').replace('\/','').replace('&',''))
            print(make_name)
            entry=nhtsa_year_model(item[2], item[0], item[1])
            print(entry['Count'])
            makes_dbs[make_name]+=entry['Count']
            time.sleep(0.25)
        except:
            print("Unable to count %s" % make_name) 
            time.sleep(0.25)
    a=makes_dbs.keys()
    b=makes_dbs.values()
    df=pd.DataFrame.from_dict(makes_dbs, 'index')
    df.columns=['Counts']
    fig=plt.figure()
    plt.plot(b, label=year)
    plt.title('Number of Recall Types Per Maker %s'%(year))
    plt.xlabel('Makers')
    plt.ylabel=('Recall Types')
    plt.legend()
    figname=str(year)+'.png'
    plt.savefig( figname, transparent=True)
    trace1 = Scatter(
    x=a,
    y=b
    )
    return trace1
def trace_multiple_years(start_year, end_year):
    traces=[]
    for year in range(start_year, end_year):
        trace_name=(str(trace)+'_'+str(year))
        print(trace_name)
        exec "%s = plot_year_no_web(year)" % (trace_name)
        exec "traces.append(%s)" % (trace_name)
    return traces
def plot_remaining_years(start_year, end_year):
    for year in range(int(start_year), int(end_year)):
        trace_name=(str('trace')+'_'+str(year))
        print(trace_name)
        exec "%s = plot_year_no_web(year)" % (trace_name)