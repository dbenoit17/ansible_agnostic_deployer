
import os
import sys
import base64
import getpass
import logging
import logging.handlers

from ravello_sdk import *

def get_credentials():
        with open(os.path.expanduser("~/.ravello_login"),"r") as pf:
                username = pf.readline().strip()
                encrypted_password = pf.readline().strip()
        password = base64.b64decode(encrypted_password).decode()
        return username,password

def get_application_id(application_name,client):
        application_id=0
        for application in client.get_applications():
                if application['name'].lower() == application_name.lower():
                        return application['id']
        raise Exception("no app:" + application_name)
def set_poweroff_timeout(app_id, ttl_mins, client):
   	app = client.get_application(app_id)
        ttl = ttl_mins * 60
        exp_req = {'expirationFromNowSeconds': ttl}
        client.set_application_expiration(app,exp_req)
        client.update_application(app)

def main():
        username, password = get_credentials()
        client = RavelloClient(username, password)
        set_poweroff_timeout(get_application_id(sys.argv[1], client), 
                             int(sys.argv[2]),
                             client)
        
main()
