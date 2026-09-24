def normalize_data(data: list[dict]) -> list[dict]:
    """
    Normalize sensor values into consistent data types.
    """

    normalized_data: list[dict] = []

    for record in data:
        normalized_record = record.copy()

        # Normalize timestamp to ISO 8601 format
        normalized_record["time"] = str(record["time"])

        # Normalize sensor values to float
        normalized_record["dht11_temperature"] = float(
            record["dht11_temperature"]
        )
        normalized_record["dht11_humidity"] = float(
            record["dht11_humidity"]
        )
        normalized_record["dht20_temperature"] = float(
            record["dht20_temperature"]
        )
        normalized_record["dht20_humidity"] = float(
            record["dht20_humidity"]
        )
        normalized_record["gas_raw"] = float(
            record["gas_raw"]
        )
        normalized_record["light"] = float(
            record["light"]
        )

        normalized_data.append(normalized_record)

    print(
        f"Normalization successful: "
        f"{len(normalized_data)} records normalized."
    )

    return normalized_data