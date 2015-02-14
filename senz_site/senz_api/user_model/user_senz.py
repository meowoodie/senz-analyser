from lean_cloud.lean_obj import AVObject

class UserSenz(AVObject):

    during = {
        "A_DAY":   0,
        "A_WEEK":  1,
        "A_MONTH": 2,
        "A_YEAR":  3
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

        self._addNewOutputTupleInDatabase(self.outputTupleCurrent)
        # self.Date()
        self._getLatestOutputListByUserId(self.during["A_DAY"])




    def _addNewOutputTupleInDatabase(self, output_tuple):
        param = {
            "userId":        self.Pointer(self.userId),
            "userIdString":  self.userId,
            "timestamp":     self.Date(),
            "visibleOutput": output_tuple
        }
        print self.save(param).content



    def _getLatestOutputListByUserId(self, during):
        pass

if __name__ == "__main__":

    m = UserSenz("54d82fefe4b0d414801050ee", motion="RUNNING", location="Tiananmen")



