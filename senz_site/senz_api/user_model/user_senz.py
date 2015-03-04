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

    def __init__(self, user_id, during_time="THIS_DAY", **output_tuple):
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
        senz_info_list = self._getLatestSenzInfoListByUserId(self.during[during_time])

        visible_output_list = []
        object_id_list = []
        old_senz_list = []
        for item in senz_info_list:
            visible_output_list.append(item["visibleOutput"])
            object_id_list.append(item["objectId"])
            old_senz_list.append(item["senz"])

        # Get the new list of Senz.
        new_senz_list = self._getNewUserSenz(visible_output_list, old_senz_list)
        # Save the result in current object
        self.senzList = new_senz_list

        # Update Senz in Database.
        self._updateSenzInDatabase(
            object_id_list,
            new_senz_list
        )

        # Update UserHMM's param in Database.
        model.addHMMParamInDatabase(
            pi=self.getPi(),
            emission=self.getEmission(),
            transition=self.getTransition()
        )



    def _addNewOutputTupleInDatabase(self, output_tuple):
        # Init the param
        param = {
            "userId":        self.Pointer(self.userId),
            "userIdString":  self.userId,
            "timestamp":     self.Date(), # The current time (formate: iso 8601)
            "visibleOutput": output_tuple
        }
        self.save(param)



    def _getLatestSenzInfoListByUserId(self, during):
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
            keys="senz,visibleOutput,timestamp,objectId"
        )
        result = json.loads(response.content)["results"]
        # return the visible output data list
        # - If there is no results, it will return an empty list.(eg. [])
        return result



    def _getNewUserSenz(self, visible_output_list, old_senz_list):
        # Init the training sample.
        self.initTrainSample(visible_output_list)
        # Train.
        self.BaumWelchLearn(0.01)
        self.ViterbiDecode()
        # Get predict result.
        doing_list = self.getQ()
        # Generate the senz and return it.
        i = 0
        for senz in old_senz_list:
            senz["doing"] = doing_list[i]
            i += 1
        return old_senz_list



    def _updateSenzInDatabase(self, object_id_list, senz_list):
        # Create the dict of update data
        update_data_list = []
        i = 0
        for ob in object_id_list:
            tmp_dict = {
                "objectId": ob,
                "senz": senz_list[i]
            }
            update_data_list.append(tmp_dict)
            i += 1
        # Update the data in Database
        self.update_all(update_data_list)



    # PUBLIC METHOD
    def getLatestSenzList(self):
        return self.senzList



if __name__ == "__main__":

    m = UserSenz("54d82fefe4b0d414801050ee", during_time="THIS_WEEK", motion="SITTING", location="EDUCATION")




