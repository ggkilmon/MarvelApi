from BaseRequest import BaseRequest
from RequestType import RequestType
from calendar import datetime
import numpy as np

class CharactersRequest(BaseRequest):
    def __init__(self):
        BaseRequest.__init__(self, RequestType.CHARACTERS)
    

    def get_name(self) -> str:
        return self._name
    def set_name(self, value: str):
        self._name = value
    name = property(get_name, set_name)


    def get_nameStartsWith(self) -> str:
        return self._nameStartsWith
    def set_nameStartsWith(self, value: str):
        self._nameStartsWith = value
    nameStartsWith = property(get_nameStartsWith, set_nameStartsWith)


    def get_modifiedSince(self) -> datetime:
        return self._modifiedSince
    def set_modifiedSince(self, value: datetime):
        self._modifiedSince = value
    modifiedSince = property(get_modifiedSince, set_modifiedSince)


    def get_comicsIds(self) -> np.array([], dtype='i'):
        return self._comicsIds
    def set_comicsIds(self, value: np.array([], dtype='i')):
        self._comicsIds = value
    comicsIds = property(get_comicsIds, set_comicsIds)


    def get_seriesIds(self) -> np.array([], dtype='i'):
        return self._seriesIds
    def set_seriesIds(self, value: np.array([], dtype='i')):
        self._seriesIds = value
    seriesIds = property(get_seriesIds, set_seriesIds)


    def get_eventsIds(self) -> np.array([], dtype='i'):
        return self._eventsIds
    def set_eventsIds(self, value: np.array([], dtype='i')):
        self._eventsIds = value
    eventsIds = property(get_eventsIds, set_eventsIds)


    def get_storiesIds(self) -> np.array([], dtype='i'):
        return self._storiesIds
    def set_storiesIds(self, value: np.array([], dtype='i')):
        self._storiesIds = value
    storiesIds = property(get_storiesIds, set_storiesIds)


    def get_orderBy(self) -> np.array([], dtype='i'):
        return self._orderBy
    def set_orderBy(self, value: np.array([], dtype='i')):
        self._orderBy = value
    orderBy = property(get_orderBy, set_orderBy)