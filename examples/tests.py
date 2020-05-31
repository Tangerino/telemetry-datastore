from telemetry_datastore import Timeseries, Datastore
from datetime import datetime, timedelta, date

if __name__ == '__main__':
    ts_name = "alpha"
    t = Timeseries(ts_name)
    today = date.today()
    now = datetime.utcnow()
    start_date = now - timedelta(days=7)
    end_date = now
    while start_date < end_date:
        t.add(start_date, 1)
        start_date += timedelta(minutes=15)
    with Datastore("/tmp/mydb.db3", create=True) as ds:
        ds.create(t)
        sensors = ds.sensors()
        for sensor in sensors:
            if sensor["name"] == ts_name:
                sensor_id = str(sensor["id"])
                data_points = ds.rollup([sensor_id], "2000-01-01", "2022-01-01", ds.day, ds.vcount, iso_date=True)
                for values in data_points.values():
                    for value in values:
                        print("\t{} => {}".format(value["ts"], value["value"]))
                print("")
                data_points = ds.raw([sensor_id], today, "2022-01-01", iso_date=True)
                for values in data_points.values():
                    for value in values:
                        print("\t{} => {}".format(value["ts"], value["value"]))
