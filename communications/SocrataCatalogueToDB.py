import pymysql,requests
import pandas as pd
import re

connection = pymysql.connect(host='localhost', user='root')
cursor = connection.cursor()

cursor.execute('''drop database if exists socrata;''')
cursor.execute('''create database socrata;''')
cursor.execute('''use socrata;''')

catalogue = requests.get('https://api.us.socrata.com/api/catalog/v1')
cat_dict = catalogue.json()
cat_dict = cat_dict['results']

def listToCSV(alist):
    csv = ''
    for value in range(len(alist)):
        if value == 0:
            csv += alist[value]
        else:
            csv += ', ' + str(alist[value])
    return csv

cursor.execute('''CREATE TABLE `datasources` (
  `index` bigint(20) DEFAULT NULL,
  `link` varchar(255) DEFAULT NULL,
  `domain` varchar(255) DEFAULT NULL,
  `Dataset_Information_Secondary_Source_Link` varchar(63) DEFAULT NULL,
  `API_And_Download_Information_Available_Download_Formats` varchar(255) DEFAULT NULL,
  `type` varchar(255) DEFAULT NULL,
  `name` varchar(255) DEFAULT NULL,
  `categories` varchar(255) DEFAULT NULL,
  `domain_category` varchar(255) DEFAULT NULL,
  `description` varchar(1024) DEFAULT NULL,
  `updatedAt` varchar(255) DEFAULT NULL,
  `Dataset_Information_DatasetId` varchar(255) DEFAULT NULL,
  `Publisher_Information_Publisher_Phone_Number` varchar(255) DEFAULT NULL,
  `Dataset_Information_Secondary_Data_Provided_By` varchar(255) DEFAULT NULL,
  `Dataset_Information_Time_Coverage` varchar(255) DEFAULT NULL,
  `Dataset_Information_Language` varchar(255) DEFAULT NULL,
  `Creator_Information_Creator_Phone_Number` varchar(255) DEFAULT NULL,
  `API_And_Download_Information_Dataset_API_Format` varchar(255) DEFAULT NULL,
  `API_And_Download_Information_API_Access_Endpoint` varchar(255) DEFAULT NULL,
  `Publisher_Information_Publisher_Email` varchar(255) DEFAULT NULL,
  `Dataset_Information_Alternate_Title` varchar(255) DEFAULT NULL,
  `Creator_Information_Creator_Email` varchar(255) DEFAULT NULL,
  `Usage_Usage_Consideration` varchar(255) DEFAULT NULL,
  `Dataset_Information_Sensitivity` varchar(255) DEFAULT NULL,
  `Publisher_Information_Publisher_Website_URL` varchar(255) DEFAULT NULL,
  `Dataset_Information_Attribution_Source` varchar(255) DEFAULT NULL,
  `Dataset_Information_Frequency` varchar(255) DEFAULT NULL,
  `Dataset_Summary_Granularity` varchar(255) DEFAULT NULL,
  `Dataset_Summary_Dataset_Owner` varchar(255) DEFAULT NULL,
  `Dataset_Summary_Contact_Information` varchar(255) DEFAULT NULL,
  `Dataset_Summary_Posting_Frequency` varchar(255) DEFAULT NULL,
  `Dataset_Summary_Time_Period` varchar(255) DEFAULT NULL,
  `Dataset_Summary_Data_Frequency` varchar(255) DEFAULT NULL,
  `Dataset_Summary_Coverage` varchar(255) DEFAULT NULL,
  `Dataset_Summary_Organization` varchar(255) DEFAULT NULL,
  `Dataset_Information_Agency` varchar(255) DEFAULT NULL,
  `Dataset_Summary_Units` varchar(255) Default NUll,
  `Data_Owner_Owner` varchar(255) DEFAULT NULL,
  `Common_Core_Publisher` varchar(255) DEFAULT NULL,
  `Common_Core_Contact_Name` varchar(255) DEFAULT NULL,
  `Common_Core_Contact_Email` varchar(255) DEFAULT NULL,
  `Common_Core_Program_Code` varchar(255) DEFAULT NULL,
  `Common_Core_Bureau_Code` varchar(255) DEFAULT NULL,
  `Additional_Resources_See_Also` varchar(255) DEFAULT NULL,
  `General_Information_ExtraGeneralInfo` TEXT DEFAULT NULL,
  `Metadata_Frequency` VARCHAR(255),
  `Metadata_Time_Period` VARCHAR(255),
  `Metadata_Data_Owner` VARCHAR(255),
  `Notes_Notes` text DEFAULT NULL,
  `Test_Test` text DEFAULT NULL,
  `Test_Custom_Field` VARCHAR(255),
  `tags` varchar(255) DEFAULT NULL,
  `Creator_Information_Creator_Website_URL` varchar(255) DEFAULT NULL,
  `permalink` varchar(255) DEFAULT NULL,
  `id` varchar(255) DEFAULT NULL,
  `domain_tags` varchar(1024) DEFAULT NULL,
  KEY `ix_datasources_index` (`index`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
''')

for i in range(len(cat_dict)):
    values = {}
    resource = cat_dict[i]['resource']
    values['id'] = resource['id']
    values['name'] = resource['name']
    values['type'] = resource['type']
    values['updatedAt'] = resource['updatedAt']
    values['description'] = resource['description']
    values['link'] = cat_dict[i]['link']
    values['domain'] = cat_dict[i]['metadata']['domain']
    values['permalink'] = cat_dict[i]['permalink']
    classification = cat_dict[i]['classification']
    domain_category = classification['domain_category']
    categories = classification['categories']
    domain_tags = classification['domain_tags']
    tags = classification['tags']
    domain_metadata = classification['domain_metadata']
    values['domain_tags'] = listToCSV(domain_tags)
    values['tags'] = listToCSV(tags)
    values['domain_category'] = listToCSV(domain_category)
    values['categories'] = listToCSV(categories)
    for entry in domain_metadata:
        key = re.sub('-','_', entry['key'])
        if key == 'API_&_Download_Information_API_Access_Endpoint':
            key = 'API_And_Download_Information_API_Access_Endpoint'
        elif key == 'API_&_Download_Information_Dataset_API_Format':
            key = 'API_And_Download_Information_Dataset_API_Format'
        elif key == 'API_&_Download_Information_Available_Download_Formats':
            key = 'API_And_Download_Information_Available_Download_Formats'
        elif key in ['Additional_Resources_See_Also__','Additional_Resources_See_Also_']:
            key = 'Additional_Resources_See_Also'
        values[key] = entry['value']
    for value in values.keys():
        values[value] = values[value].encode('utf-8').decode('latin1').encode('latin1')
    df = pd.DataFrame.from_dict(values, 'index').T
    df.to_sql('datasources', connection, flavor='mysql', schema='socrata', if_exists='append', index=True,)