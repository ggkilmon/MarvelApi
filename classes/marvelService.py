from datetime import datetime
import hashlib
import requests

class MarvelService:
    def __init__(self, baseUrl, publicKey, privateKey):
        self.baseUrl = baseUrl
        self.publicKey = publicKey
        self.privateKey = privateKey


    def request(self, requestType, params={}):
        params = self.addRequiredParams(params)
        requestUrl = self.baseUrl + requestType
        res = requests.get(url = requestUrl, params = params)
        res = self.EnsureSuccessResponse(res)
        response = res.json()
        return response
        
    
    def addRequiredParams(self, params):
        timestamp = self.getTimestamp()
        md5hash = self.generateHash(timestamp)

        params['ts'] = timestamp
        params['apikey'] = self.publicKey
        params['hash'] = md5hash
        return params


    def generateHash(self, timestamp):
        hashString = timestamp + self.privateKey + self.publicKey
        return str(hashlib.md5(hashString.encode()).hexdigest())
    

    def getTimestamp(self):
        return str(datetime.now().time())

    
    def EnsureSuccessResponse(self, res):
        print(res.status_code)
        if res.status_code == 200:
            return res
        elif res.status_code == 409:
            raise Exception('API: Authorization Error - Check API Key')
        elif res.status_code == 401:
            raise Exception('API: Authorization Error - Check API referer configuration')
        elif res.status_code == 405:
            raise Exception('API: Authorization Error - Method not allowed - {requestType}')
        elif res.status_code == 403:
            raise Exception('API: Authorization Error - Forbidden')
        else:
            raise Exception('API: Unknown Error')