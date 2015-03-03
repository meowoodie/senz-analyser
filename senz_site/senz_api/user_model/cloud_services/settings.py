
# The api's protocol
protocol  = "http://"

# The cloud servers' ip address
server_ip = {
    "Aliyun1": "120.27.30.239",
    "Aliyun2": "182.92.4.173"
}

# The service api url
get_motion_state_url = ":9001/predictByRawData/"
get_sound_scence_url = ""
get_poi_info_url     = ":9003/senz/poi_Gpeacon/"

# Other params
# --- state code :
# - 0 -> sitting
# - 1 -> driving
# - 2 -> riding
# - 3 -> walking
# - 4 -> running
state_code_set = ["SITTING", "DRIVING", "RIDING", "WALKING", "RUNNING"]

# --- poi type code:
location_code_set = {
    # Public place
    "leisure":        "PUBLIC_PLACE",
    # Community
    "neighborhood":   "COMMUNITY",
    "estate":         "COMMUNITY",
    # Office
    "government":     "OFFICE",
    "company":        "OFFICE",
    "finance":        "OFFICE",
    # Restaurant
    "canteen":        "RESTAURANT",
    "tasty":          "RESTAURANT",
    # School
    "education":      "SCHOOL",
    "training":       "SCHOOL",
    # On the way
    "transportation": "ON_THE_WAY",
    # Scenic
    "landmark":       "SCENIC",
    "scene":          "SCENIC",
    # Service
    "service":        "SERVICE",
    # Mall
    "shopping":       "MALL",
    # Hospital
    "hospital":       "HOSPITAL",
    # Other
    "car":            "OTHER",
    "other":          "OTHER"
}

# Debug url
debug_url      = "http://httpbin.org/post"
