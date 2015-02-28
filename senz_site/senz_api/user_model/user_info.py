from lean_cloud.lean_obj import AVObject
import json

class UserInfo(AVObject):

    def __init__(self, uuid):
        self.UUID = uuid
        self.userId = self._getUserIdByUUID()



    def _getUserIdByUUID(self):
        # Init the param
        param = {
            "mac": self.UUID # Select items which mac is equal to uuid.
        }
        # Get the latest hmm model from Database
        response = self.get(
            where=param,       # user id is Equal to userIdString in Database.
            limit=1            # Select the latest item of result.
        )
        # return the latest hmm model
        # - If there is no results, it will return an empty list.(eg. [])
        return json.loads(response.content)["results"][0]["objectId"]



    # PUBLIC METHOD
    def getUserID(self):
        return self.userId


if __name__ == "__main__":

    m = UserInfo("test_user_mac")