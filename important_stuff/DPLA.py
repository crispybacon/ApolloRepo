# A Python adaption of the DPLA API
# Coded by Jesse Bacon
def simple_search(TERM, search_type):
    '''
    Perform a DLPA search for items or collections against a term or terms.
    
    You can combine multiple terms using AND and OR operators. 
    The default behavior when searching for multiple terms is boolean AND. 
    Throw in an asterisk (*) when you want to match any collection of characters within a word. 
    For example, you may want all possible variants of yodeling, regardless of prefixes, infixes, and suffixes.
    example *terprise for Enterprise ir Esperprise or Deterprise and so on.
    Use detail search to search with fields
    '''
    params = {'api_key':KEY, 'q':TERM}
    enc_params = urllib.urlencode(params)
    dpla_request = URL + search_type + '/?' + enc_params
    return requests.get(dpla_request)

def detail_search(parameters, search_type):
    '''
    Used for searching DLPA assets available with parameters.
    
    paramaters are a dictionary object of parameter = value entries
    
    example:
    
    {'sourceResource.Description':'Technology', 'sourceResource.title':'initiative'}
    
    Dates
    
    The DPLA API understands dates. Combine that with the fielded search above, 
    and you’ve got a pretty spiffy way of finding records that have fields that fall before,
    after, and between dates.
    The following examples search the sourceResource.date field which is the time frame 
    of the original physical object, such as when a book was written or when a photo was taken.
    This field can be a range of dates, e.g., a book pertaining to the decade of the 1930s 
    can have an after year of 1930 and a before year of 1939.
    
    examples:
    
    {'sourceResource.date.after':'1910-01-01'}
    (items that were created on or after 1910)
    {'sourceResource.date.before':'1869-01-01'}
    (items that were created on or before 1869)
    {'sourceResource.date.after':'1910','sourceResource.date.before':'1920'}
    (items that were created between 1910 & 1920)
    
    Temporal searching
    
    A related field, sourceResource.temporal, describes the temporal characteristic, or 
    “about-ness” of the the resource, such as the time period about which a book is written.  
    As with sourceResource.date, you can search sourceResource.temporal using the keywords after and before.

    Note that the keywords after and before are used to 
    scope the time span of your search. As you will see in the examples below, 
    if you want to sort or facet a search on sourceResource.date or sourceResource.temporal, 
    you will use the keywords begin and end.
    
    You can find records around a location of interest to you by simply searching within 
    spatial fields. DPLA also understands coordinates of the form latitude:longitude so you 
    can find things more specifically.
    
    Spatial searching
    
    The following examples search the sourceResource.spatial field (the location of the 
    original physical object’s creation, or other location associated with a record, 
    e.g., its setting [for a book]).

    The spatial field has many searchable sub-fields. A few important ones are: 
    name, state, and coordinates. If you do not specify a sub-field, all are searched. 
    The state sub-field is normalized to the full spelling of the (US) state’s name.
    
    Examples:

    sourceResource.spatial=Boston
    (items that are in or about Boston)
    sourceResource.spatial.state=Hawaii
    (items that are in or about the State of Hawaii)
    sourceResource.spatial.state=Massachusetts+OR+Hawaii
    
    Searching within collections
    
    If you have a collection in mind, use the sourceResource.collection.title field.

    Example:

    sourceResource.collection.title=Smith
    
    Sorting results
    Sort stuff using the sort_by parameter. We’ll sort stuff in ascending order by default, but if you’d 
    like to flip things, set the sort_order parameter to desc.

    To see which fields are sortable, see the Sortable Fields section.

    You can also sort by distance from a geographic point (which is pretty sweet). Use the sort_by_pin 
    parameter with a latitude and longitude pair, and make sure to specify the coordinates field to use 
    in the sort_by parameter.

    Examples:

    params = {'q':'yodeling','sort_by':'sourceResource.title'}
    detail_search(params, 'items')
    (items with yodeling in any field, sorted by the title)

    params = {'q':'yodeling', 'sort_by':'sourceResource.date.begin','sort_order':'desc'}
    detail_search(params, 'items')
    (items with yodeling in any field, sorted by starting time span; most recent items listed first)

    params = {'q':'atlanta','sort_by':'sourceResource.subject.name'}
    detail_search(params, 'items')
    (items with atlanta in any field, sorted by the name of their subject)

    params={'sort_by_pin':'42.3,-71','sort_by':'sourceResource.spatial.coordinates'}
    detail_search(params, 'items')
    (all items sorted by distance to Boston)
    
    Pagination
    By default, we’ll give you 10 items. If that’s not enough, you can get the next ten items 
    incrementing the page parameter (it’s one-indexed). If that’s still not enough, you can pull 
    more items per page by using the page_size parameter (we’ll limit you to 500 items per page 
    because greediness is a vice).

    Examples:

    params = {'q':'yodeling','page_size':2}
    detail_search(params, 'items')
    params = {'q':'atlanta','page_size':25}
    detail_search(params, 'items')
    params = {'q':'atlanta','page_size':25, 'page':3}
    detail_search(params, 'items')
    
    JSONP
    
    You’re probably not on our domain, so you probably want to wrap everything up nicely with a callback. 
    Use the callback parameter and specify your callback name. The response will be JavaScript 
    (rather than pure JSON) that, when evaluated, will call your callback function.

    If you are using a JavaScript library for AJAX, such as jQuery or Zepto, the library will 
    handle using the callback parameter for you if you set dataType to “jsonp”.

    Examples:

    parameters = {'sourceResource.subject':'yodel', 'callback':'myFunc'}
    detail_search(params, 'items')
    '''
    parameters['api_key'] = KEY
    enc_params = urllib.urlencode(parameters)
    dpla_request = URL + search_type + '/?' + enc_params
    return requests.get(dpla_request)

def specific_items_search(items):
    '''
    Fetching specific items
    Say you already have the id for the item you want, and you’re just looking to get 
    the rest of the metadata for that item. Simply add the id to the end of the items request. 
    Bonus: You can search for multiple IDs by separating them with a comma (,), with a 
    maximum of 50 ids per request.
    
    Example:

    specific_items_search('fffffed915b46b7d71bcc8d888900c4b')
    '''
    params = {'api_key':KEY}
    enc_params = urllib.urlencode(params)
    dpla_request = URL + 'items/'+ items + '?' + enc_params
    return requests.get(dpla_request)

def search_with_specific_fields(items, fields):
    '''
    Fetching only certain fields
    You’re a busy person. You don’t need to stare at pages and pages of JSON. 
    You know what you want, and after you read this, you’ll know how to get it.

    You can get only the fields you want by using the “fields” parameter, and comma (,) 
    separating the field names. This works for any field except:

    @context
    originalRecord
    
    pass in fields as a string of comma seperated field labels 
    
    Examples:

    search_with_specific_fields('sourceResource.title=yodellers','sourceResource.title')
    (items with yodellers in the title but only return the titles)

    search_with_specific_fields('q=atlanta', 'sourceResource.description,sourceResource.date')
    
    '''
    params = { 'api_key':KEY, 'fields':fields }
    enc_params = urllib.urlencode(params)
    dpla_request = URL + 'items?'+ items + '&' + enc_params
    return requests.get(dpla_request)


def faceted_search_no_items(facets, search_type):
    '''
    Facets tell you the most common values for certain fields in a collection of items.
    
    We return a couple different types of facets depending upon the field you’re looking for.
    For date fields, we’ll send back facets of type date_histogram (which is what it sounds like). 
    For complex text fields, we’ll break it down for you into a terms type. For simple text fields, 
    we’ll also send back a terms type but with unadulterated values. And for geographic types, 
    we’ll give you a geo_distance type. See what that looks like in the Field Reference.
    
    Examples:
    
    Basic:
    faceted_search('isPartOf', 'items')
    
    Multiple:
    faceted_search('sourceResource.publisher,sourceResource.creator', 'items')
    
    Auto-Expanded:

    faceted_search('sourceResource.subject.@id,sourceResource.subject.name', 'items')
    
    Dates:

    faceted_search('sourceResource.date.begin', 'items')
    
    Geo-Distance:

    faceted_search('sourceResource.spatial.coordinates:42.3:-71, 'items')
    '''
    params = {'api_key':KEY, 'facets':facets}
    enc_params = urllib.urlencode(params)
    dpla_request = URL + search_type + '/?' + enc_params
    return requests.get(dpla_request)

def faceted_search_with_items(facets, parameters):
    '''
    performs a detailed search with facets
    
    paramaters are a dictionary object of parameter = value entries
    facets are a comma seperated string of facetable field labels
    
    Example:
    
    No Docs:
    
    facets = 'sourceResource.date.begin'
    parameters = {'page_size':0}
    faceted_search_with_items(facets, parameters)
    
    Facet Limit (maximum 2000):

    facets = 'sourceResource.date.begin'
    parameters = {'facet_size':3}
    faceted_search_with_items(facets, parameters)
    '''
    parameters['api_key'] = KEY
    enc_params = urllib.urlencode(parameters)
    dpla_request = URL + 'items' + '/?' + facets + '&' + enc_params
    return requests.get(dpla_request)

def items_search_object_to_json(search_object):
    '''
    pass in the return from simple_search_items() 
    to cnvert the output text to a json object.
    '''
    return json.loads(search_object.text)

significant_case_sensitive_fields = [
    'id',
    'sourceResource.format',
    'sourceResource.type',
    'sourceResource.contributor',
    'sourceResource.date.displayDate',
    'sourceResource.extent',
    'sourceResource.language.iso639',
    'sourceResource.spatial.iso3166-2',
    'sourceResource.specType',
    'sourceResource.stateLocatedIn.name',
    'sourceResource.stateLocatedIn.iso3166-2',
    ]

sortable_fields = [
    'id',
    '@id',
    'sourceResource.id',
    'sourceResource.contributor',
    'sourceResource.date.begin',
    'sourceResource.date.end',
    'sourceResource.extent',
    'sourceResource.language.name',
    'sourceResource.language.iso639_3',
    'sourceResource.format',
    'sourceResource.stateLocatedIn.name',
    'sourceResource.spatial.name',
    'sourceResource.spatial.country',
    'sourceResource.spatial.region',
    'sourceResource.spatial.county',
    'sourceResource.spatial.state',
    'sourceResource.spatial.city',
    'sourceResource.spatial.coordinates',
    'sourceResource.subject.@id',
    'sourceResource.subject.type',
    'sourceResource.subject.name',
    'sourceResource.temporal.begin',
    'sourceResource.temporal.end',
    'sourceResource.title',
    'sourceResource.type',
    'hasView.@id',
    'hasView.format',
    'isPartOf.@id',
    'isPartOf.name',
    'isShownAt',
    'object',
    'provider.@id',
    'provider.name',
]

facetable_fields = [
    'sourceResource.contributor',
    'sourceResource.date.begin',
    'sourceResource.date.end',
    'sourceResource.language.name',
    'sourceResource.language.iso639_3',
    'sourceResource.format',
    'sourceResource.stateLocatedIn.name',
    'sourceResource.spatial.name',
    'sourceResource.spatial.country',
    'sourceResource.spatial.region',
    'sourceResource.spatial.county',
    'sourceResource.spatial.state',
    'sourceResource.spatial.city',
    'sourceResource.spatial.coordinates',
    'sourceResource.subject.@id',
    'sourceResource.subject.name',
    'sourceResource.temporal.begin',
    'sourceResource.temporal.end',
    'sourceResource.type',
    'dataProvider',
    'hasView.@id',
    'hasView.format',
    'intermediateProvider',
    'isPartOf.@id',
    'isPartOf.name',
    'isShownAt',
    'object',
    'provider.@id',
    'provider.name',
    'admin.contributingInstitution', #(combines dataProvider and intermediateProvider)
]

resource_types = [
    'text',
    'image',
    'sound',
    'moving image',
    'physical object',
    'item',
    'collection',
    'terms',
    'date_histogram',
    'geo_distance',
]

field_prefixes = {
    '@':'JSON-LD field',
    '_':'internal field - look away',
}

# Field Definitions at http://dp.la/info/developers/codex/responses/field-reference/

doc = '''field	description	Source
@context	Simply speaking, a context is used to map terms to IRIs. Terms are case sensitive and any valid string that is not a reserved JSON-LD keyword can be used as a term.	JSON-LD
@id	Used to uniquely identify things that are being described in the document. To be able to externally reference nodes in a graph, it is important that nodes have an identifier. IRIs are a fundamental concept of Linked Data, for nodes to be truly linked, dereferencing the identifier should result in a representation of that node. This may allow an application to retrieve further information about a node.	JSON-LD
count	The number of matches for a query	elasticsearch
dataProvider	Provider of the SourceResource and WebResource	edm
docs		
hasView		edm
hasView.@id		edm; JSON-LD
hasView.format	Information about format.	edm
hasView.rights	Information about rights held in and over a SourceResource. Typically, rights information includes a statement about various property rights associated with the SourceResource, including intellectual property rights.	dc
facets	Groups of items collected by shared field values	elasticsearch
id	DPLA ID of a SourceResource within a given context	DPLA
ingestDate	Date on which the original record was imported into the DPLA database	DPLA
ingestType	Type of record created by ingestion (either item or collection).	DPLA
intermediateProvider	An intermediate organization that selects, collates, or curates data from a data provider that is then aggregated by a provider from which DPLA harvests.	dpla
isShownAt	An unambiguous URL reference to the digital object on the provider’s web site in its full information context.	edm
isShownAt.@id	Actual URL to the digital object on the provider’s web site in its full information context.	edm; JSON-LD
isShownAt.format	MIME type of digital object.	edm
isShownAt.rights	Any rights asserted in the digital object referenced at isShownAt.@id.	dc
limit	The number of documents returned	elasticsearch
object	An unambiguous URL reference to the DPLA digital content preview of the item.	edm
object.@id	Actual URL to the digital object preview on the DPLA web site.	edm
object.format	MIME type of digital object.	edm
object.rights	Any rights asserted in the digital object referenced at object.@id.	dc
originalRecord	Complete original record as provided by the provider	dpla
provider	Service or content hub providing access to the Data Providers content. May contain the same value as Data Provider. (literal value in this version)	edm
provider.@id	URI for the provider page the DPLA API.	edm
provider.name	Human-readable version of provider name	edm
score	The relevance score assigned to the item by Elasticsearch	elasticsearch
sourceResource	This class is a subclass of “edm:ProvidedCHO,” which comprises the source resources [in EDM called “cultural heritage objects”] about which the DPLA collects descriptions. It is here that attributes of source resources are located, not the digital representations of them.	dpla
sourceResource.collection	Array of URIs of collection or aggregation of which SourceResource is a part	dcmitype
sourceResource.collection.@id	URI of collection or aggregation of which SourceResource is a part	JSON-LD
sourceResource.collection.description	Description of the collection or aggregation of which SourceResource is a part	dc
sourceResource.collection.id	DPLA identifier of collection or aggregation of which SourceResource is a part	DPLA
sourceResource.collection.title	Title of collection or aggregation of which SourceResource is a part	dc
sourceResource.contributor	Entity responsible for making contributions to the resource	dc
sourceResource.creator	Entity primarily responsible for making sourceResource	dc
sourceResource.date	Array containing point or period of time associated with an event in lifecycle of a sourceResource (literal value).	dc
sourceResource.date.begin	Date/time of the start of a time span (inclusive).	edm
sourceResource.date.displayDate	The date to be displayed by an application seeking to provide a date to accompany the sourceResource.	
sourceResource.date.end	Date/time of the end of a time span (inclusive)	edm
sourceResource.description	Includes but is not limited to: an abstract, a table of contents, or a free-text account of SourceResource	dc
sourceResource.extent	Size or duration of the SourceResource	dcterms
sourceResource.format	Array containing file format, physical medium or dimensions of a SourceResource.	dc
sourceResource.identifier	Original identifier of a SourceResource within a given context	dc
sourceResource.language	Array containing language(s) of source resource	dc
sourceResource.language.name	Language(s) of source resource	dc
sourceResource.language.iso639_3	ISO 639-3 code for the specified language	
sourceResource.physicalMedium	A physical material or carrier in which source resource exists	dc
sourceResource.publisher	Entity responsible for making the source resource available, typically the publisher of a text (not dataProvider or provider)	dcterms
sourceResource.rights	Information about rights held in and over a SourceResource. Typically, rights information includes a statement about various property rights associated with the SourceResource, including intellectual property rights.	dc
sourceResource.spatial	Spatial characteristics of source resource (usually a literal value in this version)	dcterms
sourceResource.spatial.coordinates	Location coordinates in latitude, longitude form	dpla
sourceResource.spatial.city	Location city	dpla
sourceResource.spatial.county	Location county	dpla
sourceResource.spatial.distance	Distance from point defined in sourceResource.spatial.coordinates.	dpla
sourceResource.spatial.country	Location country	dpla
sourceResource.spatial.name	Location name	dpla
sourceResource.spatial.region	Location region	dpla
sourceResource.spatial.state	Location state	dpla
sourceResource.stateLocatedIn.name	Name of the U.S. state in which the sourceResource is held.	edm
sourceResource.subject	Array containing topic(s)of a SourceResource	dc
sourceResource.subject.@id	Identifier of a subject of a SourceResource (note: not yet specified in the database)	dc; JSON-LD
sourceResource.subject.@type	Identifier of a subject of a SourceResource (note: not yet specified in the database)	dc
sourceResource.subject.name	Topic or subject of a SourceResource	dc
sourceResource.temporal	Temporal characteristics of source resource (usually a literal value in this version)	dpla
sourceResource.temporal.begin	Date/time of the start of a time span (inclusive).	dpla
sourceResource.temporal.end	Date/time of the end of a time span (inclusive).	dpla
sourceResource.title	Name given to a SourceResource	dc
sourceResource.type	Nature or genre of source resource	dc
start	The index of the first document	elasticsearch'''