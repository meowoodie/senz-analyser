
class DataHandler(object):

    def __init__(self, user_id):
        self._userId = user_id

    # --- QUERY EVENT ---

    # [Context]
    # * Get users' context info from DATABASE
    # - Send: userId
    # - Receive: motion(rawdata), poi(GPS or iBeacon), sound(rawData)
    def getUserContext(self):
        pass

    # [Motion State]
    # * Query users' motion state from CLOUD SERVICE
    # - Send: motion(rawdata)
    # - Receive: motion(state)
    def getUserMotionState(self):
        pass

    # [POI Type & Description]
    # * Query users' poi type and description from CLOUD SERVICE
    # - Send: poi(GPS or iBeacon)
    # - Receive: poi(type)
    def getUserPOI(self):
        pass

    # [Sound Scence]
    # * Query users' sound scence from CLOUD SERVICE
    # - Send: sound(rawdata)
    # - Receive: sound(scence)
    def getUserSoundScence(self):
        pass


    # --- STORAGE EVENT ---

    # [Visible Output]
    # * Store the visible output (computed by analyser) into DATABASE
    # - Send: motion(state), poi(type), sound(scence)
    def setCurVisibleOutput(self):
        pass

    # [Senz]
    # * Store the senz (computed by analyser) into DATABASE
    # - Send: senz
    def setCurSenz(self):
        pass


