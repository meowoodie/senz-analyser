__author__ = 'woodie'


class Behavior:
    '''
    Class: BEHAVIOR

    It's a class to represent an user's behavior at some time.
    '''
    def __init__(self, **evidences):
        # The evidences
        self.bEvidences = evidences # It's a dict
        # The count of evidences
        self.bEviNum    = len(self.bEvidences)
        # The name of every evidence
        self.bEviName   = []
        for evi_name in self.bEvidences.keys():
            self.bEviName.append(evi_name)
        # The lable of the behavior
        self.bLable  = ""
        for lable in self.bEviName:
            self.bLable += lable + " "

    def getEvidenceName(self):
        return self.bEviName

    def getEvidenceCont(self, evi_name):
        return self.bEvidences[evi_name]

    def getEvidences(self):
        return self.bEvidences

    def getBehaviorLable(self):
        return self.bLable


