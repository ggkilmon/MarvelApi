from RequestType import RequestType

class BaseRequest:
    def __init__(self, requestType: RequestType):
        self.requestType = requestType
        self.offset = 0
        self.limit = 0
    
    def get_offset(self) -> int:
        return self._offset
    def set_offset(self, value: int):
        self._offset = value
    offset = property(get_offset, set_offset)


    def get_limit(self) -> int:
        return self._limit
    def set_limit(self, value: int):
        self._limit = value
    limit = property(get_limit, set_limit)

    def get_requestType(self) -> RequestType:
        return self._requestType
    def set_requestType(self, value: RequestType):
        self._requestType = value
    requestType = property(get_requestType, set_requestType)