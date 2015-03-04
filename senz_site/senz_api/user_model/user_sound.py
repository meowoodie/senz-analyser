from lean_cloud.lean_obj import AVObject
from cloud_services.service_api import ServiceAPI
import json

class UserSound(AVObject):

    DEFAULT_STATE   = 'SITTING'
    DEFAULT_RAWDATA = {}

    # If user id is not none,
    # the instantiation of UserMotion will get the rawdata from LeanCloud
    def __init__(self, user_id=None):
        # super(UserMotion, self).__init__()
        AVObject.__init__(self)

        self.rawData = self.DEFAULT_RAWDATA
        self.state   = self.DEFAULT_STATE
        self.userId  = user_id

        if user_id is not None:
            # Get the latest motion rawdata from LeanCloud
            response = self.get(self.userId)
            # Decode result as dict.

            print 'result:', json.loads(response.content)['rowData']
            # Store the motion rawData in private member.


    def getState(self):
        pass

    def saveState(self):
        pass


if __name__ == "__main__":

    m = UserMotion('54d62b86e4b09b3f3119ba6a')