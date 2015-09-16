#! /usr/bin/env python
# Jesse Bacon
# Code to accompany the Financial Analysis section of my book
import requests, sqlite3, requests, urllib, os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import locale
import plotly.plotly as ply

locale.setlocale( locale.LC_ALL, 'en_US.UTF-8' ) 

def build_currency_table():
    target = 'https://inventory.data.gov/dataset/2b1dcd52-058e-410f-b656-f35962738c4f/resource/72a33ebb-3efe-455b-9e41-0733aaed7780/download/userssharedsdfannualproductionfgrsuscurrency.csv'
    with open('currency.csv', 'wb') as f:
        c_data = requests.get(target)
        c_values = c_data.content
        f.write(c_values)
    
def remove_nans(series):
    series_conversion = []
    for i in series:
        if str(i) in ['nan','N/A', ' N/A']:
            i = 0
            series_conversion.append(i)
        else:
            series_conversion.append(locale.atoi(i))
    return series_conversion

def plot_currency_distributions():
    df = pd.DataFrame.from_csv('currency.csv')
    plot = plt.figure()
    plt.title('Total Printed Currency Values for 1980-2012')
    plt.axis([1,32,0,9000000000])
    plt.xlabel('Years')
    plt.ylabel('Billions')

    Ones = df['$1 Bills']
    plot_ones = remove_nans(Ones)

    Twos = df['$2 Bills']    
    plot_twos = remove_nans(Twos)

    Fives = df['$5 Bills']
    plot_fives = remove_nans(Fives)

    Tens = df['$10 Bills']
    plot_tens = remove_nans(Tens)

    Twenties = df['$20 Bills']
    plot_twenties = remove_nans(Twenties)

    Fifties = df['$50 Bills']
    plot_fifties = remove_nans(Fifties)

    Hundreds = df['$100 Bills']
    plot_hundreds = remove_nans(Hundreds)

    plt.xticks(range(0,32), range(1980,2013), rotation='vertical')
    plt.plot(plot_ones, lw=2, color='0.75', label='Ones')
    plt.plot(plot_twos, lw=2, color='m', label='Twos')
    plt.plot(plot_fives, lw=2, color='c', label='Fives')
    plt.plot(plot_tens, lw=2, color='g', label='Tens')
    plt.plot(plot_twenties, lw=2, color='r', label='Twenties')
    plt.plot(plot_fifties, lw=2, color='y', label='Fifties')
    plt.plot(plot_hundreds, lw=2, color='k', label='Hundreds')
    plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
    plt.show()

class CFPB_Data_tool():
    
    global api_endpoint
    global formats
    global categories

    api_endpoint = 'http://data.consumerfinance.gov/api/views'
    formats = ['json', 'xml', 'csv']
    categories = {
        'Consumer complaints (all categories)':'s6ew-h6mp',
        'Bank accounts or services':'t9fg-cqmi',
        'Credit cards':'7zpz-7ury',
        'Credit reporting':'xa48-juie',
        'Debt collection':'ckyu-ku28',
        'Money transfers':'uha4-cwwn',
        'Mortgages':'g5qz-smft',
        'Other financial services':'b239-tvpx',
        'Payday loans':'6hp8-hzag',
        'Prepaid cards':'6yuf-367p',
        'Student loans':'eew7-9yf2',
        'Vehicle or other consumer loans':'wfbn-zkat',
    }
    
    def __init__(self):
        self.api_endpoint = api_endpoint
        self.formats = formats
        self.categories = categories
        
    def request_by_category(self, category, return_format):
        data_object = requests.get( api_endpoint + '/' + category + '/' + 'rows.' + return_format )
        for item in data_object.headers:
            print(item, data_object.headers[item])
        return data_object.content
    
    def Build_CFPB_DB_FILES(self):
        try:
            for category in instance.categories.keys():
                cat_var = instance.request_by_category(instance.categories[category], 'csv')
                with open('%s.csv' % category, 'wb') as f:
                    f.write(cat_var)
                    del(cat_var)
                print('wrote %s.csv' % category)
        except:
            print('Could not grab all data')
    
    def create_sqlite3_db(self):
        conn = sqlite3.connect('CFPB.db')
        c = conn.cursor()
        for file_name in os.listdir('./'):
            if str(file_name).endswith('csv'):
                df = pd.read_csv(file_name, encoding='utf-8')
                df.to_sql(file_name[:-4], conn, if_exists='append', index=False,)
        c.close()

    def list_sql_tables(self):
        c.execute("SELECT name FROM sqlite_master WHERE type='table';")
        print(c.fetchall())