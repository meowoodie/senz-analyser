from user_model.user_info import UserInfo
from user_model.user_senz import UserSenz
from user_model.user_motion import UserMotion
from user_model.user_poi import UserPOI

class DataHandler(object):

    def __init__(self, uuid):
        # Init user info model,
        # - Get user info from database
        user = UserInfo(uuid)
        # Init user motion model
        user_motion = UserMotion(user.getUserID())
        # Init user poi model
        user_poi    = UserPOI(user.getUserID())

        state = user_motion.getLatestMotionState()
        poi_info = user_poi.getLatestPOIInfo()
        poi_type = poi_info[0]["poiType"]

        output_tuple = {
            "motion"   : state,
            "location" : poi_type
        }
        print output_tuple
        user_senz = UserSenz(user.getUserID())

if __name__ == "__main__":

    m = DataHandler("test_user_mac")




