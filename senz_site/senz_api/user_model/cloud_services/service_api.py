import json
import settings
import requests

class ServiceAPI(object):

    get_motion_state_api = settings.protocol + settings.server_ip["Aliyun1"] + settings.get_motion_state_url
    get_sound_scence_api = settings.protocol + settings.server_ip["Aliyun1"] + settings.get_sound_scence_url
    get_poi_info_api     = settings.protocol + settings.server_ip["Aliyun1"] + settings.get_poi_info_url
    state_code_set       = settings.state_code_set
    location_code_set    = settings.location_code_set

    def __init__(self):
        pass



    # --- PRIVATE METHOD ---
    @classmethod
    def _headers(cls):
        # Since properties only work on instances, need define headers property in meta class
        return {
            "Content-Type": "application/json"
        }



    @classmethod
    def getMotionStateFromCloudService(cls,  raw_data, strategy=["SS", "VH"]):
        # Here only process 100 rawdata
        if len(raw_data) > 100:
            # Here put some code to handle the condition
            # When raw data is more than 100.
            return None
        # Init the param
        param = {
            "clfType": strategy, # The learning strategies, "SS" is recommended
            "rawData": raw_data  # The motion sample data
        }

        # The difference is String's quotation is " not ' after json.dumps
        # - print "json", json.dumps(param)
        # - print "native", param

        # Query the motion state from cloud service,
        # Then decode the result to json.
        result = json.loads(requests.post(
            ServiceAPI.get_motion_state_api,
            # ServiceAPI.debug_api,
            data=json.dumps(param),
            headers=cls._headers()
        ).content)

        # Decode the json to state
        ss_state_code = None
        vh_state_code = None
        for s in strategy:
            # Only get the first element of result,
            # Because the len of raw data is less than 100,
            # There will be only one result.
            if s is "SS":
                ss_state_code = result["predSS"][0]
            elif s is "VH":
                vh_state_code = result["predVH"][0]

        # The ss is prior.
        if ss_state_code is not None:
            return ServiceAPI.state_code_set[int(ss_state_code)]
        elif vh_state_code is not None:
            return ServiceAPI.state_code_set[int(vh_state_code)]
        else:
            return None



    @classmethod
    def getPOIInfoFromCloudService(cls, poi_info_post):
        # Init the param
        param = poi_info_post
        # Query the poi info from cloud service,
        # Then decode the result to json.
        result = json.loads(requests.post(
            ServiceAPI.get_poi_info_api,
            # ServiceAPI.debug_api,
            data=json.dumps(param),
            headers=cls._headers()
        ).content)

        if result["status"] is 1:
            # Transfer poi type to location type
            for gps in result["results"]["GPS"]:
                gps["locType"] = ServiceAPI.location_code_set[gps["poiType"]]
            for ibeacon in result["results"]["iBeacon"]:
                ibeacon["locType"] = ServiceAPI.location_code_set[ibeacon["poiType"]]
            return result["results"]
        else:
            return None








if __name__ == "__main__":

    rawdata = [
        {"status": "Driving", "timestamp": 5857542057676, "values": [7.8529816, 7.1790137, 4.2999864], "sensorName": "acc", "accuracy": 0},
        {"status": "Driving", "timestamp": 5857741983426, "values": [7.8529816, 7.1790137, 4.2999864], "sensorName": "acc", "accuracy": 0}
    ]

    m = ServiceAPI()
    print m.getMotionStateFromCloudService(rawdata)