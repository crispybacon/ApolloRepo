def queryEntity(version, entity=None, get_list=True):
    '''
    entity_list = getEntities(version='v1')
    test_query = queryEntity('v1', entity_list[1], get_list=False)
    '''
    if get_list:
        entityListURI = "https://www.fema.gov/api/open/v1/OpenFemaDataSets"
    else:
        entityListURI = "https://www.fema.gov/api/open/{}/{}".format(version,entity)
    raw = json.loads(requests.get(entityListURI).content.decode('utf-8'))
    return raw
def getEntities(version='v1'):
    raw = queryEntity(version)
    return [raw['OpenFemaDataSets'][x]['name'] for x in range(len(raw['OpenFemaDataSets']))]
def getFields(version='v1', entity='all'):
    fields = queryEntity('v1', 'OpenFemaDataSetFields', get_list=False)['OpenFemaDataSetFields']
    if entity == 'all':
        return set([fields[x]['name'] for x in range(len(fields))])
    else:
        return [fields[x]['name'] for x in range(len(fields)) if fields[x]['openFemaDataSet'] == entity]
def searchEntity(version, entity, command):
    '''
    entitySearch('v1', 'HazardMitigationGrants', 'oderby=projectAmount$top=50')
    advanced_test_filter = searchEntity('v1', 'HazardMitigationGrants', "filter=state eq 'Virginia' and projectAmount eq 0&$select=disasterTitle,projectTitle,projectDescription")
    '''
    baseURI = "https://www.fema.gov/api/open/"
    query_string = baseURI + version +  '/' + entity + '?$' + command
    return json.loads(requests.get(query_string).content.decode('utf-8'))
def searchEntityAllRecords(version, entity, command):
    total = searchEntity('v1', entity, 'inlinecount=allpages&$' + command)['metadata']['count']
    cursor = 0
    data = []
    for i in range(math.ceil(total/1000 + 1)):
        cursor = i*1000
        if cursor > total:
            cursor = (cursor - 1) * 1000 + (total % 1000)
        for entry in (searchEntity('v1', entity, 'skip={}&$'.format(cursor)+command)[entity]):
            data.append(entry)
    return data
def entityFiles():
    endpoints = {}
    data = queryEntity('v1')
    for x in range(len(data['OpenFemaDataSets'])):
        endpoints[ data['OpenFemaDataSets'][x]['name'] ] = [data['OpenFemaDataSets'][x]['distribution'][1]['accessURL'] ]
    return endpoints
def loadEntity(entity, file_path):
    test = requests.get('https://www.fema.gov/api/open/v1/{}.csv'.format(entity))
    with open(file_path, 'wb') as f:
        f.write(test.content)
    df = pd.read_csv(file_path)
    return df