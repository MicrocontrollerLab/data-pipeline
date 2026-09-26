import json
import os
from urllib.request import Request, urlopen
from urllib.error import HTTPError, URLError

from dotenv import load_dotenv


# Load environment variables from .env
load_dotenv()


# Read Supabase connection details
SUPABASE_URL: str = os.environ["SUPABASE_URL"]
SUPABASE_PUBLISHABLE_KEY: str = os.environ["SUPABASE_PUBLISHABLE_KEY"]


def store_features(data: dict) -> None:
    """
    Store one feature snapshot in the Supabase database.
    """

    # Build the Supabase REST API endpoint
    endpoint: str = (
        f"{SUPABASE_URL}/rest/v1/feature_snapshots"
    )

    # Convert the feature dictionary into JSON
    payload: bytes = json.dumps(data).encode("utf-8")

    # Create the HTTP POST request
    request = Request(
        endpoint,
        data=payload,
        headers={
            "apikey": SUPABASE_PUBLISHABLE_KEY,
            "Content-Type": "application/json",
            "Prefer": "return=minimal",
        },
        method="POST",
    )

    try:
        # Send the feature snapshot to Supabase
        with urlopen(request) as response:
            print(
                f"Storage successful: "
                f"HTTP {response.status}"
            )

    except HTTPError as error:
        print(f"HTTP error: {error.code}")
        print(error.read().decode("utf-8"))
        raise

    except URLError as error:
        print(f"Connection error: {error}")
        raise