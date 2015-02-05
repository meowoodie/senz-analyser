__author__ = 'woodie'

import senz_api.hmm_senz.core.behavior as behavior

# Time = ("MORNING", "NOON", "AFTERNOON", "NIGHT", "MIDNIGHT")
# Location = ("ENTERTAINMENT", "COMMUNITY", "GOVERNMENT", "CATERING", "EDUCATION",
#             "TRAFFIC", "FINANCE", "TRAVEL", "HOTEL", "COMPANY",
#             "SHOPPING", "MEDICAL", "BUSINESS")
# Motion = ("SITTING", "WALKING", "RUNNING", "RIDING", "DRIVING")
#
# behav = []
#
# for t in Time:
#     for l in Location:
#         for m in Motion:
#             behav.append(behavior.Behavior(time = t, location = l, motion = m))
#
# for i in behav:
#     print "time:", i.evidence("time"), "location:", i.evidence("location"), "motion:", i.evidence("motion")

print behavior.createVisibleBehaviorSet()