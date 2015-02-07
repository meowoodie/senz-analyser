from lean_obj import AVObject
import json
import datetime
import requests
import settings

import warnings
warnings.filterwarnings("ignore")

class UserMotion(AVObject):

    DEFAULT_STATE   = 'SITTING'
    DEFAULT_RAWDATA = {}

    def __init__(self, user_id=None):
        super(UserMotion, self).__init__()
        self.rawData = self.DEFAULT_RAWDATA
        self.state   = self.DEFAULT_MOTION
        self.userId  = user_id

        if user_id is not None:
            # Get the latest motion rawdata.
            result = self.get(self.userId)
            # Decode result as dict.

            # Store the motion rawData in private member.

    def getState(self):
        pass

    def saveState(self):
        pass



class UserSound(AVObject):

    DEFAULT_SCENCE  = 'INSIDE'
    DEFAULT_RAWDATA = {}

    def __init__(self, user_id=None):
        super(UserSound, self).__init__()
        self.rawData = self.DEFAULT_RAWDATA
        self.scence  = self.DEFAULT_SCENCE
        self.userId  = user_id

        if user_id is not None:
            result = self.get(self.userId)

    def getScence(self):
        pass

    def saveScence(self):
        pass



class UserPOI(AVObject):

    def __init__(self):
        super(UserPOI, self).__init__()

class UserSenz(AVObject):

    def __init__(self):
        super(UserSenz, self).__init__()



class LeanManager(object):

    def __init__(self):
        pass

    # Get users' motion rawdata
    # - Send: userId
    # - Receive: motion(rawdata)
    def getMotionRawdata(self):

        pass

    # Get users' poi GPS and iBeacon info
    # - Send: userId
    # - Receive: poi(GPS & iBeacon)
    def getPOINativeInfo(self):
        pass

    # Get users' sound rawdata
    # - Send: userId
    # - Receive: sound(rawdata)
    def getSoundRawdata(self):
        pass

    # Store users' current visible output, which compute by analyser, into leancloud
    def setVisibleOutput(self):
        pass

    # Store users' current senz, which compute by analyser, into leancloud
    def setSenz(self):
        pass








        # def saveData(self, className, dataDict):
        #         res = LeanObject._save_to_avos(className,dataDict)
        #         if 'createdAt' not in json.loads(res.content):
        #                 print res.content
        #         else:
        #                 return res.content
        #
        # #By Zhong.zy, Create users
        # def createUser(self,userInfo):
        #         res = requests.post(
        #             url = LeanObject.Users,
        #             headers = LeanObject.headers(),
        #             data = json.dumps(userInfo),
        #             verify=False)
        #         if 'createdAt' not in json.loads(res.content):
        #             print 'Error: '+res.content
        #         else:
        #             print 'Create user success!\n'+res.content
        #
        # #By Zhong.zy, Get user Id by username
        # def getUserIdByName(self,username):
        #         with_params = {
        #             'keys':'objectId',
        #             'where':'{"username":"%s"}'%username
        #             }
        #         res = requests.get(
        #             url = LeanObject.Users,
        #             headers=LeanObject.headers(),
        #             params=with_params,
        #             verify=False
        #         )
        #         if not res.ok:
        #                 print 'Error'+res.content
        #                 return
        #         results = json.loads(res.content)['results']
        #         if results:
        #                 return results[0]['objectId']
        #
        #
        # #By Zhong.zy, Get info by specified opt
        # def getData(self,className,**kwargs):
        #         res = requests.get(
        #             LeanObject.base_classes+className,
        #             headers=LeanObject.headers(),
        #             params=kwargs,
        #             verify=False
        #         )
        #         if 'error' not in json.loads(res.content):
        #                 return res.content
        #         else:
        #             print res.content
        #
        # #By Zhong.zy, Save activity in a same interface
        # def saveActivity(self,dataDict):
        #         self.saveData('activities',dataDict)
        #
        # #By Zhong.zy, Get id in order to update data
        # def getIdByCondition(self,className,**kwargs):
        #         cond = json.dumps(kwargs)
        #         res = self.getData(className,keys='objectId',where=cond)
        #         if res:
        #                 results = json.loads(res)['results']
        #                 if results:
        #                         return results[0]['objectId']
        #
        # #By Zhong.zy, Get field in terms of some condition
        # def getFieldByCondition(self,className,field,**kwargs):
        #         cond = json.dumps(kwargs)
        #         res = self.getData(className,keys=field,where=cond)
        #         if res:
        #                 results = json.loads(res)['results']
        #                 if results:
        #                         return results[0][field]
        #
        # #By Zhong.zy, Get id in order to update data
        # def getIdByName(self,className,objName):
        #         return self.getIdByCondition(className,name=objName)
        #
        # #By Zhong.zy, insert or update
        # def updateDataByName(self,className,objName,dataDict):
        #         objectId =  self.getIdByName(className,objName)
        #         if objectId:
        #                 res = LeanObject._update_avos(className,str(objectId),dataDict)
        #                 if 'error' not in json.loads(res.content):
        #                         return res.content
        #                 else:
        #                         print 'Update Error:'+json.loads(res.content)['error']
        #                         print 'From: '+className+objName
        #         else:
        #                 self.saveData(className,dataDict)
        #
        # #By Zhong.zy, delete, param data is id or id list
        # def deleteData(self,className,data):
        #         res = LeanObject._remove_avos(className,data)
        #         if 'error' in json.loads(res.content):
        #             print res.content




# if __name__ == "__main__":
#         avosManager = AvosManager()
#         start = "2013-05-05 20:30:45"
#         date_utc = getUtcDate(start)
#         start_utc = timeConvet2utc(start)
#
#
#
#         start_iso = start_utc.replace(" ","T")+".000Z"
#         date_iso = date_utc.replace(" ","T")+".000Z"
#         date_time = dict(__type='Date',iso=date_iso)
#         start_time = dict(__type='Date',iso=start_iso)
#         end_time = dict(__type='Date',iso=start_iso)
#         dataDict = {"name":"《文成公主》大型实景剧","date":date_time,
#         "start_time":start_time,"end_time":end_time,"ticket":"220","region":"北京市海淀区北京邮电大学","location":gps2GeoPoint(39.970513,116.361834),"category":""}
#         className = "testDate"
#         #avosManager.saveData(className,dataDict)
#         #avosManager.saveActivity(dataDict)
#         #avosManager.updateDataByName('activities','《文成公主》大型实景剧',dict(ticket='200'))
#         print avosManager.getIdByCondition(className,name='《文成公主》大型实景剧')
#         '''
#         AvosClass.app_settings = [settings.avos_app_id, settings.avos_app_key]
#         res = AvosClass.save(dataDict)
#         if 'createdAt' in json.loads(res.content):
#                 print '\nSucceeded in creating test object in AvosClass!\n'
#         else:
#                 print res.content
#         '''
