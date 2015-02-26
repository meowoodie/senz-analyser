from lean_cloud.lean_obj import AVObject
from cloud_services.service_api import ServiceAPI
import json

class UserMotion(AVObject, ServiceAPI):
    '''
    USER MOTION

    Update the specified user's state in Database.
    - Get the user's latest motion raw date from Database
    - Query the user's latest motion state by the raw date
    - Store the state in Database.

    - Param: user id
    '''

    DEFAULT_STATE        = "Unknown"
    DEFAULT_MOTION_DATA  = {}
    DEFAULT_MOTION_COUNT = 100

    # - If user id is not none,
    # - the instantiation of UserMotion will get the rawdata from Database
    def __init__(self, user_id=None, motion_count=DEFAULT_MOTION_COUNT):
        super(UserMotion, self).__init__()
        self.motionData = self.DEFAULT_MOTION_DATA
        self.state      = self.DEFAULT_STATE
        self.userId     = user_id

        # If the user id is none, then over.
        if self.userId is None:
            return

        # Get the set of latest motion data according to user id from Database.
        # - The motion data is a list.
        # - eg. motion_data = [{...},{...}]
        self.motionData = self._getLatestMotionDataByUserId(
            motion_count # The count of motion rawdata we need
        )

        # Extract the raw data & object id from motion data
        raw_data_list  = []
        object_id_list = []
        for motion_data in self.motionData:
            raw_data_list.append(motion_data["rawData"])
            object_id_list.append(motion_data["objectId"])

        # Get the state of set of latest motion data.
        self.state = self._queryMotionStateByMotionData(raw_data_list)

        # Store the result(state of motion data) into Database.
        self._updateStateInDatabase(
            object_id_list, # The list of object id which need to be updated
            self.state      # The update value of state
        )



    def _getLatestMotionDataByUserId(self, count=DEFAULT_MOTION_COUNT):
        # Init the param
        param = {
            "userIdString": self.userId, # Select items which userId is equal to user_id.
        }
        # Get the latest motion rawdata from Database
        response = self.get(
            order="-timestamp", # Timestamp in Ascended order.
            where=param,       # user id is Equal to userIdString in Database.
            limit=count,       # Select the latest 100 item of result.
            keys="rawData,timestamp,objectId"
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
        # Update the data in Database
        self.update_all(update_data_list)



if __name__ == "__main__":

    m = UserMotion("54d82fefe4b0d414801050ee")