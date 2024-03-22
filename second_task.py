from datetime import datetime


def get_moving_time():
    
    n = int(input())
    rocket_logs, status_list = record_data(n)
    keys = sorted(list(rocket_logs.keys()), reverse=True)
    moving_time = []

    for id in keys:
        sort_logs = sorted(rocket_logs[id], key=lambda item: (item["day"], item["hour"], item["minute"]))
        diff_time = count_diff_time(sort_logs, status_list)
        moving_time.append(str(diff_time))
        
    return ' '.join(moving_time)


def count_diff_time(sort_logs, status_list):

    diff_time = 0
    diff_day = 0
    diff_hour = 0
    diff_minute = 0
    list_1 = ["A", "B", "C"]
    list_2 = ["A", "B", "S"]
    list_3 = ["A", "S"]

    if status_list != list_1 and status_list != list_2 and status_list != list_3:
        diff_time = 0

    for i in range(len(sort_logs)):

        if sort_logs[i]["status"] != 'A':
            diff_day += sort_logs[i]["day"] - sort_logs[i - 1]["day"]
            diff_hour += sort_logs[i]["hour"] - sort_logs[i - 1]["hour"]
            diff_minute += sort_logs[i]["minute"] - sort_logs[i - 1]["minute"]
            diff_time = diff_day * 24 * 60 + diff_hour * 60 + diff_minute
        else:
            i += 1
    
    return round(diff_time)


def record_data(n):
    status_list = []
    rocket_logs = {}

    for i in range(n):
        log_data = input().split()
        id = log_data[3]
        keys = list(rocket_logs.keys())
        message = {"day": int(log_data[0]),
                   "hour": int(log_data[1]),
                   "minute": int(log_data[2]),
                   "status": log_data[4]}
        
        status_list.append(message["status"])

        if id not in keys:
            rocket_logs[id] = [message]
        else: 
            rocket_logs[id].append(message)

    return rocket_logs, status_list

print(get_moving_time())