from lean_cloud.lean_obj import AVObject
from cloud_services.service_api import ServiceAPI
import json

class UserPOI(AVObject, ServiceAPI):

    DEFAULT_POI_DATA = {
        "locGPS":    {
            "latitude": 39.9096046,
            "longitude": 116.3972282
        },
        "locBeacon": ""
    }
    DEFAULT_POI_INFO = {
        "poiType": "",
        "locDescription": ""
    }


    def __init__(self, user_id=None):
        super(UserPOI, self).__init__()
        self.poiData = self.DEFAULT_POI_DATA
        self.poiInfo = self.DEFAULT_POI_INFO
        self.userId         = user_id

        # If the user id is none, then over.
        if self.userId is None:
            return

        self._getLatestPOIDataByUserId(
            self.userId,
            count=3
        )


    def _getLatestPOIDataByUserId(self, user_id, count=3):
        # Init the param
        param = {
            "userIdString": user_id, # Select items which userId is equal to user_id.
        }
        # Get the latest motion rawdata from LeanCloud
        response = self.get(
            order="timestamp", # Timestamp in Ascended order.
            where=param,       # user id is Equal to userIdString in LeanCloud.
            limit=count,       # Select the latest 100 item of result.
            keys="locGPS, locBeacon, timestamp, objectId"
        )
        # return the motion data list
        # - If there is no results, it will return an empty list.(eg. [])
        return json.loads(response.content)["results"]



    def _queryPOIInfoByPOIData(self):
        pass

if __name__ == "__main__":

    m = UserPOI("54d82fefe4b0d414801050ee")
