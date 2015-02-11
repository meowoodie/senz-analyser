from lean_cloud.lean_obj import AVObject
from cloud_services.service_api import ServiceAPI
import json

class UserPOI(AVObject, ServiceAPI):

    def __init__(self):
        super(UserPOI, self).__init__()