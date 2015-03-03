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
    "WORK": {"SITTING": 0.9, "WALKING": 0.07, "RUNNING": 0.01, "RIDING": 0.01, "DRIVING": 0.01},
    "LIVE": {"SITTING": 0.4, "WALKING": 0.35, "RUNNING": 0.04, "RIDING": 0.01, "DRIVING": 0.2},
    "RELAX": {"SITTING": 0.85, "WALKING": 0.11, "RUNNING": 0.02, "RIDING": 0.01, "DRIVING": 0.01},
    "ENTERTAIN": {"SITTING": 0.2, "WALKING": 0.5, "RUNNING": 0.1, "RIDING": 0.1, "DRIVING": 0.1},
    "EXERCISE": {"SITTING": 0.05, "WALKING": 0.1, "RUNNING": 0.55, "RIDING": 0.29, "DRIVING": 0.01}
}
location_condition = {
    "WORK": {
        "PUBLIC_PLACE": 0.001,
        "COMMUNITY":    0.1,
        "OFFICE":       0.6,
        "ON_THE_WAY":   0.001,
        "SCHOOL":       0.3,
        "HOSPITAL":     0.001,
        "MALL":         0.001,
        "RESTAURANT":   0.001,
        "SCENIC":       0.001,
        "SERVICE":      0.001,
        "OTHER":        0.001
    },
    "LIVE": {
        "PUBLIC_PLACE": 0.1,
        "COMMUNITY":    0.5,
        "OFFICE":       0.1,
        "ON_THE_WAY":   0.001,
        "SCHOOL":       0.3,
        "HOSPITAL":     0.001,
        "MALL":         0.001,
        "RESTAURANT":   0.001,
        "SCENIC":       0.001,
        "SERVICE":      0.001,
        "OTHER":        0.001
    },
    "RELAX": {
        "PUBLIC_PLACE": 0.3,
        "COMMUNITY":    0.1,
        "OFFICE":       0.001,
        "ON_THE_WAY":   0.001,
        "SCHOOL":       0.001,
        "HOSPITAL":     0.001,
        "MALL":         0.1,
        "RESTAURANT":   0.1,
        "SCENIC":       0.2,
        "SERVICE":      0.2,
        "OTHER":        0.001
    },
    "ENTERTAIN": {
        "PUBLIC_PLACE": 0.4,
        "COMMUNITY":    0.1,
        "OFFICE":       0.001,
        "ON_THE_WAY":   0.001,
        "SCHOOL":       0.001,
        "HOSPITAL":     0.001,
        "MALL":         0.001,
        "RESTAURANT":   0.1,
        "SCENIC":       0.4,
        "SERVICE":      0.001,
        "OTHER":        0.001
    },
    "EXERCISE": {
        "PUBLIC_PLACE": 0.2,
        "COMMUNITY":    0.3,
        "OFFICE":       0.001,
        "ON_THE_WAY":   0.2,
        "SCHOOL":       0.1,
        "HOSPITAL":     0.001,
        "MALL":         0.001,
        "RESTAURANT":   0.001,
        "SCENIC":       0.1,
        "SERVICE":      0.1,
        "OTHER":        0.001
    }
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

print s.hPi
print s.hTransitionP
print s.hEmissionP

print "The outcome:", s.getQ()