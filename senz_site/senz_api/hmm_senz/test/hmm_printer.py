__author__ = 'woodie'

import senz_api.hmm_senz.hmm.hmm as hmm

pi = {"WINDY" : 0.333, "SUNNY" : 0.333, "RAINNY" : 0.333}
visible_output  = ("HOT","COLD")
hidden_state    = ("WINDY","SUNNY","RAINNY")
transition_init = {'WINDY': {'WINDY': 0.333, 'SUNNY': 0.333, 'RAINNY': 0.333},
                   'SUNNY': {'WINDY': 0.333, 'SUNNY': 0.333, 'RAINNY': 0.333},
                   'RAINNY': {'WINDY': 0.333, 'SUNNY': 0.333, 'RAINNY': 0.333}}
emission_init   = {'WINDY': {'HOT': 0.5, 'COLD': 0.5},
                   'SUNNY': {'HOT': 0.75, 'COLD': 0.25},
                   'RAINNY': {'HOT': 0.25, 'COLD': 0.75}}

HMM = hmm.HMM(
    visible_output,
    hidden_state,
    pi,
    transition_init,
    emission_init
)

HMM.initTrainSample(["HOT", "HOT", "HOT", "HOT", "COLD", "HOT", "COLD", "COLD", "COLD", "COLD"])

HMM.BaumWelchLearn(0.01)

print "transition matrix:"
print HMM.hTransitionP
print "emission matrix:"
print HMM.hEmissionP

HMM.ViterbiDecode()

print HMM.hQ
