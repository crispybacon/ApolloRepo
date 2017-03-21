import requests, json, re, folium, datetime, pymongo
NYTkeys = {
    'mostPopular':'',
    'books':'',
    'geographic':'',
    'Semantic':'',
    'topStories':'',
    'articleSearch':'',
    'newsWire':'',
}
NYTRoot = 'https://api.nytimes.com/svc/'
NYTEndPoints = {
    'search':'search/v2/articlesearch.json',
    'books':'books/v3/lists.json',
    'geographics':'semantic/v2/geocodes/query.json',
    'semantics':'semantic/v2/concept/name//.json',
    'topStories':'topstories/v2/home.json',
    'newsWire':'news/v3/content/content.json'
}
standardHeaders = {'user-agent': 'NYTimesAPIClient'}
sources = ['nyt','iht']
NYTSections = [ 'World', 'U.S.', 'Politics', 'N.Y.', 'Business', 'Opinion',
               'Technology', 'Science', 'Health', 'Sports', 'Arts', 'Style', 'Food',
               'Travel' 'Magazine' 'T Magazine', 'Real Estate', ]
def newsWire(returnURI=False, default=True, source=False, section=False, timePeriod=False, limit=False, offset=False, printHeadlines=False, debug=False, report=False):
    date = datetime.datetime.strftime(datetime.datetime.today(), '%A %D %H:%m %p')
    if limit!=False:
        if limit > 20:
            limit = 20
    else:
        limit = 20
    if source != False:
        default=False
    if default==True:
        source = 'all'
        section = 'all'
    if source!=False:
        if section==False:
            section = 'all'
    URI = NYTRoot+'news/v3/content/'+source+'/'+section
    if timePeriod !=False:
        assert type(int(limit))==int,'timePeriod must be a number'
        URI+='/{}'.format(timePeriod)
    URI +='.json?'
    if limit!= False:
        assert type(int(limit))==int,'limit must be a number'
        URI+= '&limit={}'.format(limit)
    if offset!=False:
        URI+='&offset={}'.format(offset)
    URI += '&api-key='+NYTkeys['newsWire']
    if debug == True:
        print(URI)
    if returnURI == True:
        return(URI)
    results = requests.get(URI)
    assert results.ok==True, "Could not complete request.  Possibly no results. Enable debug and check URI."
    results = results.json()
    total = results['num_results']
    if report == True:
        print('New York Times News Wire Query')
        print('Date: {}'.format(date))
        print('Status: {}'.format(results['status']))
        print('Number of results: {}'.format(total))
        if offset==False:
            print('Results: 0 - {}'.format(total))
        else:
            if offset+limit < total:
                print('Results: {} - {}'.format(offset, offset+limit))
            else:
                print('Results: {} - {}'.format(offset, total))
        if printHeadlines == True:
            for article in results['results']:
                print(article['title'])
    return results
def fetchAllNewsWireresults(isource='all', isection='all', itimePeriod=120):
    idx = 20
    results = newsWire(source=isource, section=isection, timePeriod=itimePeriod, report=False)
    total = int(results['num_results'])
    paper = results['results']
    while idx <= total:
        chunk = newsWire(source=isource, section=isection, timePeriod=itimePeriod, report=False, offset=idx)
        for article in chunk['results']:
            paper.append(article)
        idx+=20
    print('Total Records Retrieved: {}'.format(total))
    return paper
def topStories(section, report=True, debug=False, returnURI=False, printHeadlines=True):
    '''
    sections are: home, arts, automobiles, books, business, fashion, 
    food, health, insider, magazine, movies, national, nyregion, 
    obituaries, opinion, politics, realestate, science, sports, 
    sundayreview, technology, theater, tmagazine, travel, upshot, 
    and world.
    '''
    date = datetime.datetime.strftime(datetime.datetime.today(), '%A %D %H:%m %p')
    URI = NYTRoot+'topstories/v1/'+section+'.json?api-key='+NYTkeys['topStories']
    if debug == True:
        print(URI)
    if returnURI == True:
        return(URI)
    results = requests.get(URI)
    assert results.ok==True, "Could not complete request. Possibly no results. Enable debug and check URI."
    results = results.json()
    total = results['num_results']
    if report == True:
        print('New York Times Top Stories Query')
        print('Date: {}'.format(date))
        print('Status: {}'.format(results['status']))
        print('Number of results: {}'.format(total))
        if printHeadlines == True:
            for article in results['results']:
                print(article['title'])
    return results
def mostPopular(section, pType, pTypeTarget='facebook;twitter', timePeriod=1, report=True, debug=False, returnURI=False, printHeadlines=True):
    '''
    sections are: home, arts, automobiles, books, business, fashion, 
    food, health, insider, magazine, movies, national, nyregion, 
    obituaries, opinion, politics, realestate, science, sports, 
    sundayreview, technology, theater, tmagazine, travel, upshot, 
    and world.
    supported time periods are 1,7 and 30
    '''
    date = datetime.datetime.strftime(datetime.datetime.today(), '%A %D %H:%m %p')
    if pType != 'mostshared':
        URI = NYTRoot+'mostpopular/v2/'+pType+'/'+section
    else:
        URI = NYTRoot+'mostpopular/v2/'+pType+'/'+section+'/'+pTypeTarget
    URI+= '/{}'.format(timePeriod)
    URI +='.json?apikey='+NYTkeys['mostPopular']
    if debug == True:
        print(URI)
    if returnURI == True:
        return(URI)
    results = requests.get(URI)
    assert results.ok==True, "Could not complete request. Possibly no results. Enable debug and check URI."
    results = results.json()
    total = results['num_results']
    if report == True:
        print('New York Times Most Popular Stories Query')
        print('Date: {}'.format(date))
        print('Status: {}'.format(results['status']))
        print('Number of results: {}'.format(total))
        if printHeadlines == True:
            for article in results['results']:
                print(article['title'])
    return results
def semanticSearchbyType(concept, specific_concept_name, report=True, debug=False, returnURI=False, printHeadlines=True):
    '''
    concept Types =  {
        'Location':'nytd_geo',
        'Person':'nytd_per',
        'Organization':'nytd_org',
        'Descriptor':'nytd_des',
        }
    '''
    date = datetime.datetime.strftime(datetime.datetime.today(), '%A %D %H:%m %p')
    URI = NYTRoot+'semantic/v2/concept/name/'+concept + '/' + specific_concept_name +'.json?fields=all&api-key='+NYTkeys['topStories']
    if debug == True:
        print(URI)
    if returnURI == True:
        return(URI)
    results = requests.get(URI)
    assert results.ok==True, "Could not complete request. Possibly no results. Enable debug and check URI."
    results = results.json()
    total = results['num_results']
    if report == True:
        print('New York Times Semantics Query')
        print('Date: {}'.format(date))
        print('Status: {}'.format(results['status']))
        print('Number of results: {}'.format(total))
        '''if printHeadlines == True:
            for article in results['results']:
                print(article['title'])'''
    return results
def specificArticle(url, debug=False, returnURI=False):
    date = datetime.datetime.strftime(datetime.datetime.today(), '%A %D %H:%m %p')
    URI = NYTRoot+'news/v3/content.json?url={}'.format(url)
    URI += '&api-key='+NYTkeys['topStories']
    if debug == True:
        print(URI)
    if returnURI == True:
        return(URI)
    results = requests.get(URI)
    assert results.ok==True, "Could not complete request. Possibly no results. Enable debug and check URI."
    results = results.json()
    #total = results['num_results']
    return results
def search(query, debug=False, returnURI=False):
    date = datetime.datetime.strftime(datetime.datetime.today(), '%A %D %H:%m %p')
    URI = NYTRoot+'search/v2/articlesearch.json?fq={}'.format(query)
    URI += '&api-key='+NYTkeys['topStories']
    if debug == True:
        print(URI)
    if returnURI == True:
        return(URI)
    results = requests.get(URI)
    assert results.ok==True, "Could not complete request. Possibly no results. Enable debug and check URI."
    results = results.json()
    #total = results['num_results']
    return results
def relatedURLS(article, report=False):
    if 'related_urls' in article:
        #print(article)
        try:
            related = article['related_urls'] 
            facets = {}
            urls = []
            for record in related:
                for item in record:
                    urls.append({item:record[item]})
            for record in article:
                if 'facet' in record:
                    facets[record] = article[record]
        except:
            print('No related URLS, use facets instead')
    return urls, facets
def followURLSMap(urls, report=False):
    report = {}
    x=0
    for i in range(0,len(urls), 2):
        rArticle = specificArticle(urls[i]['url'])
        results = rArticle['results'][0]
        report[x] = results
        x += 1
    return report
def makePopUp(results):
    summary = results1['abstract']
    article_template = """<b>Title: </b>{}</br>
    <b>Byline:</b> {}</br>
    <b>Abstract</b>: {}</br>
    <b>link:</b> {}""".format(results['title'],
                                   results['byline'], 
                                   results['abstract'], 
                                   results['url'])
    if 'multimedia' in results:
        if results['multimedia'] != '':
            for entry in results['multimedia']:
                if entry['type'] == 'image':
                    media = entry
        article_template+="""</br>
         <img src="{}" alt={}></br>
         <b>Caption: </b>{}</br>
         """.format(media['url'], media['copyright'],media['caption'])
    return article_template
def addCluster(layer, cluster, color):
    for article in layer:
        for place in layer[article]['geo_facet']:
            try:
                coordinate = wikipedia.page(place).coordinates
            except:
                pass
            sub_article_template = makePopUp(layer[article])
            secondaryPopUp = folium.Html(sub_article_template, script=True)
            articlePopup = folium.Popup(secondaryPopUp, max_width=450,)
            Marker = folium.Marker(location=coordinate,
                                   popup=articlePopup,
                                   icon = folium.Icon(color = color)
                                  ).add_to(cluster)
def layer3Relations(layer1_relations, layer2):
    i=0
    layer1_urls = []
    for x in range(0,len(layer1_relations), 2):
        layer1_urls.append(layer1_relations[x]['url'])
    new_urls = []
    for x in layer2:
        try:
            urls = layer2[x]['related_urls']
            for x in range(1,len(urls), 2):
                #print(urls[x]['url'])
                if urls[x]['url'] not in layer1_urls:
                    if urls[x] not in new_urls:
                        new_urls.append(urls[x])
        except:pass
    return new_urls
def dataLayerFromRelated(urls):
    layer_report = {}
    x = 0
    for article in layer3_urls:
        try:
            #print(article['url'])
            layer_report[x] = specificArticle(article['url'])['results'][0]
            x+=1
        except:pass
    return layer_report
def mapArticleRelations(article):
    center = (39, 34)
    primaryPost = (40.45, -73.59)
    layer1 = specificArticle(article['url'])
    if layer1['results'][0]['geo_facet'] != 0:
        try:
            primaryPost = wikipedia.page(layer1['results'][0]['geo_facet']).coordinates
        except:
            pass
    newsMap = folium.Map(location=primaryPost,tiles='Stamen Watercolor', zoom_start=2)
    layer2Cluster = folium.MarkerCluster().add_to(newsMap)
    layer3Cluster = folium.MarkerCluster().add_to(newsMap)
    print(layer1['results'][0]['title'])
    print('Primary: Blue')
    print('Layer 2 Relations: Red')
    print('Layer 3 Relations: Green')
    article_template = makePopUp(article)
    primaryPopUp = folium.Html(article_template, script=True)
    popup = folium.Popup(primaryPopUp, max_width=450)
    folium.Marker(primaryPost, popup=popup).add_to(newsMap)
    layer1_relations, layer1_facets = relatedURLS(article)
    layer2 = followURLSMap(layer1_relations, report=False)
    print('layer2  {}'.format(len(layer2)))
    layer3_urls = layer3Relations(layer1_relations, layer2)
    layer3 = dataLayerFromRelated(layer3_urls)
    print('layer3 {}'.format(len(layer3)))
    addCluster(layer2, layer2Cluster, color='red')
    addCluster(layer3, layer3Cluster, color='green')
    layer2Cluster.add_to(newsMap)
    layer3Cluster.add_to(newsMap)
    folium.TileLayer('openstreetmap').add_to(newsMap)
    folium.TileLayer('Stamen Toner').add_to(newsMap)
    folium.TileLayer('mapboxcontrolroom').add_to(newsMap)
    folium.TileLayer('cartodbpositron').add_to(newsMap)
    folium.LayerControl().add_to(newsMap)
    return newsMap