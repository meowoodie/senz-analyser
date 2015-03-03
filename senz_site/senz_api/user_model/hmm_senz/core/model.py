from __future__ import division
from behavior import Behavior
# import senz_api.user_model.hmm_senz.core.behavior as behavior

__author__ = 'woodie'

# Hidden state set
DEFAULT_HIDDEN_STATE = ("WORK", "LIVE", "RELAX", "ENTERTAIN", "EXERCISE")
# Visible output set
DEFAULT_LOCATION     = (
    "PUBLIC_PLACE",
    "COMMUNITY",
    "OFFICE",
    "ON_THE_WAY",
    "SCHOOL",
    "HOSPITAL",
    "MALL",
    "RESTAURANT",
    "SCENIC",
    "SERVICE",
    "OTHER"
)
# - Motion   = ("SITTING", "WALKING", "RUNNING", "RIDING", "DRIVING")
DEFAULT_MOTION       = ("SITTING", "DRIVING", "RIDING", "WALKING", "RUNNING")
# - Sound    = ("")
DEFAULT_SOUND        = ()

# The class of senz model
class SenzModel:

    def __init__(self,
                 hidden_state = DEFAULT_HIDDEN_STATE,  # The Hidden State Set
                 location = DEFAULT_LOCATION, motion = DEFAULT_MOTION, sound = DEFAULT_SOUND): # The Visible Output Set
        # - It is location evidence
        self.mDefaultLocation = location
        # - It is motion evidence
        self.mDefaultMotion = motion
        # - It is sound evidence
        self.mDefaultSound = sound
        # - It's visible output set
        #   It is made up of element above-mentioned
        self.mDefaultVisibleOutputSet = self.createDefaultVisibleBehaviorSet()

        # - It's hidden state set
        self.mDefaultHiddenStateSet = hidden_state

        # - Condition Motion Matrix
        self.mMotionConditionMatrix = self.createDefaultConditionMatrix(self.mDefaultMotion)
        # - Condition Location Matrix
        self.mLocationConditionMatrix = self.createDefaultConditionMatrix(self.mDefaultLocation)
        # - Condition Location Matrix
        # self.mSoundConditionMatrix = self.createDefaultConditionMatrix(self.mDefaultSound)

        # - It's the prior probability of hidden states
        self.mDefaultPi = self.createDefaultPi()
        # - Transition Matrix
        self.mDefaultTransitionMatrix = self.createDefaultTransitionMatrix()
        # - Emission Matrix
        self.mDefaultEmissionMatrix = self.createDefaultEmissionMatrix()


    # Public Method.

    def setPi(self, pi):
        '''
        SET PI

        :param pi:
            It's a dict, the key is state name, the value is the probability.
            eg. pi = {"WORK": 0.6, "LIVE": 0.1, "RELAX": 0.05, "ENTERTAIN": 0.2, "EXERCISE": 0.05}
        :return:
        '''
        self.mDefaultPi = pi

    def setTransitionP(self, transition_p):
        '''
        SET TRANSITION P

        :param transition_p:
            It's a two-dimension dict, the first and second level key is state name, the value the probability.
            eg. transition_p = {STATE1 : {STATE1 : p1, STATE2 : p2, ...}, ...}
        :return:
        '''
        self.mDefaultTransitionMatrix = transition_p

    def setEmissionP(self, emission_p):
        '''
        SET EMISSION P

        :param emission_p:
            It's a dict, the key is state name, the value is an array of emission probability.
            eg. emission_p = {STATE1: [p1, p2, p3, ...], ...}
        :return:
        '''
        for state in self.mDefaultHiddenStateSet:
            output_index = 0
            for output in self.mDefaultVisibleOutputSet:
                self.mDefaultEmissionMatrix[state][output] = emission_p[state][output_index]
                output_index += 1

    def setMotionConditionP(self, motion_p):
        '''
        SET MOTION CONDITION P

        :param motion_p:
        :return:
        '''
        self.mMotionConditionMatrix = motion_p
        # Re-compute emission matrix
        self.mDefaultEmissionMatrix = self.createDefaultEmissionMatrix()

    def setLocationConditionP(self, location_p):
        '''
        SET LOCATION CONDITION P

        :param location_p:
        :return:
        '''
        self.mLocationConditionMatrix = location_p
        # Re-compute emission matrix
        self.mDefaultEmissionMatrix = self.createDefaultEmissionMatrix()

    # def setSoundConditionP(self, sound_p):
    #     self.mSoundConditionMatrix = sound_p
    #     # Re-compute emission matrix
    #     self.mDefaultEmissionMatrix = self.createDefaultEmissionMatrix()

    # Private Method.

    # The construction of Condition Matrix
    # - Motion Condition Matrix
    def createDefaultConditionMatrix(self, condition):
        size       = len(condition) # The count of condition
        value      = 1/size
        # the return value
        # condition_matrix = {}
        # for c in condition:
        #     condition_matrix[c] = {}
        #     for state in self.mDefaultHiddenStateSet:
        #         condition_matrix[c][state] = value
        # return condition_matrix
        condition_matrix = {}
        for state in self.mDefaultHiddenStateSet:
            condition_matrix[state] = {}
            for c in condition:
                condition_matrix[state][c] = value
        return condition_matrix

    def createDefaultPi(self):
        pi    = {}
        size  = len(self.mDefaultHiddenStateSet)
        value = 1/size
        for state in self.mDefaultHiddenStateSet:
            pi[state] = value
        return pi

    def createDefaultTransitionMatrix(self):
        transition = {}
        size       = len(self.mDefaultHiddenStateSet)
        value      = 1/size
        for state_i in self.mDefaultHiddenStateSet:
            transition[state_i] = {}
            for state_j in self.mDefaultHiddenStateSet:
                transition[state_i][state_j] = value
        return transition

    def createDefaultEmissionMatrix(self):
        emission = {}
        # row      = len(self.mDefaultHiddenStateSet)
        # col      = len(self.mDefaultVisibleOutputSet)
        for state in self.mDefaultHiddenStateSet:
            emission[state] = {}
            for output in self.mDefaultVisibleOutputSet:
                product = 1
                for evidence_name in output.getEvidenceName():
                    evidence = output.getEvidences()
                    # print evidence, evidence_name
                    if evidence_name == "motion":
                        product *= self.mMotionConditionMatrix[state][evidence[evidence_name]]
                    elif evidence_name == "location":
                        product *= self.mLocationConditionMatrix[state][evidence[evidence_name]]
                    # elif evidence_name == "sound":
                    #     product *= self.mSoundConditionMatrix[state][evidence[evidence_name]]
                    # print evidence_name,
                emission[state][output] = product
        return emission

    def createDefaultVisibleBehaviorSet(self):
        '''
        CREATE VISIBLE BEHAVIOR SET

        This func will create a set of visible output for HMM.

        :return: behav(list of obj)
        '''
        # According to these sets, we instantiate a list of behavior obj.
        behav = []
        i = 0
        # for t in self.mDefaultTime:
        for l in self.mDefaultLocation:
            for m in self.mDefaultMotion:
                # for s in self.mDefaultSound
                behav.append(Behavior(motion = m,
                                      location = l
                                      # no = i,
                                      # sound = s
                ))
                i += 1
        return behav

