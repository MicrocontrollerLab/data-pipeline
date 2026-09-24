from datetime import datetime, timezone
from statistics import median


def aggregate_data(data: list[dict]) -> dict:
    """
    Create one statistical snapshot from the last 24 hours of sensor data.
    """

    # Stop if there is no data to aggregate.
    if not data:
        raise ValueError("No data available for aggregation.")

    # Define the aggregation window.
    window_hours: int = 24

    # Record the time when this snapshot was created.
    snapshot_time: str = datetime.now(timezone.utc).isoformat()

    # Define the sensor fields that should be aggregated.
    sensor_fields: list[str] = [
        "dht11_temperature",
        "dht11_humidity",
        "dht20_temperature",
        "dht20_humidity",
        "gas_raw",
        "light",
    ]

    # Store metadata about the snapshot.
    aggregated_data: dict = {
        "snapshot_time": snapshot_time,
        "window_hours": window_hours,
        "record_count": len(data),
    }

    # Calculate statistics for every sensor field.
    for field in sensor_fields:

        # Extract all values for the current sensor.
        values: list[float] = [
            float(record[field])
            for record in data
        ]

        # Calculate the arithmetic average.
        aggregated_data[f"{field}_average"] = (
            sum(values) / len(values)
        )

        # Calculate the median value with statistics library.
        aggregated_data[f"{field}_median"] = median(values)

        # Find the lowest measured value.
        aggregated_data[f"{field}_min"] = min(values)

        # Find the highest measured value.
        aggregated_data[f"{field}_max"] = max(values)

    print(
        f"Aggregation successful: "
        f"{len(data)} records aggregated into one "
        f"{window_hours}h snapshot."
    )

    return aggregated_data
