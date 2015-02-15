__author__ = 'woodie'

import senz_api.user_model.hmm_senz.core.senz as senz
import senz_api.user_model.hmm_senz.utility.utility as utility
import senz_api.user_model.hmm_senz.core.model as model




pi = {"WORK": 0.6, "LIVE": 0.1, "RELAX": 0.05, "ENTERTAIN": 0.2, "EXERCISE": 0.05}
# motion_condition = {
#     "SITTING": {"WORK": 0.7, "LIVE": 0.1, "RELAX": 0.15, "ENTERTAIN": 0.04, "EXERCISE": 0.01},
#     "WALKING": {"WORK": 0.01, "LIVE": 0.3, "RELAX": 0.09, "ENTERTAIN": 0.59, "EXERCISE": 0.01},
#     "RUNNING": {"WORK": 0.01, "LIVE": 0.01, "RELAX": 0.01, "ENTERTAIN": 0.05, "EXERCISE": 0.92}
# }
# location_condition = {
#     "EDUCATION": {"WORK": 0.5, "LIVE": 0.3, "RELAX": 0.18, "ENTERTAIN": 0.01, "EXERCISE": 0.01},
#     "SHOPPING": {"WORK": 0.01, "LIVE": 0.01, "RELAX": 0.2, "ENTERTAIN": 0.75, "EXERCISE": 0.03},
#     "COMMUNITY": {"WORK": 0.2, "LIVE": 0.4, "RELAX": 0.15, "ENTERTAIN": 0.05, "EXERCISE": 0.2}
# }
motion_condition = {
    "WORK": {"SITTING": 0.9, "WALKING": 0.09, "RUNNING": 0.01},
    "LIVE": {"SITTING": 0.5, "WALKING": 0.45, "RUNNING": 0.05},
    "RELAX": {"SITTING": 0.85, "WALKING": 0.13, "RUNNING": 0.02},
    "ENTERTAIN": {"SITTING": 0.2, "WALKING": 0.7, "RUNNING": 0.1},
    "EXERCISE": {"SITTING": 0.05, "WALKING": 0.1, "RUNNING": 0.85}
}
location_condition = {
    "WORK": {"EDUCATION": 0.6, "SHOPPING": 0.01, "COMMUNITY": 0.39},
    "LIVE": {"EDUCATION": 0.3, "SHOPPING": 0.05, "COMMUNITY": 0.65},
    "RELAX": {"EDUCATION": 0.15, "SHOPPING": 0.55, "COMMUNITY": 0.3},
    "ENTERTAIN": {"EDUCATION": 0.1, "SHOPPING": 0.8, "COMMUNITY": 0.1},
    "EXERCISE": {"EDUCATION": 0.2, "SHOPPING": 0.4, "COMMUNITY": 0.4}
}

m = model.SenzModel()
m.setPi(pi)
m.setMotionConditionP(motion_condition)

s = senz.Senz(m)

u = utility.Utility(s)
u.printTransitionMatrix()
u.printEmissionMatrix()
u.printHiddenState()
u.printVisibleOutput()

s.initTrainSample([{'motion': 'SITTING', 'location': 'EDUCATION'},
                   {'motion': 'SITTING', 'location': 'EDUCATION'},
                   {'motion': 'SITTING', 'location': 'COMMUNITY'},
                   {'motion': 'SITTING', 'location': 'EDUCATION'},
                   {'motion': 'SITTING', 'location': 'EDUCATION'},
                   {'motion': 'WALKING', 'location': 'SHOPPING'},
                   {'motion': 'WALKING', 'location': 'SHOPPING'},

                   {'motion': 'SITTING', 'location': 'EDUCATION'},
                   {'motion': 'SITTING', 'location': 'EDUCATION'},
                   {'motion': 'SITTING', 'location': 'COMMUNITY'},
                   {'motion': 'SITTING', 'location': 'EDUCATION'},
                   {'motion': 'SITTING', 'location': 'EDUCATION'},
                   {'motion': 'WALKING', 'location': 'SHOPPING'},
                   {'motion': 'WALKING', 'location': 'SHOPPING'},

                   {'motion': 'SITTING', 'location': 'EDUCATION'},
                   {'motion': 'SITTING', 'location': 'EDUCATION'},
                   {'motion': 'SITTING', 'location': 'COMMUNITY'},
                   {'motion': 'SITTING', 'location': 'EDUCATION'},
                   {'motion': 'SITTING', 'location': 'EDUCATION'},
                   {'motion': 'WALKING', 'location': 'SHOPPING'},
                   {'motion': 'WALKING', 'location': 'SHOPPING'},

                   {'motion': 'SITTING', 'location': 'EDUCATION'},
                   {'motion': 'SITTING', 'location': 'EDUCATION'},
                   {'motion': 'SITTING', 'location': 'COMMUNITY'},
                   {'motion': 'SITTING', 'location': 'EDUCATION'},
                   {'motion': 'SITTING', 'location': 'EDUCATION'},
                   {'motion': 'WALKING', 'location': 'SHOPPING'},
                   {'motion': 'WALKING', 'location': 'SHOPPING'},

                   {'motion': 'SITTING', 'location': 'EDUCATION'},
                   {'motion': 'SITTING', 'location': 'EDUCATION'},
                   {'motion': 'SITTING', 'location': 'COMMUNITY'},
                   {'motion': 'SITTING', 'location': 'EDUCATION'},
                   {'motion': 'SITTING', 'location': 'EDUCATION'},
                   {'motion': 'RUNNING', 'location': 'COMMUNITY'},
                   {'motion': 'RUNNING', 'location': 'COMMUNITY'}
                   ])

s.BaumWelchLearn(0.01)
s.ViterbiDecode()

u.printTransitionMatrix()
u.printEmissionMatrix()
u.printHiddenState()
u.printVisibleOutput()

print "The outcome:", s.getQ()