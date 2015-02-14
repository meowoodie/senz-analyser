from lean_cloud.lean_obj import AVObject

class UserSenz(AVObject):

    during = {
        "A_DAY":   0,
        "A_WEEK":  1,
        "A_MONTH": 2,
        "A_YEAR":  3
    }
    output_key = (
        "Motion",
        "POI",
        "Sound",
        "Light"
    )
    DEFAULT_SENZ_DURING = during["A_DAY"]

    def __init__(self, user_id=None, during=DEFAULT_SENZ_DURING, **output_tuple):
        super(UserSenz, self).__init__()
        self.userId = user_id
        self.outputListDuring   = [] # The latest output list during * from Database
        self.outputTupleCurrent = {}
        # Init Current output tuple
        for key in self.output_key:
            if output_tuple.has_key(key):
                self.outputTupleCurrent[key] = output_tuple[key]

