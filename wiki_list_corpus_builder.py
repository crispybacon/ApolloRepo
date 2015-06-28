# Jesse Bacon 6/28/15
# This will output a pickle that can be loaded and contatins a comprehensive list
# of usefull lists from Wikipedia.  It is usefull as a text corpus for neuro linguistic
# exercies, text processing, and training a lexical classifier or language emulator
# I don't know.  Um.

import wikipedia, re, pickle

list_of_lists = {}
category_names = []
categories = []
page = wikipedia.page('List of lists of lists')
content = page.content
i = 0

def build_list_data(content):
    all_list_data = content.splitlines()
    for line in all_list_data:
        if line == '':
            all_list_data.remove(line)
    all_list_data = all_list_data[1:]
    for line in all_list_data:
        #I had to put these in
        re.sub( r'\xe2\x80\x9308|\xe2\x80\x9310|\xe2\x80\x9309', '', line )
        re.sub( r'(1966\u20132001)', '1966-2001', line  )
        re.sub( 'r\u2013', '', line )
        if line.startswith('Lists of tenants in the World Trade Center'):
            line.replace(line, 'Lists of tenants in the World Trade Center (1966-2001)')
        if line.endswith('World Trade Center (1966\u20132001)'):
            line.repace(line, 'Lists of tenants in the World Trade Center (1966-2001)' )
        #for me it will not sub.  Perhaps I need to change the encoding
        if line.startswith('Lists of tenants in the World Trade Center'):
            line.encode('ascii', 'ignore').decode('ascii', 'ignore')
        #I defer here.  Somethings up.  
    return all_list_data

def build_categories(all_list_data):
    for line in all_list_data:
        if line.startswith('='):
            categories.append(line)
    return categories

def assemble_dict(categories):
    for category in categories:
        cat_name = re.sub('\s|\n|=', '', category.lower())
        #print(cat_name)
        category_names.append(cat_name)
        list_of_lists[cat_name] = []

def populate_dict(lists_page):
    for line in lists_page:
        if line == '' :
            lists_page.remove(line)
        if line.startswith('='):
            current_category = re.sub( '\s|=', '', line ).lower()
            #print(current_category)
        else:
            text = re.sub(r'\n', '', line)
            text = re.sub(r'\xe2\x80\x9308|\xe2\x80\x9310|\xe2\x80\x9309', '', text)
            list_of_lists[current_category].append(text)

def recurse_lists_level_1(list_of_lists):
    for category in list_of_lists.keys():
        print category
        recurse = {}
        print('######   ' + category + '   ######')
        for page in list_of_lists[category]:
            if i<1:
                try:
                    print(page)
                    fetch = wikipedia.page(page)
                    content = fetch.content
                    recurse[page] = content
                except:
                    print('Could not fetch %s' % page)
        list_of_lists[category] = recurse

def save_big_dict_pickle(bd_name):
    pickle.dump(list_of_lists, open( bd_name, 'wb'))

def load_big_dict_pickle(bd_file):
    return pickle.load( open( bd_file, 'rb') )
    
lists_page = build_list_data(content)
categories = build_categories(lists_page)
assemble_dict(categories)
populate_dict(lists_page)
bigDictWikiLists = recurse_lists_level_1(list_of_lists)
save_big_dict_pickle('test.pickle')
db = load_big_dict_pickle('test.pickle')