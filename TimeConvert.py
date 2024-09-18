import datetime
cur_split = "\n"

def curTimeMin(tm:int):
    return tm * 60
def curTimeSec(tm:int):
    return tm * (60 ** 2)

cur_time = datetime.datetime.now()
cur_hour = cur_time.hour
cur_min = curTimeMin(cur_hour)
cur_sec = curTimeSec(cur_hour)




print(cur_hour, cur_min, cur_sec)