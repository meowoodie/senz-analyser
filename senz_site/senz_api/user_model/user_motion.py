# from senz_api.lean_cloud.lean_obj import AVObject
from lean_cloud.lean_obj import AVObject
import json
import requests

class UserMotion(AVObject):

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
        self.motionData = self._getLatestMotionDataByUserId(self.userId)

        # self.motionData = {'timestamp':5857542057676,'values':[7.8529816,7.1790137,4.2999864],'sensorName':'acc','accuracy':0}
        # Get the state of set of latest motion data.
        self.state = self._queryMotionStateByMotionData(self.motionData)

        # Store the result(state of motion data) into LeanCloud.
        self._saveStateIntoDatabase(self.state)

    def _getLatestMotionDataByUserId(self, user_id):
        # Init the param
        param = {
            "userIdString": user_id, # Select items which userId is equal to user_id.
        }
        # Get the latest motion rawdata from LeanCloud
        response = self.get(
            order="timestamp", # Timestamp in Ascended order.
            where=param,       # user id is Equal to userIdString in LeanCloud.
            limit=100,         # Select the latest 100 item of result.
            include="rawData"
        )
        # return the motion data list
        # - If there is no results, it will return an empty list.(eg. [])
        return json.loads(response.content)["results"]

    def _queryMotionStateByMotionData(self, motion_data):
        # Init the param
        param = {
            "clfType": ["SS"],
            "rawData": motion_data
        }
        # Query the motion state
        response = requests.post(
            self.URL_MOTION_SERVICE,
            params=param,
            verify=False
        )
        print response.content

    def _saveStateIntoDatabase(self, state):
        pass



if __name__ == "__main__":

    m = UserMotion("54d82fefe4b0d414801050ee")