import os
from cognite.client import CogniteClient
from cognite.client.data_classes import TimeSeries, Datapoints
 
def main():
    # Initialize client (uses env variables)
    client = CogniteClient()
 
    ts_external_id = "demo_timeseries_github"
 
    # Check if timeseries exists
    existing = client.time_series.retrieve(external_id=ts_external_id)
 
    if not existing:
        print("Creating new time series...")
        ts = TimeSeries(
            external_id=ts_external_id,
            name="GitHub Demo Time Series",
            description="Created via GitHub Actions",
            is_string=False
        )
        client.time_series.create(ts)
    else:
        print("Time series already exists")
 
    # Insert datapoints
    datapoints = [
        (int(1e12), 10.5),
        (int(1e12 + 1000), 12.3),
        (int(1e12 + 2000), 11.8),
    ]
 
    print("Inserting datapoints...")
    client.datapoints.insert(
        external_id=ts_external_id,
        datapoints=datapoints
    )
 
    print("Done!")
 
if __name__ == "__main__":
    main()