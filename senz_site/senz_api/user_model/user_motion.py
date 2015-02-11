# from senz_api.lean_cloud.lean_obj import AVObject
from lean_cloud.lean_obj import AVObject
from cloud_services.service_api import ServiceAPI
import json
# import requests

class UserMotion(AVObject, ServiceAPI):

    DEFAULT_STATE       = "SITTING"
    DEFAULT_MOTION_DATA = {}

    # - If user id is not none,
    # - the instantiation of UserMotion will get the rawdata from LeanCloud
    def __init__(self, user_id=None):
        '''
        THE INIT OF USER MOTION

        :param user_id:
        :return:
        '''
        super(UserMotion, self).__init__()
        self.motionData = self.DEFAULT_MOTION_DATA
        self.state      = self.DEFAULT_STATE
        self.userId     = user_id

        # If the user id is none, then over.
        if user_id is None:
            return

        # Get the set of latest motion data according to user id from LeanCloud.
        # - The motion data is a list.
        # - eg. motion_data = [{...},{...}]
        self.motionData = self._getLatestMotionDataByUserId(
            self.userId, # The corresponding user's id
            100          # The count of motion rawdata we need
        )

        # Extract the raw data & object id from motion data
        raw_data_list  = []
        object_id_list = []
        for motion_data in self.motionData:
            raw_data_list.append(motion_data["rawData"])
            object_id_list.append(motion_data["objectId"])

        # Get the state of set of latest motion data.
        self.state = self._queryMotionStateByMotionData(raw_data_list)

        # Store the result(state of motion data) into LeanCloud.
        self._updateStateInDatabase(object_id_list, self.state)



    def _getLatestMotionDataByUserId(self, user_id, count=100):
        # Init the param
        param = {
            "userIdString": user_id, # Select items which userId is equal to user_id.
        }
        # Get the latest motion rawdata from LeanCloud
        response = self.get(
            order="timestamp", # Timestamp in Ascended order.
            where=param,       # user id is Equal to userIdString in LeanCloud.
            limit=count,       # Select the latest 100 item of result.
            keys="rawData, timestamp, objectId"
        )
        # return the motion data list
        # - If there is no results, it will return an empty list.(eg. [])
        return json.loads(response.content)["results"]



    def _queryMotionStateByMotionData(self, raw_data_list):
        # Invoke the cloud service interface.
        return self.getMotionStateFromCloudService(
            raw_data_list, # The training sample motion data
            ["SS", "VH"]   # It's the training strategy
        )



    def _updateStateInDatabase(self, object_id_list, state = "UNKNOWN"):
        # Create the dict of update data
        update_data_list = []
        for ob in object_id_list:
            tmp_dict = {
                "objectId": ob,
                "state": state
            }
            update_data_list.append(tmp_dict)
        # Update the data in LeanCloud
        self.update_all(update_data_list)



if __name__ == "__main__":

    m = UserMotion("54d82fefe4b0d414801050ee")