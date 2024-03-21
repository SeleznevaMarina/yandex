from datetime import datetime


def get_moving_time():
    
    n = int(input())
    rocket_logs = record_data(n)
    keys = sorted(list(rocket_logs.keys()), reverse=True)
    moving_time = []

    for id in keys:
        sort_logs = sorted(rocket_logs[id], key=lambda item: item["date"])
        diff_time = count_diff_time(sort_logs)
        moving_time.append(str(diff_time))
        
    return ' '.join(moving_time)


def count_diff_time(sort_logs):

    diff_time = 0

    for i in range(len(sort_logs)):

        if sort_logs[i]["status"] != 'A':
            diff_time += (sort_logs[i]["date"] - sort_logs[i - 1]["date"]).total_seconds() / 60 ## rounding??
        else:
            i += 1
    
    return round(diff_time)


def record_data(n):
    rocket_logs = {}

    for i in range(n):
        log_data = input().split()
        id = log_data[3]
        keys = list(rocket_logs.keys())
        message = {"date": datetime.strptime(f"2021-{log_data[0]}-{log_data[1]}-{log_data[2]}", "%Y-%j-%H-%M"),
                   "status": log_data[4]}

        if id not in keys:
            rocket_logs[id] = [message]
        else: 
            rocket_logs[id].append(message)

    return rocket_logs

print(get_moving_time())