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
    DEFAULT_POI_COUNT = 1


    def __init__(self, user_id=None):
        # super(UserPOI, self).__init__()
        AVObject.__init__(self)
        ServiceAPI.__init__(self)

        self.poiData     = self.DEFAULT_POI_DATA
        self.poiInfoList = [self.DEFAULT_POI_INFO]
        self.userId      = user_id



    def _getLatestPOIDataByUserId(self, poi_count=DEFAULT_POI_COUNT):
        # Init the param
        param = {
            "userIdString": self.userId, # Select items which userId is equal to user_id.
        }
        # Get the latest poi data(GPS & Beacon) from Database
        response = self.get(
            order="timestamp", # Timestamp in Ascended order.
            where=param,       # user id is Equal to userIdString in Database.
            limit=poi_count,   # Select the latest 100 item of result.
            keys="locBeacon,locGPS,timestamp,objectId"
        )
        # return the poi data list
        # - If there is no results, it will return an empty list.(eg. [])
        return json.loads(response.content)["results"]



    def _queryPOIInfoByPOIData(self, poi_info_post):
        return self.getPOIInfoFromCloudService(poi_info_post)



    def _updatePOIInfoInDatabase(self, object_id_list, poi_info_list):
        # Create the dict of update data
        update_data_list = []
        i = 0
        for ob in object_id_list:
            tmp_dict = {
                "objectId":       ob,
                "poiType":        poi_info_list[i]["poiType"],
                "locType":        poi_info_list[i]["locType"],
                "locDescription": poi_info_list[i]["locDescription"]
            }
            update_data_list.append(tmp_dict)
            i += 1
        # Update the data in Database
        self.update_all(update_data_list)



    def _analysePOI(self, poi_result):
        # The result of GPS, it is a list
        gps_result = poi_result["GPS"]
        # The result of iBeacon, it is a list
        ibeacon_result = poi_result["iBeacon"]

        if len(ibeacon_result) > 0:
            return ibeacon_result[0]
        elif (len(ibeacon_result) is 0) and (len(gps_result) > 0):
            return gps_result[0]
        else:
            return None



    # PUBLIC METHOD
    def getLatestPOIInfo(self, poi_count=DEFAULT_POI_COUNT):
        '''
        GET LATEST POI INFO

        :param poi_count:
        :return:
        '''
        # Get the set of latest poi data according to user id from Database.
        # - The poi data is a list.
        # - eg. poi_data = [{...},{...}]
        self.poiData = self._getLatestPOIDataByUserId(
            poi_count
        )
        # Extract the poi data & object id from motion data
        poi_info_post  = {
            "GPS": [],
            "iBeacon": [],
            "userId": self.userId
        }
        gps_object_id_list     = []
        ibeacon_object_id_list = []
        for poi_data in self.poiData:
            # poi info
            if poi_data.has_key("locGPS") and poi_data["locGPS"] is not None:
                tmp = {}
                tmp["latitude"]  = poi_data["locGPS"]["latitude"]
                tmp["longitude"] = poi_data["locGPS"]["longitude"]
                tmp["timestamp"] = self.iso2timestamp(poi_data["timestamp"]["iso"])
                poi_info_post["GPS"].append(tmp)
                gps_object_id_list.append(poi_data["objectId"])
            if poi_data.has_key("locBeacon") and poi_data["locBeacon"] is not None:
                tmp = {}
                tmp["uuid"]      = poi_data["locBeacon"]["uuid"]
                tmp["major"]     = poi_data["locBeacon"]["major"]
                tmp["minor"]     = poi_data["locBeacon"]["minor"]
                tmp["rssi"]      = poi_data["locBeacon"]["rssi"]
                tmp["timestamp"] = self.iso2timestamp(poi_data["timestamp"]["iso"])
                poi_info_post["iBeacon"].append(tmp)
                ibeacon_object_id_list.append(poi_data["objectId"])
        # Get the latest poi type&description set of poi data.
        self.poiInfoList = self._queryPOIInfoByPOIData(poi_info_post)
        # Store the result into Database.
        self._updatePOIInfoInDatabase(
            gps_object_id_list,     # The list of gps object id which need to be updated
            self.poiInfoList["GPS"] # The update value of poi info
        )
        self._updatePOIInfoInDatabase(
            ibeacon_object_id_list,     # The list of gps object id which need to be updated
            self.poiInfoList["iBeacon"] # The update value of poi info
        )

        return self._analysePOI(self.poiInfoList)




if __name__ == "__main__":

    m = UserPOI("54d82fefe4b0d414801050ee")
    print m.getLatestPOIInfo()
