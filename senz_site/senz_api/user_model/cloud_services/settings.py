
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

# --- poi type code:
# - PUBLIC_PLACE -> 休闲场所
# - COMMUNITY    -> 社区
# - OFFICE       -> 办公地点
# - ON_THE_WAY   -> 路上
# - SCHOOL       -> 学校
# - HOSPITAL     -> 医院
# - MALL         -> 商场
# - RESTAURANT   -> 餐厅
# - SCENIC       -> 旅游景点
# - SERVICE      -> 生活服务
location_code_set = {
    # Public place
    "leisure":        "PUBLIC_PLACE",# 休闲娱乐
    # Community
    "neighborhood":   "COMMUNITY",# 地产小区
    "estate":         "COMMUNITY",# 房地产
    # Office
    "government":     "OFFICE",# 政府机构
    "company":        "OFFICE",# 公司企业
    "finance":        "OFFICE",# 金融
    # Restaurant
    "canteen":        "RESTAURANT",# 餐饮
    "tasty":          "RESTAURANT",# 美食
    # School
    "education":      "SCHOOL",# 教育
    "training":       "SCHOOL",# 教育培训
    # On the way
    "transportation": "ON_THE_WAY",# 交通设施
    # Scenic
    "landmark":       "SCENIC",# 行政地标
    "scene":          "SCENIC",# 旅游景点
    # Service
    "service":        "SERVICE",# 生活服务
    # Mall
    "shopping":       "MALL",# 购物
    # Hospital
    "hospital":       "HOSPITAL",# 医疗
    # Other
    "car":            "OTHER",# 汽车服务
    "other":          "OTHER" # 其他
}

# Debug url
debug_url      = "http://httpbin.org/post"
