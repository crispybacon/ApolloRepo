import argparse
import getpass
import imaplib
#Backup your Gmail over Imap to the current directory
GOOGLE_IMAP_SERVER = 'imap.googlemail.com'
username=(raw_input("Enter Your Google account name: "))
mailbox = imaplib.IMAP4_SSL(GOOGLE_IMAP_SERVER, '993') 
password = getpass.getpass(prompt="Enter your Google password: ") 
mailbox.login(username, password)
mailbox.select('Inbox')
typ, data = mailbox.search(None, 'ALL')
for message in data[0].split():
    ret_message=mailbox.fetch(message, '(RFC822)')
    with open(str(message), 'w') as f:
        f.write(str(ret_message[1][0]))