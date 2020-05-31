from telemetry_datastore import Datastore, Timeseries
from datetime import datetime, timedelta
from time import time

if __name__ == '__main__':
    end_date = datetime.utcnow()
    start_date = end_date - timedelta(days=1)
    t = Timeseries("beta")
    start_time = time()
    while start_date < end_date:
        t.add(start_date, 1)
        start_date += timedelta(seconds=1)
    with Datastore("/tmp/telemetry.db3", create=True) as ds:
        ds.create(t)
    elapsed = time() - start_time
    print("{} data points inserted in {} seconds".format(len(t), round(elapsed, 2)))

