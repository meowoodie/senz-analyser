__author__ = 'woodie'

# import hmm_senz.core.behavior as behavior
# import senz_api.hmm_senz.hmm.hmm as hmm
# import senz_api.hmm_senz.core.model as model
from ..hmm.hmm import HMM
from model import SenzModel


class Senz(HMM):
    '''
    SENZ


    '''
    # Override base func
    def __init__(self, model=SenzModel()):
        # the senz model
        self.model = model
        # senz's hidden state for hmm
        self.hidden_state = model.mDefaultHiddenStateSet
        # senz's visible output for hmm
        self.visible_output_obj = model.mDefaultVisibleOutputSet
        # Set a default value for hmm
        # self.initHMMParam(model.mDefaultPi,
        #                   model.mDefaultTransitionMatrix,
        #                   model.mDefaultEmissionMatrix)
        HMM.__init__(self,
                     self.visible_output_obj,
                     self.hidden_state,
                     model.mDefaultPi,
                     model.mDefaultTransitionMatrix,
                     model.mDefaultEmissionMatrix)

    # Override base func
    def initTrainSample(self, output): # The Senz's visible output
        '''
        INIT TRAIN SAMPLE



        :param output:
        :return:
        '''
        # Transfer train sample from dict to obj
        output_obj = []
        for o in output:
            # For every element in output,
            # which is same with in visible_output_obj
            output_obj.append(self.outputDictToObj(o))
        # init train sample
        HMM.initTrainSample(self, output_obj)

    # def initHMMParam(self, pi_init, transition_init, emission_init):
    #     '''
    #     INIT HMM PARAM
    #
    #
    #
    #     :param pi_init:
    #     :param transition_init:
    #     :param emission_init:
    #     :return:
    #     '''
    #     # Transfer matrix to dict
    #     transition = self.matrixToDict(transition_init, self.hidden_state, self.hidden_state)
    #     # emission   = self.matrixToDict(emission_init, self.hidden_state, self.visible_output_obj)
    #     pi         = self.matrixToDict(pi_init, 0, self.hidden_state)
    #     # Invoke base class
    #     hmm.HMM.__init__(self, self.visible_output_obj, self.hidden_state, pi, transition, emission_init)

    def outputDictToObj(self, output_dict):
        '''
        OUTPUT DICT TO OBJ



        :param output_dict:
        :return:
        '''
        for b in self.visible_output_obj:
            if output_dict == b.getEvidences():
                return b

    def matrixToDict(self, matrix, row, col):
        '''
        MATRIX TO DICT

        The method helps __init__ func transfer param (transition, emission, pi) from
        num matrix to dict. the dict data structure is good at data processing.

        :param matrix: It is the matrix that need to be transfered to dict
        :param row: the list of matrix's row
        :param col: the list of matrix's col
        :return: the dict which is transfered from matrix
        '''
        dict = {}
        i = 0 # index of row/col of matrix
        # If matrix has no row
        if row == 0:
            for c in col:
                dict[c] = matrix[i]
                i += 1
            return dict
        # Else if matrix is two-dimension
        for r in row:
            j = 0 # index of col of matrix
            dict[r] = {}
            for c in col:
                dict[r][c] = matrix[i][j]
                j += 1
            i += 1
        return dict
