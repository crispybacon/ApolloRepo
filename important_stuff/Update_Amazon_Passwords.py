#!/usr/bin/env python
#TODO
#Logging
#Account Change Report
#Password update verification test 
import boto, time, os, urllib
import pandas as pd
from boto.iam.connection import IAMConnection
df = pd.DataFrame.from_csv('Jujitsu.csv')
df1 = pd.DataFrame.from_csv('IAM_passwords.csv')
# Missing from the file is the IAM password list 
# This script assumes that an IAM password list exists
IAM_Passwords = df1['passwords']
IAM_Users = df[' IAM User'] # Grab the users
Access_keys = df['Access Key'] # Grab the Ids
Secret_keys = df['Secret Key'] # Grab the Keys
credentials = zip(Access_keys, Secret_keys)
df2 = pd.DataFrame.from_csv('Rollover_passwords.csv')
new_passwords = df2['passwords']
x = len(new_passwords) 
for num in range(0,x)
    b_user = IAMConnection( credentials[num][0], credentials[num][1] )
    b_user.update_login_profile('royce_gracie', newpasswords[num])
    #b_user.get_account_password_policy()
    #b_user.get_account_summary()