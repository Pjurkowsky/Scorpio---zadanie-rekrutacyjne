import psutil
import time
import json

data = {
    "CPU": {
        # "core 1": {
        # "load": 0,
        # "temp": 0
        # }
    },
    "RAM": {
        "total": 0,
        "used": 0,
        "available": 0
    },
    "Disk": {
        "used": 0
    },
    "Network Interface": {
        # "essa": {
        # "ip": 0.0.0.0,
        # "status": "Down",
        # "net_in": 0,
        # "net_out": 0
        # }
    }
}


def read_data():
    i = 0
    for load in psutil.cpu_percent(interval=1, percpu=True):
        data["CPU"].update({"core " + str(i): {"load": load, "temp": 0}})
        i += 1
        # print(psutil.sensors_temperatures())

    data["RAM"]["total"] = round(psutil.virtual_memory().total / 1024 / 1024, 3)
    data["RAM"]["used"] = psutil.virtual_memory().percent
    data["RAM"]["available"] = round(psutil.virtual_memory().available / 1024 / 1024, 3)

    data["Disk"]["used"] = psutil.disk_usage('/').percent

    for inf in psutil.net_if_addrs().items():
        net_in, net_out = net_usage(inf[0])
        data["Network Interface"].update({inf[0]: {"ip": inf[1][0].address,
                                                   "status": 'UP' if psutil.net_if_stats()[inf[0]].isup else "DOWN",
                                                   "net_in": net_in, "net_out": net_out}})

    with open('/home/pjury/Desktop/Scorpio-zadanie-rekrutacyjne/system_data_readings.txt', 'w') as outfile:
        json.dump(data, outfile)

    print(data)


def net_usage(inf):
    net_stat = psutil.net_io_counters(pernic=True, nowrap=True)[inf]
    net_in_1 = net_stat.bytes_recv
    net_out_1 = net_stat.bytes_sent
    time.sleep(1)
    net_stat = psutil.net_io_counters(pernic=True, nowrap=True)[inf]
    net_in_2 = net_stat.bytes_recv
    net_out_2 = net_stat.bytes_sent

    net_in = round((net_in_2 - net_in_1) / 1024 / 1024, 3)
    net_out = round((net_out_2 - net_out_1) / 1024 / 1024, 3)

    return net_in, net_out


def main():
    while (True):
        read_data()
        time.sleep(5)


if __name__ == '__main__':
    main()
