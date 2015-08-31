#!/usr/bin/env python
# Jesse Bacon 8/30/2015
# A Module to access the Yallow Pages API in Canada.  
# The module will be used to Gather business data for utilization 
# in data visualization and database operation as well as GIS exercises.
# An API key is required for operation.  You can request one at :
# https://publisher.yp.com/register

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
    sandbox_api = ''
    sandbox_root = 'http://api.sandbox.yellowapi.com'
    
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
    
    def __init__(self):
        self.sandbox_api = sandbox_api
        self.sandbox_root = sandbox_root
        self.Business_Search_parameters = Business_Search_parameters
        self.Business_Details_Search_parameters = Business_Details_Search_parameters
        self.FindDealer_Search_paramaters = FindDealer_Search_paramaters
        self.GetTypeAhead_Search_parameters = GetTypeAhead_Search_parameters
        
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
        pprint.pprint(x)
    
    def GetBusinessDetails_Search(self, parameters_dict):
        '''
        pass in the business id from FindBusiness() in the paramaters
        '''
        form = params
        query = urllib.urlencode(form)
        #print (sandbox_root + '/GetBusinessDetails/' + "?" + query)
        YellowAPI_request = urllib.urlopen(sandbox_root + '/GetBusinessDetails/' + "?" + query)
        x = json.loads(YellowAPI_request.read())
        pprint.pprint(x)
    
    def FindDealer_Search(self, paramaters_dict):
        '''
        pass in the parentId in params.
        '''
        form = params
        query = urllib.urlencode(form)
        #print (sandbox_root + '/FindDealer/' + "?" + query)
        YellowAPI_request = urllib.urlopen(sandbox_root + '/FindDealer/' + "?" + query)
        x = json.loads(YellowAPI_request.read())
        pprint.pprint(x)
    
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
        pprint.pprint(x)
