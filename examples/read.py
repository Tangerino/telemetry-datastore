from datetime import datetime
from time import time

from telemetry_datastore import Datastore

if __name__ == '__main__':
    start_time = time()
    total = 0
    with Datastore("/tmp/telemetry.db3") as ds:
        sensors = ds.sensors()
        sensor_list = []
        for sensor in sensors:
            sensor_list.append(sensor["id"])
        data_points = ds.raw(sensor_list, 0, datetime.utcnow())
        for values in data_points.values():
            total += len(values)
    elapsed = time() - start_time
    print("{} data points read in {} seconds".format(total, round(elapsed, 2)))
