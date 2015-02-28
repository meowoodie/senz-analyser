__author__ = 'woodie'

# import senz_api.hmm_senz.utility.decorator as decorator
# import senz_api.hmm_senz.utility.exception as exception

class HMM:
    '''Base Class : HMM

    The base class is used to solve the basic HMM problem.
    '''

    #@decorator.SenzDecorator.funcLogger
    def __init__(self,
                 visible_output,  # All kinds of visible outputs, it's a tuple, eg. ("wet", "dry")
                 hidden_state,    # All kinds of hidden states, it's a tuple, eg. ("sunny", "windy", "cloudy", "rainny")
                 pi,              # The initial probability of every states when started
                 transition_init, # The Matrix of hidden states' transition probability
                 emission_init): # The Matrix of visible outputs' emission probability
        self.hVisibleOutput = visible_output
        self.hHiddenState   = hidden_state
        self.hSizeHmm       = {
            'visible output' : len(self.hVisibleOutput),
            'hidden state'   : len(self.hHiddenState)
        }

        # The initial of hTransitionP
        # - It's a 2-dimension dict
        # - { key1 : { key2 : value } }
        # - key1 is hidden states' name
        # - key2 is hidden states' name
        # - value is the transition probability from key1 to key2
        self.hTransitionP = transition_init
        # self.hTransitionP = self.matrixToDict(transition_init, self.hHiddenState, self.hHiddenState)
        # The initial of hEmissionP
        # - It's a 2-dimension dict
        # - { key1 : { key2 : value } }
        # - key1 is hidden states' name
        # - key2 is visible outputs' name
        # - value is the transition probability from key1 to key2
        self.hEmissionP   = emission_init
        # self.hEmissionP   = self.matrixToDict(emission_init, self.hHiddenState, self.hVisibleOutput)
        # The initial probablility of every hidden state
        # - eg. pi = {"sunny" : 0.2, "windy" : 0.3, "cloudy" : 0.1, "rainny" : 0.4}
        self.hPi          = pi
        # self.hPi          = self.matrixToDict(pi, 0, self.hHiddenState)

        # The HMM's timestamp, default is 0
        self.hT       = 0
        # The HMM's visible output
        self.hOutput  = []
        # The probability of evety output
        self.hOutputP = []

        # forward variable
        # - t = 1 : alpha[1][Si] = pi[Si] * emission[Si][O1]
        # - other : alpha[t][Si] = emission[Si][Ot] * sum(N,j=1)(alpha(t-1)(Sj) * transition[Sj][Si])
        self.hAlpha  = []
        # backward variable
        self.hBeta   = []
        # Be at Si when t
        self.hGamma  = []
        # Be at Si when t and at Sj when t+1
        self.hXi     = []
        # Partial Probability
        self.hDelta  = []
        # The Viterbi Path
        self.hPsi    = []
        # Hidden state seq of Prediction
        self.hQ      = []

    #@decorator.SenzDecorator.funcLogger
    def initTrainSample(self, output): # The HMM's visible output
        '''
        GIVE INITIAL TRAINNING SAMPLE

        If you have complete trainning sample,
        you can call this function to give your sample to HMM.
        Meanwhile, HMM will set HMM's timestamp according to the size of your sample.
        And init the related variable.

        :param output: The HMM's visible output
        :return: None
        '''

        self.hT = len(output)
        self.hOutput = output
        # Init hOutputP by hT
        for t in range(0, self.hT):
            self.hOutputP.append(0)
        # Init hAlpha by hT
        for t in range(0, self.hT):
            alpha_t = {}
            for state in self.hHiddenState:
                alpha_t[state] = 0
            self.hAlpha.append(alpha_t)
        # Init hBeta by hT
        for t in range(0, self.hT):
            beta_t = {}
            for state in self.hHiddenState:
                beta_t[state] = 0
            self.hBeta.append(beta_t)
        # Init hGamma by hT
        for t in range(0, self.hT):
            gamma_t = {}
            for state in self.hHiddenState:
                gamma_t[state] = 0
            self.hGamma.append(gamma_t)
        # Init hXi by hT
        for t in range(0, self.hT):
            xi_t = {}
            for state_i in self.hHiddenState:
                xi_t[state_i] = {}
                for state_j in self.hHiddenState:
                    xi_t[state_i][state_j] = 0
            self.hXi.append(xi_t)
        # Init hDelta by hT
        for t in range(0, self.hT):
            delta_t = {}
            for state in self.hHiddenState:
                delta_t[state] = 0
            self.hDelta.append(delta_t)
        # Init hPsi by hT
        for t in range(0, self.hT):
            psi_t = {}
            for state in self.hHiddenState:
                psi_t[state] = 0
            self.hPsi.append(psi_t)
        # Init Hidden state seq of Prediction by hT
        for t in range(0, self.hT):
            self.hQ.append(self.hHiddenState[0])
        # ---INTERESTING PROBLEM---
        # If I write like this:
        #  1 alpha_t = {}
        #  2 for state in self.hHiddenState:
        #  3     alpha_t[state] = 0
        #  4 for t in range(0, self.hT):
        #  5    self.hAlpha.append(alpha_t)
        # all member of self.hAlpha will stay the same with each other all the time,
        # because they are the same object named alpha_t

    #@decorator.SenzDecorator.funcLogger
    def forward(self):
        '''
        FORWARD

        It used to excute forward algorithm.
        It will calculate HMM's forward variable(alpha).
        And store in HMM.hAlpha.

        :return: max_delta(float)
        '''
        # Initialization:
        # - Calculate the every hidden state's alpha(forward variable) at t=1
        max_delta = 0 # the maximum of delta in alpha variable's elements
        for state in self.hHiddenState:
            self.hAlpha[0][state] = self.hPi[state] * self.hEmissionP[state][self.hOutput[0]]
            #print "alpha t=", 0, " state=", state, "val=", self.hAlpha[0][state]
        # Induction:
        # - Compute all alpha at every t
        for t in range(0, self.hT - 1):
            for state_j in self.hHiddenState:
                sum = 0
                for state_i in self.hHiddenState:
                    sum += self.hAlpha[t][state_i] * self.hTransitionP[state_i][state_j]
                new_alpha = sum * self.hEmissionP[state_j][self.hOutput[t+1]] # The new alpha variable value
                delta = abs(new_alpha - self.hAlpha[t+1][state_j])
                self.hAlpha[t+1][state_j] = new_alpha
                if delta >= max_delta:
                    max_delta = delta
                #print "alpha t=", t+1, " state=", state_j, "val=", self.hAlpha[t+1][state_j]
        return max_delta

    #@decorator.SenzDecorator.funcLogger
    def backward(self):
        '''
        BACKWARD

        It used to excute backward algorithm.
        It will calculate HMM's backward variable(beta).
        And store in HMM.hBeta.

        :return: max_delta(float)
        '''
        max_delta = 0
        # Initialization:
        for state in self.hHiddenState:
            self.hBeta[self.hT - 1][state] = 1.0
        # Induction:
        for t in range(self.hT - 2, -1, -1): # count from T-1 to 0
            for state_i in self.hHiddenState:
                sum = 0
                for state_j in self.hHiddenState:
                    sum += self.hTransitionP[state_i][state_j] * \
                           self.hEmissionP[state_j][self.hOutput[t+1]] * \
                           self.hBeta[t+1][state_j]
                new_beta = sum # The new beta variable value
                delta = abs(new_beta - self.hBeta[t][state_i])
                self.hBeta[t][state_i] = new_beta
                if delta >= max_delta:
                    max_delta = delta
        return max_delta

    #@decorator.SenzDecorator.funcLogger
    def computeGamma(self):
        '''
        COMPUTE GAMMA

        - gamma = (alpha[t][i]*beta[t][i])/sum(N,i=1)(alpha[t][i]*beta[t][i])
        - sum(N,i=1)(alpha[t][i]*beta[t][i]) = 1
        This func will compute the HMM's gamma variable with
        exist alpha variable and beta variable.

        :return: None
        '''
        for t in range(0, self.hT):
            denominator = 0
            for state in self.hHiddenState:
                denominator += (self.hAlpha[t][state] * self.hBeta[t][state])
            for state in self.hHiddenState:
                numerator = self.hAlpha[t][state] * self.hBeta[t][state]
                self.hGamma[t][state] = numerator / denominator

    #@decorator.SenzDecorator.funcLogger
    def computeXi(self):
        '''
        COMPUTE XI

        - xi = (alpha[t][i]*a[i][j]*b[j][O[t+1]]*beta[t][i])/sum(N,i=1){sum(N,j=1)(alpha[t][i]*a[i][j]*b[j][O[t+1]]*beta[t][i])}
        - sum(N,i=1)(alpha[t][i]*a[i][j]*b[j][O[t+1]]*beta[t][i]) = gamma[t][i]
        This func will compute the HMM's xi variable with
        exist alpha variable, beta variable, transition matrix and emission matrix.

        :return: None
        '''
        for t in range(0, self.hT - 1):
            denominator = 0
            for state_i in self.hHiddenState:
                for state_j in self.hHiddenState:
                    denominator += self.hAlpha[t][state_i] * \
                                   self.hTransitionP[state_i][state_j] * \
                                   self.hEmissionP[state_j][self.hOutput[t+1]] * \
                                   self.hBeta[t+1][state_j]
            for state_i in self.hHiddenState:
                for state_j in self.hHiddenState:
                    numerator = self.hAlpha[t][state_i] * \
                                self.hTransitionP[state_i][state_j] * \
                                self.hEmissionP[state_j][self.hOutput[t+1]] * \
                                self.hBeta[t+1][state_j]
                    self.hXi[t][state_i][state_j] = numerator / denominator

    #@decorator.SenzDecorator.funcLogger
    def reestimateHMM(self, freq):
        '''
        REESTIMATE HMM

        It's used to reestimate the param of HMM with the visible output result.
        We recommonded that the freq should not be too small.
        The bigger freq is, the slower HMM will be reestimated

        :param freq: the frequency of the reestimate, (0,1] is allowed.
                     the value is bigger, the speed of changing is faster.
        :return: None
        '''
        # Reestimate frequency of state i in time = 1
        for state in self.hHiddenState:
            self.hPi[state] = (1 - freq) + freq * self.hGamma[0][state]
        # Reestimate transition matrix and emission matrix in each state
        for state_i in self.hHiddenState:

            # Calculate the expect of transition matrix (A)
            # - Denominator of A
            denominatorA = 0
            for t in range(0, self.hT - 1):
                denominatorA += self.hGamma[t][state_i]
            for state_j in self.hHiddenState:
                # - Numerator of A
                numeratorA = 0
                for t in range(0, self.hT - 1):
                    numeratorA += self.hXi[t][state_i][state_j]
                    self.hTransitionP[state_i][state_j] = (1 - freq) + freq * (numeratorA / denominatorA)

            # Calculate the expect of emission matrix (B)
            # - Denominator of B
            denominatorB = denominatorA + self.hGamma[self.hT - 1][state_i]
            for output in self.hVisibleOutput:
                # - Numerator of B
                numeratorB = 0
                for t in range(0, self.hT):
                    if self.hOutput[t] == output:
                        numeratorB += self.hGamma[t][state_i]
                self.hEmissionP[state_i][output] = (1 - freq) + freq * (numeratorB / denominatorB)

    #@decorator.SenzDecorator.funcLogger
    def BaumWelchLearn(self, delta):
        '''
        BAUM WELCH ALGORITHM

        The Baum Welch algorithm uses the well-known EM algorithm to find the maximum likelihood
        estimate of the parameters of a hidden Markov model given a set of observed feature vectors
        It contains the following steps:
        - Compute forward, backward variable
        - Compute Gamma, Xi variable
        - Check delta
        - repeat untill the delta less then the threshold

        :param delta(float) the threshold
        :return: None
        '''
        count = 0 # It's a counter
        while count < 99:
            delta_alpha = self.forward()
            delta_beta  = self.backward()
            self.computeGamma()
            self.computeXi()
            # Get the maximum of delta
            if delta_alpha >= delta_beta:
                max_delta = delta_alpha
            else:
                max_delta = delta_beta
            print count, ". delta =", max_delta, "( Alpha =", delta_alpha, ", beta =", delta_beta, ")"
            self.reestimateHMM(0.999)
            count += 1
            # Condition of Loop
            if max_delta <= delta:
                print "Baum Welch Algorithm runs", count, "loops"
                break
        else:
            # Here throw senz exception
            # - no partial best solution.
            print "ERROR"

    #@decorator.SenzDecorator.funcLogger
    def estimateValue(self):
        '''
        ESTIMATE VALUE

        It used to estimate the probability of current output.
        Before invoke this func, you should have calculated forward variable.
        You can call forward or forwardByStep to calculate forward variable.

        :return:  estimate_p(float)  the probability of current output
        '''
        # Forward:
        # - Calculate the HMM's forward variable(alpha).
        #self.forward()

        # Termination:
        # - The probability of output at t = sum of every state's probability at t (that is alpha[t][state])
        estimate_p = 0.0
        for state in self.hHiddenState:
            estimate_p += self.hAlpha[self.hT - 1][state]
        return estimate_p

    #@decorator.SenzDecorator.funcLogger
    def ViterbiDecode(self):
        '''
        VITERBI DECODE

        It's a dynamic programming algorithm for finding the most likely sequence of hidden states,
        called Viterbi path, that result in a sequence of observed events, especially in the context
        of Markov information sources and hidden Markov models.
        The result will be stored in Q variable.

        :return: None
        '''
        # Initialization
        for state in self.hHiddenState:
            self.hDelta[0][state] = self.hPi[state] * self.hEmissionP[state][self.hOutput[0]]
            self.hPsi[0][state] = self.hHiddenState[0]

        # Recursion
        for t in range(1, self.hT):
            for state_j in self.hHiddenState:
                maxval = 0
                maxvalind = self.hHiddenState[0]
                for state_i in self.hHiddenState:
                    val = self.hDelta[t-1][state_i] * self.hTransitionP[state_i][state_j]
                    if val > maxval:
                        maxval    = val
                        maxvalind = state_i
                self.hPsi[t][state_j]   = maxvalind
                self.hDelta[t][state_j] = maxval * self.hEmissionP[state_j][self.hOutput[t]]

        # Termination
        prob = 0
        # - Compute Q when t = T
        for state in self.hHiddenState:
            if self.hDelta[self.hT - 1][state] > prob:
                prob = self.hDelta[self.hT - 1][state]
                self.hQ[self.hT - 1] = state

        # Path backtracking
        for t in range(self.hT - 2, -1, -1):
            self.hQ[t] = self.hPsi[t+1][self.hQ[t+1]]

    def getHiddenState(self):
        return self.hHiddenState

    def getVisibleOutput(self):
        return self.hVisibleOutput

    def getTransition(self):
        return self.hTransitionP

    def getEmission(self):
        emission_p = {}
        for state in self.hHiddenState:
            emission_p[state] = []
            for output in self.hVisibleOutput:
                emission_p[state].append(self.hEmissionP[state][output])
        return emission_p

    def getOutputSeq(self):
        return self.hOutput

    def getPi(self):
        return self.hPi

    def getQ(self):
        return self.hQ