from lean_cloud.lean_obj import AVObject
from cloud_services.service_api import ServiceAPI
import json

class UserPOI(AVObject, ServiceAPI):

    DEFAULT_POI_DATA = {
        "locGPS":    {
            "latitude": 39.9096046,
            "longitude": 116.3972282
        },
        "locBeacon": "None"
    }
    DEFAULT_POI_INFO = {
        "poiType": "Other",
        "locDescription": "None"
    }


    def __init__(self, user_id=None):
        super(UserPOI, self).__init__()
        self.poiData = self.DEFAULT_POI_DATA
        self.poiInfo = self.DEFAULT_POI_INFO
        self.userId         = user_id

        # If the user id is none, then over.
        if self.userId is None:
            return

        # Get the set of latest poi data according to user id from LeanCloud.
        # - The poi data is a list.
        # - eg. poi_data = [{...},{...}]
        self._getLatestPOIDataByUserId(
            self.userId,
            count=3
        )

        # Extract the poi data & object id from motion data
        poi_info_list  = []
        object_id_list = []
        for poi_data in self.motionData:
            # poi info
            poi_info = {
                "locGPS":    {
                    "latitude": poi_data["locGPS"]["latitude"],
                    "longitude": poi_data["locGPS"]["longitude"]
                },
                "locBeacon": poi_data["locBeacon"]
            }
            poi_info_list.append(poi_info)
            # object id
            object_id_list.append(poi_data["objectId"])

        # Get the poi type & description set of latest poi data.
        self._queryPOIInfoByPOIData(poi_info_list)




    def _getLatestPOIDataByUserId(self, user_id, count=3):
        # Init the param
        param = {
            "userIdString": user_id, # Select items which userId is equal to user_id.
        }
        # Get the latest poi data(GPS & Beacon) from LeanCloud
        response = self.get(
            order="timestamp", # Timestamp in Ascended order.
            where=param,       # user id is Equal to userIdString in LeanCloud.
            limit=count,       # Select the latest 100 item of result.
            keys="locBeacon,locGPS,timestamp,objectId"
        )
        # return the poi data list
        # - If there is no results, it will return an empty list.(eg. [])
        return json.loads(response.content)["results"]



    def _queryPOIInfoByPOIData(self):
        pass

if __name__ == "__main__":

    m = UserPOI("54d82fefe4b0d414801050ee")
