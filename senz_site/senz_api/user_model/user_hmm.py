from lean_cloud.lean_obj import AVObject
from hmm_senz.core.model import SenzModel
import json

class UserHMM(AVObject, SenzModel):

    def __init__(self, user_id):
        super(UserHMM, self).__init__()
        self.userId = user_id



if __name__ == "__main__":

    m = UserHMM("54d82fefe4b0d414801050ee")
