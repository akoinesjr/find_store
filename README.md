# Find Store

find_store.py will locate the nearest store (as the crow flies) from
store-locations.csv, print the matching store address, as well as
the distance to that store.

This repository contains the following files:

store-locations.csv - This is a tabular dataset of the locations of every store of a major national retail chain.
find_store.py - The Find Store application
requirements.txt - Find Store's dependencies
config.ini - Configuration values for Find Store
tests.py -

# Set Up

1. Ensure that you are in an environment with both Python 3 and pip installed
2. Create and activate a new Python 3 virtual environment
3. Create a file called config.ini in the top level of this repository with the following contents:

```
[config]
google_key = $YOUR_GOOGLE_MAPS_API_KEY_HERE
```

4. Run pip install -r requirement.txt to install Find Store's depencies

# Usage Instructions

```

Usage:
  python3 find_store.py --address="<address>"
  python3 find_store.py --address="<address>" [--units=(mi|km)] [--output=text|json]
  python3 find_store.py --zip=<zip>
  python3 find_store.py --zip=<zip> [--units=(mi|km)] [--output=text|json]

Options:
  --zip=<zip>          Find nearest store to this zip code. If there are multiple best-matches, return the first.
  --address            Find nearest store to this address. If there are multiple best-matches, return the first.
  --units=(mi|km)      Display units in miles or kilometers [default: mi]
  --output=(text|json) Output in human-readable text, or in JSON (e.g. machine-readable) [default: text]

Example
  python3 find_store.py --address="1770 Union St, San Francisco, CA 94123"
  python3 find_store.py --zip=94115 --units=km
```

# Notes

I assumed that it would be okay to have this program run by executing the file with the relevant arguments as opposed to having the program run from within an interactive mode. It could of course be relatively easily modified to run that way instead.

I also decided that it made sense for the program to accept either a zip code or address argument but not both.