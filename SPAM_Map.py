#!/usr/bin/env python
#Extract and Map SPAM from your gmail account
import argparse
import getpass
import imaplib

def authenticate():
    GOOGLE_IMAP_SERVER = 'imap.googlemail.com'
    username=(raw_input("Enter Your Google account name: "))
    mailbox = imaplib.IMAP4_SSL(GOOGLE_IMAP_SERVER, '993') 
    password = getpass.getpass(prompt="Enter your Google password: ") 
    mailbox.login(username, password)
def grab_SPAM():
    mailbox.select('[Gmail]/Spam')
    typ, data = mailbox.search(None, 'ALL')