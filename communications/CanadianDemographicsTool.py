#! A Tool By Jesse Bacon to research business demographics in Canada 9/1/2015
import time

class sandbox():
    '''
    Yellow Pages Canada Sandbox API implementation
    create an instance of sandbox
    
    instance = sandbox()
    
    the search methods have parameters.  They are available for reference through the instance $Method_paramaters
    
    instance.Business_parameters
    
    build a dict prom selected paramaters for your method and pass that to the $Method_search function.
    
    params = { 'what':'Boots' }
    instance.Business_Search( params )
    '''
    
    global sandbox_api
    global sandbox_root
    global Business_Search_parameters
    global Business_Details_Search_parameters
    global FindDealer_Search_paramaters
    global GetTypeAhead_Search_parameters
    global Industries
    global provinces
    global Canadian_Capitals
    global Canadian_Total_Area
    global Canadian_Land_Area
    global Canadian_Water_Area
    global Canadian_Largest_Metropolitan_Areas
    global SandBox_Searches
    SandBox_Searches = 300
    sandbox_api = ''
    sandbox_root = 'http://api.sandbox.yellowapi.com'
    
    Canadian_Largest_Metropolitan_Areas = {
    'Toronto':{'name':'Ontario','population':'5,583,064',},
    'London':{'name':'Ontario', 'population':'474,786',},
    'Montreal':{'name':'Quebec', 'population':'3,824,221',},
    'St. Catharines-Niagara':{'name':'Ontario', 'population':'392,184',},
    'Vancouver':{'name':'British Columbia', 'population':'2,313,328',},
    'Halifax':{'name':'Nova Scotia', 'population':'390,328',},
    'Ottawa-Gatineau':{'name':'Ontario–Quebec', 'population':'1,236,324',},
    'Oshawa':{'name':'Ontario', 'population':'356,177',},
    'Calgary':{'name':'Alberta', 'population':'1,214,839',},
    'Victoria':{'name':'British Columbia', 'population':'344,615',},
    'Edmonton':{'name':'Alberta', 'population':'1,159,869',},
    'Windsor':{'name':'Ontario', 'population':'319,246',},
    'Quebec':{'name':'Quebec', 'population':'765,706',},
    'Saskatoon':{'name':'Saskatchewan', 'population':'260,600',},
    'Winnipeg':{'name':'Manitoba', 'population':'730,018',},
    'Regina':{'name':'Saskatchewan', 'population':'210,556',},
    'Hamilton':{'name':'Ontario', 'population':'721,053',},
    'Sherbrooke':{'name':'Quebec', 'population':'201,890',},
    'Kitchener-Cambridge-Waterloo':{'name':'Ontario', 'population':'477,160',},
    "St. John's":{'name':'Newfoundland and Labrador', 'population':'196,966',},
}
    Canadian_Water_Area = {
    '1':{'rank':'1', 'name':'Quebec', 'Square kilometers':'176,928', 'Square miles':'68,312', 'percentage of area':'11.5', 'percentage of total':'19.9',},
    '2':{'rank':'2', 'name':'Northwest Territories', 'Square kilometers':'163,021', 'Square miles':'62,943', 'percentage of area':'12.1', 'percentage of total':'18.3',},
    '3':{'rank':'3', 'name':'Ontario', 'Square kilometers':'158,654', 'Square miles':'61,257', 'percentage of area':'14.7', 'percentage of total':'17.8',},
    '4':{'rank':'4', 'name':'Nunavut', 'Square kilometers':'157,077', 'Square miles':'60,648', 'percentage of area':'7.5', 'percentage of total':'17.6',},
    '5':{'rank':'5', 'name':'Manitoba', 'Square kilometers':'94,241', 'Square miles':'36,387', 'percentage of area':'14.5', 'percentage of total':'10.6',},
    '6':{'rank':'6', 'name':'Saskatchewan', 'Square kilometers':'59,366', 'Square miles':'22,921', 'percentage of area':'9.1', 'percentage of total':'6.7',},
    '7':{'rank':'7', 'name':'Newfoundland and Labrador', 'Square kilometers':'31,340', 'Square miles':'12,100', 'percentage of area':'7.7', 'percentage of total':'3.5',},
    '8':{'rank':'8', 'name':'British Columbia', 'Square kilometers':'19,549', 'Square miles':'7,548', 'percentage of area':'2.1', 'percentage of total':'2.2',},
    '9':{'rank':'9', 'name':'Alberta', 'Square kilometers':'19,531', 'Square miles':'7,541', 'percentage of area':'3.0', 'percentage of total':'2.2',},
    '10':{'rank':'10', 'name':'Yukon', 'Square kilometers':'8,052', 'Square miles':'3,109', 'percentage of area':'1.7', 'percentage of total':'0.9',},
    '11':{'rank':'11', 'name':'Nova Scotia', 'Square kilometers':'1,946', 'Square miles':'751', 'percentage of area':'3.5', 'percentage of total':'0.2',},
    '12':{'rank':'12', 'name':'New Brunswick', 'Square kilometers':'1,458', 'Square miles':'563', 'percentage of area':'2.0', 'percentage of total':'0.2',},
    '13':{'rank':'13', 'name':'Prince Edward Island', 'Square kilometers':'0', 'Square miles':'0', 'percentage of area':'0', 'percentage of total':'0',},
}
    Canadian_Land_Area = {
    '1':{'rank':'1', 'name':'Nunavut', 'Square kilometers':'1,936,113','Square Miles':'747,537','percentag':'21.3',},
    '2':{'rank':'2', 'name':'Quebec', 'Square kilometers':'1,365,128', 'Square Miles':'27,0759', 'Percentage':'15.0',},
    '3':{'rank':'3', 'name':'Northwest Territories', 'Square kilometers':'1,183,085', 'Square Miles':'456,792', 'Percentage':'13.0',},
    '4':{'rank':'4', 'name':'British Columbia', 'Square kilometers':'925,186', 'Square Miles':'357,216', 'Percentage':'10.4',},
    '5':{'rank':'5', 'name':'Ontario', 'Square kilometers':'917,741', 'Square Miles':'354,342', 'Percentage':'10.1',},
    '6':{'rank':'6', 'name':'Alberta', 'Square kilometers':'642,317', 'Square Miles':'248,000', 'Percentage':'7.1',},
    '7':{'rank':'7', 'name':'Saskatchewan', 'Square kilometers':'591,670', 'Square Miles':'228,445', 'Percentage':'6.5',},
    '8':{'rank':'8', 'name':'Manitoba', 'Square kilometers':'553,556', 'Square Miles':'213,729', 'Percentage':'6.1',},
    '9':{'rank':'9', 'name':'Yukon', 'Square kilometers':'474,391', 'Square Miles':'183,163', 'Percentage':'5.2',},
    '10':{'rank':'10', 'name':'Newfoundland and Labrador', 'Square kilometers':'373,872', 'Square Miles':'144,353', 'Percentage':'4.1',},
    '11':{'rank':'11', 'name':'New Brunswick', 'Square kilometers':'71,450', 'Square Miles':'27,587', 'Percentage':'0.8',},
    '12':{'rank':'12', 'name':'Nova Scotia', 'Square kilometers':'53,338', 'Square Miles':'20,594', 'Percentage':'0.6',},
    '13':{'rank':'13', 'name':'Prince Edward Island', 'Square kilometers':'5,660', 'Square Miles':'2,185', 'Percentage':'0.1',},
}  
    Canadian_Capitals = {
    'Ottowa':{'territory':'Canada','capitol':'Ottowa','type':'National',},
    'Edmonton':{'territory':'Alberta','capitol':'Edmonton','type':'Provincial',},
    'Victoria':{'territory':'British Columbia','capitol':'Victoria','type':'Provincial',},
    'Winnipeg':{'territory':'Manitoba','capitol':'Winnipeg','type':'Provincial',},
    'Fredericton':{'territory':'New Brunswick','capitol':'Fredericton','type':'Provincial',},
    "St. John's":{'territory':'Newfoundl and Labrador','capitol':"St. John's",'type':'Provincial',},
    'Halifax':{'territory':'Nova Scotia','capitol':'Halifax','type':'Provincial',},
    'Toronto':{'territory':'Ontario','capitol':'Toronto','type':'Provincial',},
    'Charlottetown':{'territory':'Prince Edward Island','capitol':'Charlottetown','type':'Provincial',},
    'Quebec City':{'territory':'Quebec','capitol':'Quebec City','type':'Provincial',},
    'Regina':{'territory':'Saskatchewan','capitol':'Regina','type':'Provincial',},
    'Yellowknife':{'territory':'Northwest Territories','capitol':'Yellowknife','type':'Territorial',},
    'Iqaluit':{'territory':'Nunavut','capitol':'Iqaluit','type':'Territorial',},
    'Whitehorse':{'territory':'Yukon','capitol':'Whitehorse','type':'Territorial',},
}
    Canadian_Total_Area = {
    'Nunavut':{'rank':'1', 'name':'Nunavut', 'Square kilometers':'2,093,190', 'Square Miles':'808,185', 'Percentage':'21.0',},
    'Quebec':{'rank':'2', 'name':'Quebec', 'Square kilometers':'1,542,056', 'Square Miles':'595,391', 'Percentage':'15.4',},
    'Northwest Territories':{'rank':'3', 'name':'Northwest Territories', 'Square kilometers':'1,346,106', 'Square Miles':'519,734', 'Percentage':'13.5',},
    'Ontario':{'rank':'4', 'name':'Ontario', 'Square kilometers':'1,076,395', 'Square Miles':'415,598', 'Percentage':'10.8',},
    'British Columbia':{'rank':'5', 'name':'British Columbia', 'Square kilometers':'944,735', 'Square Miles':'364,764', 'Percentage':'9.5',},
    'Alberta':{'rank':'6', 'name':'Alberta', 'Square kilometers':'661,848', 'Square Miles':'255,541', 'Percentage':'6.6',},
    'Saskatchewan':{'rank':'7', 'name':'Saskatchewan', 'Square kilometers':'651,036', 'Square Miles':'251,366', 'Percentage':'6.5',},
    'Manitoba':{'rank':'8', 'name':'Manitoba', 'Square kilometers':'647,797', 'Square Miles':'250,116', 'Percentage':'6.5',},
    'Yukon':{'rank':'9', 'name':'Yukon', 'Square kilometers':'482,443', 'Square Miles':'186,272', 'Percentage':'4.8',},
    'Newfoundland and Labrador':{'rank':'10', 'name':'Newfoundland and Labrador', 'Square kilometers':'405,212', 'Square Miles':'156,453', 'Percentage':'4.1',},
    'New Brunswick':{'rank':'11', 'name':'New Brunswick', 'Square kilometers':'72,908', 'Square Miles':'28,150', 'Percentage':'0.7',},
    'Nova Scotia':{'rank':'12', 'name':'Nova Scotia', 'Square kilometers':'55,284', 'Square Miles':'21,345', 'Percentage':'0.6',},
    'Prince Edward Island':{'rank':'13', 'name':'Prince Edward Island', 'Square kilometers':'5,660', 'Square Miles':'2,185', 'Percentage':'0.1',},
}   
    Business_Search_parameters = {
        'pg':{ 'description':'Requested page', 'example':'integer > 0, max 50 defailt 1', 'required':'N'},
        'what':{ 'description':'search term or keyword or telephone number', 'example':'any text string, utf-8', 'required':'Y'},
        'lang':{ 'description':'language for returned content', 'example':'en, fr', 'required':'N'},
        'where':{ 'description':'This may be a location name or a specific coordinate specification in the format: cZ{longitude},{latitude}.', 'example':'Toronto , cZ-73.61995,45.49981, UTF-8', 'required':'Y' },
        'pgLen':{ 'descrition':'Number of results', 'example':'integer > 0, Max 100, Default 40', 'required':'N'},
        'dist':{ 'description':'Maximum distance to return results within (when latitude/longitude is specified) in kilometres', 'example':'Positive decimal value', 'required':'N'},
        'fmt':{ 'desription':'The format of output', 'example':'JSON or XML', 'required':'Y'},
        'sflag':{ 'description':'Flags to modify or filter the search result. These may be combined as logical “AND” filters.  To combine more than one filter, use the “dash” to separate each value.', 'example':'bn – {what} search term in business name, fto – results has photo, vdo – results has video', 'required':'N'},
        'apikey':{ 'description':'an API key for the Places API', 'example':'24 characters alphanumeric string', 'required':'Y'},
        'UID':{ 'description':'A string of characters which uniquely identifies a user of the application. (ie. IP address, session ID, or hash of the phone ID)', 'example':'IP address, session ID, hash of the phone ID, etc.', 'required':'Y' }
}
    Business_Details_Search_parameters = {
        'prov':{ 'description':'Normalized name of Province.  Canada is acceptable', 'example':'text-string', 'required':'Y' },
        'city':{ 'description':'The city location', 'example':'Text string', 'required':'N' },
        'bus-name':{ 'description':'Business Name normalized', 'example':'text-string', 'required':'Y' },
        'listingId':{ 'description':'The unique listing id identifying the business', 'example':'from getbusiness and getdealer', 'required':'Y' },
        'lang':{ 'description':'Suggestion Language', 'example':'en, fr', 'required':'N' },
        'fmt':{ 'description':'The format of the Output', 'example':'JSON or XML', 'required':'Y' },
        'apikey':{ 'description':'API key', 'example':'24 character alphanumeric', 'required':'Y' },
        'UID':{ 'description':'A string of characers which uniquely identifies a user of the application', 'example':'phone-number or proper name', 'required':'Y' },
}
    FindDealer_Search_paramaters = {
        'pid':{ 'description':'The listingId of a parent business. A parent business can be identified by the ‘isParent’ flag in the Listing object returned by FindBusinesses.', 'example':'Valid parent listing id', 'required':'Y' },
        'pg':{ 'description':'The requested page', 'example':'Number > 0 <=50 default 1', 'required':'N' },
        'pgLen':{ 'description':'Results to return per page', 'example':'Number > 0 and <= 100 default 40', 'required':'N' },
        'lang':{ 'description':'Suggestion language', 'example':'en, fr', 'required':'N' },
        'fmt':{ 'description':'THe format of the ouput', 'example':'JSON or XML', 'required':'Y' },
        'apikey':{ 'description':'API key', 'example':'24 character alphanumeric', 'required':'Y' },
        'UID':{ 'description':'A string of characers which uniquely identifies a user of the application', 'example':'phone-number or proper name', 'required':'Y' }, 
}    
    GetTypeAhead_Search_parameters = {
        'text':{ 'description':'Characters typed by user', 'example':'Any Character sequence', 'required':'Y' },
        'lang':{ 'description':'Suggestion language', 'example':'en, fr', 'required':'N' },
        'field':{ 'description':'which field to provide suggestion', 'example':'WHAT, WHERE', 'required':'Y' },
        'apikey':{ 'description':'the api key', 'example':'24 digit alpha numeric code', 'required':'Y' },
        'fmt':{ 'description':'THe format of the ouput', 'example':'JSON or XML', 'required':'Y' },
        'UID':{ 'description':'A unique identifier', 'example':'Phone number, proper name', 'required':'Y' },
}    
    Industries = {
    'Agriculture':[ 'Extermination/Pest Control','Farming(Animal Production)','Farming(Crop Production)',\
                   'Fishing/Hunting','Landscape Services','Lawn care Services','Other (Agriculture & Forestry/Wildlife)'],
    'Business & Information':['Consultant','Employment Office','Fundraisers','Going out of Business Sales',\
                              'Marketing/Advertising','Non Profit Organization','Notary Public','Online Business',\
                              'Other (Business & Information)','Publishing Services','Record Business',\
                              'Retail Sales','Technology Services','Telemarketing','Travel Agency','Video Production',],
    'Construction':['AC & Heating','Architect','Building Construction','Building Inspection','Concrete Manufacturing',\
                    'Contractor','Engineering/Drafting','Equipment Rental','Other (Construction/Utilities/Contracting)',\
                    'Plumbing','Remodeling','Repair/Maintenance'],
    'Education':['Child Care Services','College/Universities','Cosmetology School','Elementary & Secondary Education',\
                 'GED Certification','Other (Education)','Private School','Real Estate School','Technical School',\
                 'Trade School','Tutoring Services','Vocational School',],
    'Finance & Insurance':['Accountant','Auditing','Bank/Credit Union','Bookkeeping','Cash Advances',\
                           'Collection Agency','Insurance','Investor','Other (Finance & Insurance)',\
                           'Pawn Brokers','Tax Preparation',],
    'Food & Hospitality':['Alcohol/Tobacco Sales','Alcoholic Beverage Manufacturing','Bakery','Caterer',\
                          'Food/Beverage Manufacturing','Grocery/Convenience Store(Gas Station)',\
                          'Grocery/Convenience Store(No Gas Station)','Hotels/Motels(Casino)',\
                          'Hotels/Motels(No Casino)','Mobile Food Services','Other (Food & Hospitality)',\
                          'Restaurant/Bar','Specialty Food(Fruit/Vegetables)','Specialty Food(Meat)',\
                          'Specialty Food(Seafood)','Tobacco Product Manufacturing','Truck Stop','Vending Machine',],
    'Gaming':['Auctioneer','Boxing/Wrestling','Casino/Video Gaming','Other (Gaming)','Racetrack','Sports Agent',],
    'Health Services':['Acupuncturist','Athletic Trainer','Child/Youth Services','Chiropractic Office',\
                       'Dentistry','Electrolysis','Embalmer','Emergency Medical Services',\
                       'Emergency Medical Transportation','Hearing Aid Dealers','Home Health Services',\
                       'Hospital','Massage Therapy','Medical Office','Mental Health Services',\
                       'Non Emergency Medical Transportation','Optometry','Other (Health Services)',\
                       'Pharmacy','Physical Therapy','Physicians Office','Radiology','Residential Care Facility',\
                       'Speech/Occupational Therapy','Substance Abuse Services','Veterinary Medicine',\
                       'Vocational Rehabilitation','Wholesale Drug Distribution'],
    'Motor Vehicle':['Automotive Part Sales','Car Wash/Detailing','Motor Vehicle Rental','Motor Vehicle Repair',\
                     'New Motor Vehicle Sales','Other (Motor Vehicle)','Recreational Vehicle Sales',\
                     'Used Motor Vehicle Sales',],
    'Natural Resources/Environmental':['Conservation Organizations','Environmental Health','Land Surveying',\
                                       'Oil & Gas Distribution','Oil & Gas Extraction/Production',\
                                       'Other (Natural Resources/Environmental)','Pipeline','Water Well Drilling',],
    'Other':['Other'],
    'Personal Services':['Animal Boarding','Barber Shop','Beauty Salon','Cemetery','Diet Center',\
                         'Dry cleaning/Laundry','Entertainment/Party Rentals','Event Planning','Fitness Center',\
                         'Florist','Funeral Director','Janitorial/Cleaning Services','Massage/Day Spa','Nail Salon',\
                         'Other (Personal Services)','Personal Assistant','Photography','Tanning Salon',],
    'Real Estate & Housing':['Home Inspection','Interior Design','Manufactured Housing','Mortgage Company',\
                             'Other (Real Estate & Housing)','Property Management','Real Estate Broker/Agent',\
                             'Warehouse/Storage'],
    'Security':['Attorney','Bail Bonds','Court Reporter','Drug Screening','Locksmith','Other (Safety/Security & Legal)',\
                'Private Investigator','Security Guard','Security System Services',],
    'Transportation':['Air Transportation','Boat Services','Limousine Services','Other (Transportation)',\
                      'Taxi Services','Towing','Truck Transportation(Fuel)','Truck Transportation(Non Fuel)',],    
}
    
    def __init__(self):
        self.sandbox_api = sandbox_api
        self.sandbox_root = sandbox_root
        self.Business_Search_parameters = Business_Search_parameters
        self.Business_Details_Search_parameters = Business_Details_Search_parameters
        self.FindDealer_Search_paramaters = FindDealer_Search_paramaters
        self.GetTypeAhead_Search_parameters = GetTypeAhead_Search_parameters
        self.Industries = Industries
        self.Canadian_Capitals = Canadian_Capitals
        self.Canadian_Total_Area = Canadian_Total_Area
        self.Canadian_Land_Area = Canadian_Land_Area
        self.Canadian_Water_Area = Canadian_Water_Area
        self.Canadian_Largest_Metropolitan_Areas = Canadian_Largest_Metropolitan_Areas
        self.SandBox_Searches = SandBox_Searches
        
    def FindBusiness_Search_Required_Parameters(self):
        return [p for p in Business_Search_parameters if Business_Search_parameters[p]['required'] == 'Y']
    
    def GetBusinessDetails_Search_Required_Parameters(self):
        return [p for p in Business_Details_Search_parameters if Business_Details_Search_parameters[p]['required'] == 'Y']
    
    def FindDealer_Search_Required_Paramaters(self):
        return [p for p in FindDealer_Search_paramaters if FindDealer_Search_paramaters[p]['required'] == 'Y']
    
    def GetTypeAhead_Search_Required_Parameters(self):
        return [p for p in GetTypeAhead_Search_parameters if GetTypeAhead_Search_parameters[p]['required'] == 'Y']
    
    def FindBusiness_Search(self, parameters_dict):
        '''
        build a dict prom selected paramaters for your method and pass that to the $Method_search function.
        
        instance = sandbox()
        params = { 'what':'Boots' }
        instance.Business_Search( params )
        
        All Required Paramaters have to be passed in
        [p for p in instance.Business_parameters if p.values()[0]['required' == 'Y']
        
        specify JSON output 'fmt':'JSON'
        '''
        form = params
        query = urllib.urlencode(form)
        #print (sandbox_root + '/FindBusiness/' + "?" + query)
        YellowAPI_request = urllib.urlopen(sandbox_root + '/FindBusiness/' + "?" + query)
        x = json.loads(YellowAPI_request.read())
        return x
    
    def GetBusinessDetails_Search(self, parameters_dict):
        '''
        pass in the business id from FindBusiness() in the paramaters
        '''
        form = params
        query = urllib.urlencode(form)
        #print (sandbox_root + '/GetBusinessDetails/' + "?" + query)
        YellowAPI_request = urllib.urlopen(sandbox_root + '/GetBusinessDetails/' + "?" + query)
        x = json.loads(YellowAPI_request.read())
        return x
    
    def FindDealer_Search(self, paramaters_dict):
        '''
        pass in the parentId in params.
        '''
        form = params
        query = urllib.urlencode(form)
        #print (sandbox_root + '/FindDealer/' + "?" + query)
        YellowAPI_request = urllib.urlopen(sandbox_root + '/FindDealer/' + "?" + query)
        x = json.loads(YellowAPI_request.read())
        return x
    
    def GetTypeAhead_Search(self, parameters_dict):
        '''
        pass in required paramaters in dict form.
        
        This is for autocomplete for a web form. field is WHAT or WHERE
        '''
        form = params
        query = urllib.urlencode(form)
        #print (sandbox_root + '/GetTypeAhead/' + "?" + query)
        YellowAPI_request = urllib.urlopen(sandbox_root + '/GetTypeAhead/' + "?" + query)
        x = json.loads(YellowAPI_request.read())
        return x
    
    def Industry_Search_In_Capitals(self, business_list, UID):
        Search_Results_Dict = {}
        SandBox_Searches = 300
        if SandBox_Searches >= 0:
            for city in Canadian_Capitals:
                Search_Results_Dict[city] = {}
                for business_type in business_list:
                    print('Searching %s for %s' % (city, business_type))
                    params = { 'what':business_type, 'apikey':sandbox_api, 'fmt':'JSON', 'where':city, 'UID':UID, 'pgLen':'100' }
                    Search_Results_Dict[city][business_type] = instance.FindBusiness_Search(params)
                    SandBox_Searches -= 1
                    time.sleep(2)
        else:
            print('Reached daily limit of searches')
            return Search_Results_Dict
        return Search_Results_Dict