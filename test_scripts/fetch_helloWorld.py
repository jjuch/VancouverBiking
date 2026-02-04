## Training:  Fetch bikeways records as JSON from Vancouver's Opendatasoft API. The lexicon is https://help.opendatasoft.com/apis/ods-explore-v2/

import json
import sys
import urllib.parse
import requests

BASE = "https://opendata.vancouver.ca/api/explore/v2.1/catalog/datasets/bikeways/records"

def fetch_bikeways(limit=5, bbox=None, fields=None, order_by=None):
    """
    Fetch bikeways records as JSON from Vancouver's Opendatasoft API.

    Args:
        limit (int): number of records
        bbox (tuple): (xmin, ymin, xmax, ymax) in WGS84 for within_bbox filter
        fields (list[str]): list of field names to select
        order_by (str): field to sort by (ascending)

    Returns:
        dict: parsed JSON response
    """
    params = {}

    # limit & sort
    params["limit"] = int(limit)
    if order_by:
        params["order_by"] = order_by

    # select only needed fields (plus geometry is usually "geometry")
    if fields:
        params["select"] = ",".join(fields)

    # optional bbox filter
    if bbox:
        xmin, ymin, xmax, ymax = bbox
        where_expr = f"in_bbox(geom,{xmin},{ymin},{xmax},{ymax})"
        params["where"] = where_expr

    url = BASE + "?" + urllib.parse.urlencode(params, safe="(),")

    try:
        resp = requests.get(url, timeout=20)
        resp.raise_for_status()
    except requests.RequestException as e:
        print(f"HTTP error: {e}", file=sys.stderr)
        print(f"URL was: {url}", file=sys.stderr)
        raise

    try:
        data = resp.json()
    except json.JSONDecodeError as e:
        print("Failed to decode JSON", file=sys.stderr)
        print(resp.text[:500], file=sys.stderr)
        raise

    # Basic sanity checks on expected keys
    if "results" not in data:
        raise RuntimeError(f"Unexpected payload (no 'results'): keys={list(data.keys())}")

    return data

if __name__ == "__main__":
    # Example A: simple 5‑row sample
    print("Example A")
    sample = fetch_bikeways(limit=5)
    print("Sample (first item):")
    print(json.dumps(sample["results"][0], indent=2) if sample["results"] else "No results")

    # Example B: downtown bbox + select + sort
    print("Example B")
    bbox = (49.268,-123.140,49.290,-123.100)  # approx downtown, first latitude then longitude
    fields = ["bike_route_name", "bikeway_type", "geom"]
    data = fetch_bikeways(limit=50, bbox=bbox, fields=fields, order_by="bike_route_name")
    print(f"\nFetched {len(data['results'])} records in bbox.")