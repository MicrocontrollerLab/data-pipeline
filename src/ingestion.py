import json
import os
from datetime import datetime, timedelta, timezone
from urllib.request import Request, urlopen
from urllib.error import HTTPError, URLError
from urllib.parse import urlencode

from dotenv import load_dotenv


# Load environment variables from the local .env file
load_dotenv()


# Read Supabase connection details from environment variables
SUPABASE_URL: str = os.environ["SUPABASE_URL"]
SUPABASE_PUBLISHABLE_KEY: str = os.environ["SUPABASE_PUBLISHABLE_KEY"]

PAGE_SIZE: int = 1000


def ingest_data(hours: int = 24) -> list[dict]:
    """
    Retrieve sensor data from Supabase for the specified time window.

    Data is fetched page by page because the Supabase REST API
    limits the number of records returned per request.

    Args:
        hours: Number of hours of historical data to retrieve.

    Returns:
        A list containing the retrieved sensor records.
    """

    # Calculate the start timestamp of the requested time window
    start_time: str = (
        datetime.now(timezone.utc) - timedelta(hours=hours)
    ).isoformat()

    # Start with the first page
    offset: int = 0

    # Store all retrieved records
    data: list[dict] = []

    while True:
        # Build the query parameters for the current page
        query: str = urlencode({
            "select": "*",
            "time": f"gte.{start_time}",
            "limit": PAGE_SIZE,
            "offset": offset,
            "order": "time.asc",
        })

        # Build the Supabase REST API endpoint
        endpoint: str = f"{SUPABASE_URL}/rest/v1/sensor_data?{query}"

        # Create the HTTP GET request
        request: Request = Request(
            endpoint,
            headers={
                "apikey": SUPABASE_PUBLISHABLE_KEY,
                "Accept": "application/json",
            },
            method="GET",
        )

        try:
            # Send the request and read the response
            with urlopen(request) as response:
                page: list[dict] = json.loads(
                    response.read().decode("utf-8")
                )

        except HTTPError as error:
            # Print the response body to make API errors easier to debug
            print(f"HTTP error: {error.code}")
            print(error.read().decode("utf-8"))
            raise

        except URLError as error:
            # Handle connection-related errors
            print(f"Connection error: {error}")
            raise

        # Add the current page to the complete dataset
        data.extend(page)

        # Report the current page
        print(
            f"Fetched {len(page)} records "
            f"(offset {offset})"
        )

        # Stop when fewer records than the page size were returned
        if len(page) < PAGE_SIZE:
            break

        # Move to the next page
        offset += PAGE_SIZE

    # Return the complete dataset to the caller
    return data


if __name__ == "__main__":
    # Run the ingestion directly when this file is executed
    data: list[dict] = ingest_data(hours=24)

    # Report the total number of records received
    print(f"Successfully ingested {len(data)} records.")

    # Print the first five records for inspection
    for record in data[:5]:
        print(record)