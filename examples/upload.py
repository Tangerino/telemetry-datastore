from time import time

from telemetry_datastore import Datastore


def data_push_to_cloud(data_points):
    last_id = 0
    for data_point in data_points:
        last_id = data_point["id"]
    return last_id


if __name__ == '__main__':
    start_time = time()
    total = 0
    index = 0
    batch_size = 1000
    with Datastore("/tmp/telemetry.db3") as ds:
        sensors = ds.sensors()
        while True:
            values = ds.raw_dump(index, batch_size)
            if values:
                last_index = data_push_to_cloud(values)
                index = last_index + 1
                total += len(values)
            else:
                break
    elapsed = time() - start_time
    print("{} data points published to cloud in {} seconds".format(total, round(elapsed, 2)))
