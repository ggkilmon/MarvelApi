from datetime import datetime
import hashlib
import requests

class MarvelService:
    def __init__(self, baseUrl, publicKey, privateKey):
        self.baseUrl = baseUrl
        self.publicKey = publicKey
        self.privateKey = privateKey


    def request(self, requestType, params={}):
        timestamp = self.getTimestamp()
        md5hash = self.generateHash(timestamp)

        requestUrl = self.baseUrl + requestType

        params['ts'] = timestamp
        params['apikey'] = self.publicKey
        params['hash'] = md5hash

        r = requests.get(url = requestUrl, params = params)
        
        return r.json()


    def generateHash(self, timestamp):
        hashString = timestamp + self.privateKey + self.publicKey
        return str(hashlib.md5(hashString.encode()).hexdigest())
    

    def getTimestamp(self):
        return str(datetime.now().time())