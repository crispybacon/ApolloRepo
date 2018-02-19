import requests,re,random,time,os
import matplotlib.pyplot as plt
from nltk import word_tokenize, sent_tokenize

site_root = 'https://www.boardgamegeek.com/xmlapi2/'

api_commands = dict(search_thing='thing?type=',
                    search_hot='hot?parameter',
                    search='search?',)

def apiQuery(api_command, query, **kwargs):
    headers = {
        'User-Agent':'BGG Agent Utility'
    }
    full_query = site_root + api_command + query
    print(full_query)
    return requests.get(full_query)

def stripIds(xml):
    id_search = re.compile('id="(\d+)"')
    with open(xml) as f:
        data = f.read()
    ids = id_search.findall(data, re.DOTALL)
    return ids

def stripPic(xml):
    image_search = re.compile('\<image\>(\S+)?\<')
    with open(xml) as f:
        data = f.read()
    image = image_search.search(data, re.DOTALL).groups()[0]
    return image

def stripDescription(xml):
    desc = re.compile('\<description\>([\S|\s]+?)\<')
    with open(xml, 'r') as f:
        data = f.read()
    description = desc.search(data, re.DOTALL).groups()[0]
    return description

def speak(txt):
    os.system('echo "{}" | /usr/bin/espeak -s 140 -ven+f3'.format(txt))

def beginnerText(txt):
    sentences = sent_tokenize(txt)
    for sentence in sentences:
        sent = word_tokenize(sentence)
        sent = [word for word in sent if word.isalpha() and word not in ['amp']]
        speak(' '.join(sent))
        time.sleep(0.35)

def showPic(pic):
    plt.figure(frameon=False, figsize=(12,12))
    plt.imshow(plt.imread('game_pic.jpg'))
    plt.axis('off')
    plt.show(block=False)

def downloadPic(url):
    with open('game_pic.jpg', 'wb') as f:
        f.write(requests.get(url).content)
    return 'game_pic.jpg'

if __name__ == '__main__':
    result = apiQuery('hot?', 'type=boardgame')
    with open('hot_games.xml', 'wb') as f:
        f.write(result.content)
    game = random.choice(stripIds('./hot_games.xml'))
    result = apiQuery('thing?', 'id={}'.format(game))
    with open('game.xml', 'wb') as f:
        f.write(result.content)
    downloadPic(stripPic('game.xml'))
    showPic('game_pic.jpg')
    beginnerText(stripDescription('game.xml'))
    time.sleep(4)

