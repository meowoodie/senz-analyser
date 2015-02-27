from lean_cloud.lean_obj import AVObject
from user_hmm import UserHMM
from hmm_senz.core.senz import Senz
import json

class UserSenz(Senz, AVObject):

    during = {
        "THIS_DAY":   0,
        "THIS_WEEK":  1,
        "THIS_MONTH": 2,
        "THIS_YEAR":  3
    }
    output_key = (
        "motion",
        "location",
        "sound",
        "light"
    )

    def __init__(self, user_id, **output_tuple):
        self.userId = user_id
        self.outputListDuring   = [] # The latest output list during * from Database
        self.outputTupleCurrent = {} # The Current output tuple (made by other model's computing result)

        model = UserHMM(self.userId)
        # super(UserSenz, self).__init__()
        Senz.__init__(self, model)
        AVObject.__init__(self)

        # Init Current output tuple
        for key in self.output_key:
            if output_tuple.has_key(key):
                self.outputTupleCurrent[key] = output_tuple[key]

        # Add a new visible output tuple into database.
        self._addNewOutputTupleInDatabase(self.outputTupleCurrent)

        # Get the latest visible output list during this (year/month/week/day).
        visible_ouput_list = self._getLatestOutputListByUserId(self.during["THIS_DAY"])

        self.initTrainSample(visible_ouput_list)

        self.BaumWelchLearn(0.01)
        self.ViterbiDecode()





    def _addNewOutputTupleInDatabase(self, output_tuple):
        # Init the param
        param = {
            "userId":        self.Pointer(self.userId),
            "userIdString":  self.userId,
            "timestamp":     self.Date(), # The current time (formate: iso 8601)
            "visibleOutput": output_tuple
        }
        self.save(param)



    def _getLatestOutputListByUserId(self, during):
        # Init the param
        param = {
            "userIdString": self.userId, # Select items which userId is equal to user_id.
            "timestamp": {
                "$gte": self.Date(during)
            }
        }
        # Get the latest visible output list from Database
        response = self.get(
            order="timestamp", # Timestamp in Ascended order.
            where=param,       # user id is Equal to userIdString in Database.
            keys="visibleOutput,timestamp,objectId"
        )
        result = json.loads(response.content)["results"]
        visible_output_list = []
        for item in result:
            visible_output_list.append(item["visibleOutput"])
        # return the visible output data list
        # - If there is no results, it will return an empty list.(eg. [])
        return visible_output_list



    def _getPredictUserSenz(self):
        pass



if __name__ == "__main__":

    m = UserSenz("54d82fefe4b0d414801050ee", motion="RUNNING", location="COMMUNITY")



