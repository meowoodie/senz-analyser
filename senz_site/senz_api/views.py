import json
from django.http.response import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from data_handler import DataHandler
from django.http import JsonResponse

def errorInfo():
    import sys
    info = "%s || %s" % (sys.exc_info()[0], sys.exc_info()[1])  # todo log the exception info
    print info
    return info

def errorResponses(error=None):
    if not error:
        info = errorInfo()
    else:
        info = error

    return JsonResponse({"status": 0}, {"errors": info})


def successResponses(results):

    return JsonResponse({"status": 1, "results": results})

@csrf_exempt
def Senz(request):

    if request.method == 'POST':
        body = json.loads(request.body)  #body is deprecated
    else:
        return errorResponses("Error!")

    user_mac     = body["userMac"]
    motion_count = body["motionCount"]
    sound_count  = body["soundCount"]
    poi_count    = body["poiCount"]
    during_time  = body["duringTime"]

    dh = DataHandler(user_mac, during_time=during_time)
    senz_list = dh.getUserSenz(motion_count, poi_count, sound_count)

    return successResponses(senz_list[0])