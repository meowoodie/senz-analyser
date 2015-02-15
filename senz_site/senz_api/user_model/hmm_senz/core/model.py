from __future__ import division
from behavior import Behavior
import senz_api.user_model.hmm_senz.core.behavior as behavior

__author__ = 'woodie'

# Hidden state set
DEFAULT_HIDDEN_STATE = ("WORK", "LIVE", "RELAX", "ENTERTAIN", "EXERCISE")
# Visible output set

# - Location = ("ENTERTAINMENT", "COMMUNITY", "GOVERNMENT", "CATERING", "EDUCATION",
#               "TRAFFIC", "FINANCE", "TRAVEL", "HOTEL", "COMPANY",
#               "SHOPPING", "MEDICAL", "BUSINESS")
DEFAULT_LOCATION     = ("EDUCATION", "SHOPPING", "COMMUNITY")
# - Motion   = ("SITTING", "WALKING", "RUNNING", "RIDING", "DRIVING")
DEFAULT_MOTION       = ("SITTING", "WALKING", "RUNNING")
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


    def setPi(self, pi):
        self.mDefaultPi = pi

    def setTransitionP(self, transition_p):
        self.mDefaultTransitionMatrix = transition_p

    def setMotionConditionP(self, motion_p):
        self.mMotionConditionMatrix = motion_p
        # Re-compute emission matrix
        self.mDefaultEmissionMatrix = self.createDefaultEmissionMatrix()

    def setLocationConditionP(self, location_p):
        self.mLocationConditionMatrix = location_p
        # Re-compute emission matrix
        self.mDefaultEmissionMatrix = self.createDefaultEmissionMatrix()

    # def setSoundConditionP(self, sound_p):
    #     self.mSoundConditionMatrix = sound_p
    #     # Re-compute emission matrix
    #     self.mDefaultEmissionMatrix = self.createDefaultEmissionMatrix()

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

