from lean_cloud.lean_obj import AVObject
import json

class UserSenz(AVObject):

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
        super(UserSenz, self).__init__()
        self.userId = user_id
        self.outputListDuring   = [] # The latest output list during * from Database
        self.outputTupleCurrent = {} # The Current output tuple (made by other model's computing result)
        # Init Current output tuple
        for key in self.output_key:
            if output_tuple.has_key(key):
                self.outputTupleCurrent[key] = output_tuple[key]

        # self._addNewOutputTupleInDatabase(self.outputTupleCurrent)

        result = self._getLatestOutputListByUserId(self.during["THIS_YEAR"])

        for i in result:
            print i
        print len(result)




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
        # Get the latest poi data(GPS & Beacon) from Database
        response = self.get(
            order="timestamp", # Timestamp in Ascended order.
            where=param,       # user id is Equal to userIdString in Database.
            keys="visibleOutput,timestamp,objectId"
        )
        # return the poi data list
        # - If there is no results, it will return an empty list.(eg. [])
        return json.loads(response.content)["results"]

if __name__ == "__main__":

    m = UserSenz("54d82fefe4b0d414801050ee", motion="RUNNING", location="Tiananmen")



