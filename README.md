# Data Pipeline

Data processing pipeline for the MicrocontrollerLab project.

The pipeline retrieves raw sensor data from the database, processes and
transforms the data, and stores derived features for further analysis
and visualization.

## Pipeline


```text
Raw Sensor Data
       ↓
   Ingestion
       ↓
   Inspection
       ↓
   Validation
       ↓
  Normalization
       ↓
  Aggregation
       ↓
Feature Engineering
       ↓
 Feature Database
       ↓
Visualization / Analysis / ML
```

## Data Source

The pipeline processes sensor data collected by the MicrocontrollerLab
sensor infrastructure.

Raw sensor data is currently stored in Supabase PostgreSQL.

Raw Data

Current sensor measurements include:

DHT11 temperature
DHT11 humidity
DHT20 temperature
DHT20 humidity
Gas sensor raw value
Light sensor raw value
Timestamp
Output

Processed and derived sensor features will be stored separately from the
raw sensor data.

The raw data remains unchanged and serves as the source for subsequent
processing and analysis.

Automation

The pipeline is intended to run automatically using GitHub Actions.

Manual execution will also be supported for development and testing.

## Output

Processed sensor features stored in a dedicated feature database/table.

## Automation

Processing will be executed using GitHub Actions.

## Project Status

🚧 Early development