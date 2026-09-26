# 🧪 Data Pipeline

Data processing pipeline for the **MicrocontrollerLab** project.

The pipeline retrieves raw sensor data from Supabase, validates and transforms the data, generates a statistical 24-hour snapshot, derives additional features, and stores the results for further analysis and visualization.

## 🔄 Pipeline

```text
📡 Raw Sensor Data
        ↓
📥 Ingestion
        ↓
🔍 Validation
        ↓
🔧 Normalization
        ↓
📊 Aggregation
        ↓
🧬 Feature Engineering
        ↓
💾 Storage
        ↓
📈 Feature Snapshots
```

## 🗄️ Data Source

The pipeline processes sensor data collected by the MicrocontrollerLab sensor infrastructure.

Raw sensor data is currently stored in **Supabase PostgreSQL**.

### 📡 Raw Data

Current sensor measurements include:

* 🌡️ DHT11 temperature
* 💧 DHT11 humidity
* 🌡️ DHT20 temperature
* 💧 DHT20 humidity
* 🧪 Gas sensor raw value
* 💡 Light sensor raw value
* 🕒 Timestamp

The raw data remains unchanged and serves as the source for subsequent processing and analysis.

## ⚙️ Processing

### 📥 Ingestion

Retrieves the last 24 hours of sensor data from Supabase.

The data is retrieved using pagination to handle datasets larger than the API page size.

### 🔍 Validation

Checks incoming records for the required sensor fields.

### 🔧 Normalization

Converts sensor values into a consistent format for further processing.

### 📊 Aggregation

Reduces the 24-hour dataset to a single statistical snapshot.

For each sensor value, the pipeline calculates:

* 📈 Average
* 📊 Median
* ⬇️ Minimum
* ⬆️ Maximum

The snapshot also contains metadata such as:

* 🕒 Snapshot timestamp
* ⏱️ Aggregation window
* 🔢 Number of source records

### 🧬 Feature Engineering

Creates derived values from the aggregated sensor data, such as:

* 🌡️ Sensor temperature difference
* 📏 Temperature range
* 💧 Humidity range
* 🧪 Gas range
* 💡 Light range

## 💾 Output

Processed data is stored separately from the raw sensor data.

The current Supabase database contains:

```text
sensor_data
    ↓
📡 Raw sensor measurements

feature_snapshots
    ↓
📊 Processed 24-hour snapshots
   and derived features
```

The raw sensor data remains unchanged.

## 🤖 Automation

The complete pipeline can be executed through **GitHub Actions**.

The workflow currently supports:

* ⏱️ Automatic hourly execution
* ▶️ Manual execution for development and testing

The workflow retrieves the required Supabase credentials from GitHub Actions secrets.

## 🟢 Current Status

**Basic pipeline operational**

The complete processing chain is currently functional:

```text
☁️ Supabase
   ↓
📥 Ingestion
   ↓
🔍 Validation
   ↓
🔧 Normalization
   ↓
📊 Aggregation
   ↓
🧬 Feature Engineering
   ↓
💾 Storage
   ↓
☁️ Supabase feature_snapshots
```

The pipeline has been successfully executed through GitHub Actions and is currently configured for hourly automated execution.
