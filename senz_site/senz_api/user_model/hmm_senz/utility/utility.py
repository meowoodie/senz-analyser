__author__ = 'woodie'

# the utility method



# the utility class for printing senz info

class Utility:

    def __init__(self, senz):
        self.senz = senz

    def printOver(self):
        print "\n"

    # need type check!
    def printEmissionMatrix(self):
        matrix = self.senz.getEmission()
        print "   ---- HMM's Emission Matrix ----"
        for state in matrix:
            print "   * [", state, "] ->"
            for output in matrix[state]:
                print "    ", output.getEvidences(), "=", matrix[state][output]
        self.printOver()

    def printTransitionMatrix(self):
        matrix = self.senz.getTransition()
        print "   ---- HMM's Transition Matrix ----"
        for state_i in matrix:
            print "   * [", state_i, "] -> {",
            for state_j in matrix[state_i]:
                print "[", state_j, "] =", matrix[state_i][state_j],
            print "}"
        self.printOver()

    def printHiddenState(self):
        tuple = self.senz.getHiddenState()
        print "   ---- HMM's Hidden State Tuple ----"
        print "  ",
        for state in tuple:
            print "[", state, "]",
        self.printOver()

    def printVisibleOutput(self):
        list = self.senz.getVisibleOutput()
        print "   ---- HMM's Visible Output List ----"
        for output in list:
            print "   *", output.getEvidences()
        self.printOver()

