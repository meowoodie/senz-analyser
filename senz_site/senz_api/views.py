import json
from django.http.response import HttpResponse
from data_handler import DataHandler

def Senz(request):

    if request.method == 'POST':
        body = json.loads(request.body)  #body is deprecated
    else:
        return HttpResponse("Error!")

    user_mac     = body["userMac"]
    motion_count = body["motionCount"]
    sound_count  = body["soundCount"]
    poi_count    = body["poiCount"]
    during_time  = body["duringTime"]

    dh = DataHandler(user_mac, during_time=during_time)
    senz_list = dh.getUserSenz(motion_count, poi_count, sound_count)

    return HttpResponse(senz_list[0])