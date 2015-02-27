from lean_cloud.lean_obj import AVObject
from hmm_senz.core.model import SenzModel
import json

class UserHMM(SenzModel, AVObject):

    def __init__(self, user_id):
        # super(UserHMM, self).__init__()
        SenzModel.__init__(self)
        AVObject.__init__(self)

        self.userId = user_id

        # Get hmm model's param from database by user id.
        model_info = self._getUserHMMParamsByUserId()

        # Set the model with these params.
        self._setTransitionMatrix(model_info)
        self._setEmissionMatrix(model_info)
        self._setPi(model_info)



    def _getUserHMMParamsByUserId(self):
        # Init the param
        param = {
            "userIdString": self.userId # Select items which userId is equal to user_id.
        }
        # Get the latest hmm model from Database
        response = self.get(
            order="-timestamp", # Timestamp in Ascended order.
            where=param,       # user id is Equal to userIdString in Database.
            keys="pi,emissionMatrix,transitionMatrix,motionConditionMatrix,locationConditionMatrix,soundConditionMatrix,timestamp",
            limit=1            # Select the latest item of result.
        )
        # return the latest hmm model
        # - If there is no results, it will return an empty list.(eg. [])
        return json.loads(response.content)["results"][0]



    def _setTransitionMatrix(self, model_info):
        # If the transition matrix is exist
        if model_info.has_key("transitionMatrix") and model_info["transitionMatrix"] is not None:
            self.setTransitionP(model_info["transitionMatrix"])
        # If the transition matrix is not exist,
        # then we will generate a new matrix, and store into Database.
        else:
            pass


    def _setEmissionMatrix(self, model_info):
        if model_info.has_key("emissionMatrix") and model_info["emissionMatrix"] is not None:
            self.setEmissionP(model_info["emissionMatrix"])
        else:
            if model_info.has_key("motionConditionMatrix") and model_info["motionConditionMatrix"] is not None:
                self.setMotionConditionP(model_info["motionConditionMatrix"])
            if model_info.has_key("locationConditionMatrix") and model_info["locationConditionMatrix"] is not None:
                self.setLocationConditionP(model_info["locationConditionMatrix"])
            # if model_info.has_key("soundConditionMatrix"):
            #    self.setSoundConditionP(model_info["soundConditionMatrix"])



    def _setPi(self, model_info):
        if model_info.has_key("pi") and model_info["pi"] is not None:
            self.setPi(model_info["pi"])


if __name__ == "__main__":

    m = UserHMM("54d82fefe4b0d414801050ee")
