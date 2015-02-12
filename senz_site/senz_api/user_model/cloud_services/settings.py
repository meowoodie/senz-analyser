
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
get_poi_info_url     = ""

# Other params
# --- state code :
# - 0 -> sitting
# - 1 -> driving
# - 2 -> riding
# - 3 -> walking
# - 4 -> running
state_code_set = ["SITTING", "DRIVING", "RIDING", "WALKING", "RUNNING"]

# Debug url
debug_url      = "http://httpbin.org/post"
