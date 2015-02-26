from lean_cloud.lean_obj import AVObject
from hmm_senz.core.model import SenzModel
import json

class UserHMM(AVObject, SenzModel):

    def __init__(self, user_id):
        super(UserHMM, self).__init__()
        self.userId = user_id

        model = self._getUserHMMParamsByUserId()
        for i in model:
            print i


    def _getUserHMMParamsByUserId(self):
        # Init the param
        param = {
            "userIdString": self.userId, # Select items which userId is equal to user_id.
        }
        # Get the latest motion rawdata from Database
        response = self.get(
            where=param,       # user id is Equal to userIdString in Database.
            keys="pi,transitionMatrix,emissionMatrix,motionConditionMatrix,locationConditionMatrix,soundConditionMatrix"
        )
        # return the motion data list
        # - If there is no results, it will return an empty list.(eg. [])
        return json.loads(response.content)["results"]


if __name__ == "__main__":

    m = UserHMM("54d82fefe4b0d414801050ee")
