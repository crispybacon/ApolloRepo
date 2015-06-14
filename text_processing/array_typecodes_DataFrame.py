#Jesse Bacon
#Demonstrates combining DataFrames to make a chart or data stream
#Will render an HTML table in IPython
import pandas as pd
def types_chart_table():
    type_codes = []
    c = {'c':{'Type Code':'c', 'C Type':'char', 'Python Type':'character', 'Minimum Bytes':'1', }}
    b = {'b':{'Type Code':'b', 'C Type':'signed char', 'Python Type':'int', 'Minimum Bytes':'1', }}
    B = {'B':{'Type Code':'B', 'C Type':'unsigned char', 'Python Type':'int', 'Minimum Bytes':'1', }}
    u = {'u':{'Type Code':'u', 'C Type':'PY_UNICODE', 'Python Type':'Unicode character', 'Minimum Bytes':'2', }}
    h = {'h':{'Type Code':'h', 'C Type':'signed short', 'Python Type':'int', 'Minimum Bytes':'2', }}
    b = {'H':{'Type Code':'H', 'C Type':'unsigned short', 'Python Type':'int', 'Minimum Bytes':'2', }}
    i = {'i':{'Type Code':'i', 'C Type':'signed int', 'Python Type':'int', 'Minimum Bytes':'2', }}
    I = {'I':{'Type Code':'I', 'C Type':'unsigned int', 'Python Type':'long', 'Minimum Bytes':'2', }}
    l = {'l':{'Type Code':'l', 'C Type':'signed long', 'Python Type':'int', 'Minimum Bytes':'4', }}
    L = {'L':{'Type Code':'L', 'C Type':'unsinged long', 'Python Type':'long', 'Minimum Bytes':'4', }}
    f = {'f':{'Type Code':'f', 'C Type':'float', 'Python Type':'float', 'Minimum Bytes':'4', }}
    d = {'d':{'Type Code':'d', 'C Type':'double', 'Python Type':'float', 'Minimum Bytes':'8', }}
    df0 = pd.DataFrame(c)
    df1 = pd.DataFrame(b)
    df2 = pd.DataFrame(B)
    df3 = pd.DataFrame(u)
    df4 = pd.DataFrame(h)
    df5 = pd.DataFrame(b)
    df6 = pd.DataFrame(i)
    df7 = pd.DataFrame(I)
    df8 = pd.DataFrame(l)
    df9 = pd.DataFrame(L)
    df10 = pd.DataFrame(f)
    df11 = pd.DataFrame(d)
    table = pd.concat( [df0,df1,df2,df3,df4,df5,df6,df7,df8,df9,df10,df11], axis=1 )
    return table

types_b = [
    {'c':{'Type Code':'c', 'C Type':'char', 'Python Type':'character', 'Minimum Bytes':'1', }},
    {'b':{'Type Code':'b', 'C Type':'signed char', 'Python Type':'int', 'Minimum Bytes':'1', }},
    {'B':{'Type Code':'B', 'C Type':'unsigned char', 'Python Type':'int', 'Minimum Bytes':'1', }},
    {'u':{'Type Code':'u', 'C Type':'PY_UNICODE', 'Python Type':'Unicode character', 'Minimum Bytes':'2', }},
    {'h':{'Type Code':'h', 'C Type':'signed short', 'Python Type':'int', 'Minimum Bytes':'2', }},
    {'H':{'Type Code':'H', 'C Type':'unsigned short', 'Python Type':'int', 'Minimum Bytes':'2', }},
    {'i':{'Type Code':'i', 'C Type':'signed int', 'Python Type':'int', 'Minimum Bytes':'2', }},
    {'I':{'Type Code':'I', 'C Type':'unsigned int', 'Python Type':'long', 'Minimum Bytes':'2', }},
    {'l':{'Type Code':'l', 'C Type':'signed long', 'Python Type':'int', 'Minimum Bytes':'4', }},
    {'L':{'Type Code':'L', 'C Type':'unsinged long', 'Python Type':'long', 'Minimum Bytes':'4', }},
    {'f':{'Type Code':'f', 'C Type':'float', 'Python Type':'float', 'Minimum Bytes':'4', }},
    {'d':{'Type Code':'d', 'C Type':'double', 'Python Type':'float', 'Minimum Bytes':'8', }},
]
def programmatic_table(list_of_dicts): 
    '''
    The Dicts should be in the the format above:
    the name of the data type : followed by a dict of key/value pairs that 
    represent the data type.
    '''
    c = 0
    frames = []
    for i in range(0, len(types_b)):
        df = pd.DataFrame(types_b[i].values())
        #df.rename(index={i: types_b[0].keys()[0]})
        frames.append(df)
        c +=1
    table = pd.concat( frames, )
    table.index=(range(0,len(table)))
    return chart
#table = types_table_manual()
table = programmatic_table(types_b)
print(table)
