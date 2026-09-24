
def engineer_features(data: dict) -> dict:
    """
    Create derived features from the aggregated sensor data.
    """

    # Create a copy so the aggregated data remains unchanged.
    features: dict = data.copy()

    # Calculate the temperature range measured by the DHT20.
    features["dht20_temperature_range"] = (
        data["dht20_temperature_max"]
        - data["dht20_temperature_min"]
    )

    # Calculate the humidity range measured by the DHT20.
    features["dht20_humidity_range"] = (
        data["dht20_humidity_max"]
        - data["dht20_humidity_min"]
    )

    # Calculate the difference between the two temperature sensors.
    features["temperature_sensor_difference"] = (
        data["dht20_temperature_average"]
        - data["dht11_temperature_average"]
    )

    # Calculate the range of the raw gas sensor values.
    features["gas_range"] = (
        data["gas_raw_max"]
        - data["gas_raw_min"]
    )

    # Calculate the range of the measured light values.
    features["light_range"] = (
        data["light_max"]
        - data["light_min"]
    )

    print(
        "Feature engineering successful: "
        f"{len(features)} values available."
    )

    return features
