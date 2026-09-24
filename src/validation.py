# Fields that must exist in every sensor record
REQUIRED_FIELDS: list[str] = [
    "time",
    "dht11_temperature",
    "dht11_humidity",
    "dht20_temperature",
    "dht20_humidity",
    "gas_raw",
    "light",
]

def validate_data(data: list[dict]) -> list[dict]:
    """
    Go through every record in the dataset.
    'index' is the position of the record in the list.
    'record' contains the actual sensor data.
    """
    for index, record in enumerate(data):

        # Check every field that is required for the pipeline.
        for field in REQUIRED_FIELDS:

            # If a required field is missing, stop the pipeline
            # because the record cannot be processed reliably.
            if field not in record:
                raise ValueError(
                    f"Record {index} is missing required field: {field}"
                )

    # Validation ONLY checks the data. No new List[dict]!
    # Return the original dataset after successful validation.
    return data