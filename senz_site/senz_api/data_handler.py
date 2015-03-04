from user_model.user_info import UserInfo
from user_model.user_senz import UserSenz
from user_model.user_motion import UserMotion
from user_model.user_poi import UserPOI

class DataHandler(object):

    def __init__(self, uuid, during_time="THIS_DAY"):
        # Init user info model,
        # - Get user info from database
        self.user = UserInfo(uuid)
        # Init user motion model
        self.userMotion = UserMotion(self.user.getUserID())
        # Init user poi model
        self.userPOI    = UserPOI(self.user.getUserID())
        # Init the during time
        self.duringTime = during_time



    def getUserSenz(self, motion_count=100, poi_count=5, sound_count=100):

        state_info = self.userMotion.getLatestMotionState(motion_count)
        poi_info   = self.userPOI.getLatestPOIInfo(poi_count)

        latest_state = state_info["state"]
        loc_type     = poi_info["locType"]

        user_senz = UserSenz(
            self.user.getUserID(),
            during_time=self.duringTime,
            motion=latest_state,
            location=loc_type
        )

        return user_senz.getLatestSenzList()


if __name__ == "__main__":

    m = DataHandler("test_user_mac")
    m.getUserSenz()




