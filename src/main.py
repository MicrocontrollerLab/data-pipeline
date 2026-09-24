from ingestion import ingest_data
from validation import validate_data
from normalization import normalize_data
from aggregation import aggregate_data
from feature_engineering import engineer_features


def main():
    # Step 1: Retrieve raw sensor data from the database
    raw_data = ingest_data(hours=24)

    # Step 2: Check the incoming data for required fields and valid values
    validated_data = validate_data(raw_data)

    # Step 3: Convert and standardize the validated data
    normalized_data = normalize_data(validated_data)

    # Step 4: Calculate statistical aggregates from the normalized data
    aggregated_data = aggregate_data(normalized_data)

    # Step 5: Create derived features for further analysis
    features = engineer_features(aggregated_data)

    # Return the final feature data
    return features

if __name__ == "__main__":
    # Start the data pipeline
    main()