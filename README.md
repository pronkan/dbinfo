# dbinfo
Get, sort and process database information, retrieved from API endpoint in JSON format  

## About
This homework project reads from provided API endpoint in compatible structured format and processes  
data to form easily human-readable table of database entries, sorted by storage usage percentage.  

## Requirement
> Write a script that retrieves info from the API and prints out:
> - all database names
> - their storage type
> - their used storage
> - percentage of storage used.
> Sort the output by storage used in descending order by percentage of storage used.

## Prerequisites
- Python 3.12
- poetry 1.8.3

## Installation
```bash
git clone git@github.com:pronkan/dbinfo.git
cd dbinfo
python3 -m venv .venv
source .venv/bin/activate
pip install poetry
poetry install --no-root
```

## Usage
```bash
poetry run python src/main.py <API_ENDPOINT>
```

## Example output
```bash
INFO:root:Getting data from <API_ENDPOINT>
INFO:root:Sorting databases by storage used percentage
INFO:root:Printing sorted table
+-------------------------+----------------+----------------+----------------+------------------+
| DB name                 | Storage type   |   Storage size | Storage used   | Storage used %   |
+=========================+================+================+================+==================+
| interview-db-54         | standard       |             10 | 6.409          | 64.09            |
+-------------------------+----------------+----------------+----------------+------------------+
| interview-db-26         | gp2            |            200 | 120.364        | 60.182           |
+-------------------------+----------------+----------------+----------------+------------------+
| interview-db-42         | standard       |            100 | 34.262         | 34.262           |
+-------------------------+----------------+----------------+----------------+------------------+
| interview-db-41         | standard       |             10 | 3.105          | 31.05            |
+-------------------------+----------------+----------------+----------------+------------------+
| interview-db-0          | gp2            |             10 | 3.033          | 30.33            |
+-------------------------+----------------+----------------+----------------+------------------+
| interview-db-0-replica  | gp2            |             10 | 2.966          | 29.66            |
+-------------------------+----------------+----------------+----------------+------------------+
| interview-db-38         | gp2            |             10 | 2.895          | 28.95            |
+-------------------------+----------------+----------------+----------------+------------------+
| interview-db-2          | gp2            |             10 | 2.691          | 26.91            |
+-------------------------+----------------+----------------+----------------+------------------+
| interview-db-71         | gp2            |             10 | 2.683          | 26.83            |
+-------------------------+----------------+----------------+----------------+------------------+
| interview-db-71-replica | gp2            |             10 | 2.683          | 26.83            |
+-------------------------+----------------+----------------+----------------+------------------+
...
```

## Testing
TBD can be added if needed

## License
MIT

## Author
Andrii Pronkin
