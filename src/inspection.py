def inspect_data(data: list[dict]) -> None:
    """
    Take a quick look at the incoming data.
    Inspection does not change the data.
    """

    # How many records did we receive?
    print(f"Records received: {len(data)}")

    # Stop here if there is no data
    if not data:
        print("No data to inspect.")
        return

    # What fields are available?
    print(f"Fields: {list(data[0].keys())}")

    # Are there any empty values?
    empty_values = 0

    for record in data:
        for value in record.values():
            if value is None:
                empty_values += 1

    print(f"Empty values: {empty_values}")
    print("Inspection: Data inspection completed.")