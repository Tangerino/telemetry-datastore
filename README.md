# Telemetry Data Store

The telemetry data store allows store, aggregate and retrieve telemetry data for your IoT project
using simple API call that will hide all the complexity from the user.

No file system manipulation is necessary and several databases can be created to separate different contexts if necessary.

Once the telemetry is inserted into the database, an aggregation process is executed automatically.

The raw data (the one inserted by the user) and the aggregated data is immediately available.

The library performs the following aggregations:
- Sum
- Average
- Count
- Maximum and
- Minimum

Data is aggregated over the hour, day, month and year.

## Use cases

- Permanent telemetry storage
- Data manipulation at the edge
 

## Installation

```angular2
pip3 install telemetry-datastore
```

## Examples
Please look the the `examples` folder
