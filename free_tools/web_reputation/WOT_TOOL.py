#! python
import requests, json
'''
http://api.mywot.com/version/interface?param1=value1&param2=value2
http://api.mywot.com/0.4/public_link_json2?hosts=example.COM/www.EXAMPLE.NET/&callback=process&key=<your API key>
'''

categories = {
    #'Negative':{
    101:'Malware or Viruses',
    102:'Poor customer experience',
    103:'Phishing',
    104:'Scam',
    105:'Potentially illegal',
    #},
    #'Questionable':{
    201:'Misleadig claims or unethical',
    202:'Privacy Risks',
    203:'Suspicious',
    204:'Hate, discrimination',
    205:'Spam',
    206:'Potentially Unwanted Programs',
    207:'Ads/pop-ups',
    #},
    #'Neutral':{
    301:'Online Tracking',
    302:'Alternative or controversial medicine',
    303:'Opinions, religion, politics',
    304:'Other',
    #},
    #'Positive':{
    501:'Good Site',
    #},
}

def WOT_request(domain):
    results = {}
    for domain in domain:
        if not str(domain)[-1] == '/':
            domain = domain + '/'
        base_request_url = 'http://api.mywot.com/0.4/public_link_json2?'
        #print(base_request_url+'hosts='+domain+'&key='+api_key)
        request_url = base_request_url+'hosts='+domain+'&key='+api_key
        #print(request_url)
        result = requests.get(request_url)
        #print(result.content)
        result_dict = json.loads(result.content)
        results[domain] = result_dict
        return results

def translate_results(results):
    report = {}
    data = results.values()[0].values()[0]
    for entry in data:
        if entry == 'target':
            report['Domain'] = data[entry]
        if entry == 'categories':
            site_category_list = {}
            for value in data[entry]:
                print(value+': {}'.format(categories[int(value)]))
                site_category_list[value] = categories[int(value)]
            report['categories'] = site_category_list
        if len(entry) == 1:
            if int(entry) == 1:
                report['TrustWorthiness_Score'] = {
                'reputation_estimate':data[entry][0],
                'reputation_confidence':data[entry][1]
            }
            elif int(entry) == 4:
                report['Child_Safety_Score'] = {
                'reputation_estimate':data[entry][0],
                'reputation_confidence':data[entry][1]
            }
    return report

def get_key():
    pass
