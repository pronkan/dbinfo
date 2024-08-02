import requests
import json
import sys
from utils import DBInfo, sorted_tabel, sort_list

import logging

logging.basicConfig(level=logging.INFO)


def main():
    """
    Main function to get data from url, parse it and print the sorted table
    :return: Sorted multi-line string table
    """
    # Get url as argument
    url = sys.argv[1]
    logging.info(f"Getting data from {url}")

    # Get data from url in json format
    response = requests.get(url)

    # Check if data is correct and parse it
    db_info_data_raw = json.loads(response.text)

    # Create list of db info data objects
    databases = []
    if db_info_data_raw and isinstance(db_info_data_raw, dict):
        #     databases = [DBInfo(**item) for sublist in db_info_data_raw.values() for item in sublist]
        #     This approach is a lot simple and faster, howewer I tend to preserve manipulatrable data from the start,
        #     if I don;t know if it'll be useful in the future, like keys of original dict
        for i, db_info in db_info_data_raw.items():
            for info in db_info:
                logging.debug("Creating DB object from DB info data")
                db_object = DBInfo(**info)
                logging.debug("Appended DB object to databases list")
                databases.append(db_object)
    else:
        raise ValueError("Data is not in correct format")

    # Sorting list by percentage of used storage per DB if it is available (I assume if used in the data null, it means,
    # that it is not available or data is incomplete) this storages will be printed in the end with 'N/A' value
    logging.info("Sorting databases by storage used percentage")
    databases = sort_list(databases)

    # Print sorted table
    logging.info("Printing sorted table")

    print(sorted_tabel(databases))


if __name__ == "__main__":
    main()
