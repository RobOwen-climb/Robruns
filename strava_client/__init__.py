import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint
from requests import Session
from typing import Optional, List

#class Client:
#
#    def __init__(self, url: str, API_KEY: str): #the stuff we know we'll need with each request
#        self.base_url = url + "/api/v1/"
#        self.API_KEY = API_KEY
#        self.session = Session()
#        self.session.headers.update({"Authorisation": f"Bearer {API_KEY}"})
#        # The Session object allows you to persist certain parameters across requests
#        # in this case, in means the API key only has to be sent once, and many requests
#        # can then be made

swagger_client.configuration.access_token = ''

# GET https://www.strava.com/oauth/authorize

## Installed swagger




