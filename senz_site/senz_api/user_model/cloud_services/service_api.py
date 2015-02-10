import json
import settings
import requests

class ServiceAPI:

    get_motion_state_api = settings.protocol + settings.server_ip["Aliyun1"] + settings.get_motion_state_url
    get_sound_scence_api = settings.protocol + settings.server_ip["Aliyun1"] + settings.get_sound_scence_url
    get_poi_info_api     = settings.protocol + settings.server_ip["Aliyun1"] + settings.get_poi_info_url

    def __init__(self):
        pass

    # --- PRIVATE METHOD ---
    @classmethod
    def headers(cls):
        # Since properties only work on instances, need define headers property in meta class
        return {
            "Content-Type": "application/json"
        }

    @classmethod
    def getMotionStateFromCloudService(cls):
        param = {
            "clfType": ["SS", "VH"],
            "rawData": [
                {"status": "Driving", "timestamp": 5857542057676, "values": [7.8529816, 7.1790137, 4.2999864], "sensorName": "acc", "accuracy": 0},
                {"status": "Driving", "timestamp": 5857741983426, "values": [7.8529816, 7.1790137, 4.2999864], "sensorName": "acc", "accuracy": 0}
            ]
        }
        print json.dumps(param)
        print ServiceAPI.get_motion_state_api
        return requests.post(
            ServiceAPI.get_motion_state_api,
            data=json.dumps(param),
            headers=cls.headers()
        )

if __name__ == "__main__":

    m = ServiceAPI()
    print m.getMotionStateFromCloudService().content