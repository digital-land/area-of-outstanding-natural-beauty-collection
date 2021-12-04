#!/usr/bin/env python3

import csv
from os import path
from glob import glob
from pathlib import Path
from decimal import Decimal

lookup = {}
entity = {}

csv.field_size_limit(1000000000)

# ignoring resource for now ..
def key(row):
    return ",".join([row[f] for f in ["pipeline", "organisation", "value"]])


for row in csv.DictReader(open("specification/dataset.csv")):
    entity[row["dataset"]] = Decimal(row["entity-minimum"])


if path.exists("pipeline/lookup.csv"):
    for row in csv.DictReader(open("pipeline/lookup.csv")):
        lookup[key(row)] = row
        e = Decimal(row["entity"])
        if e > entity[row["pipeline"]]:
            entity[row["pipeline"]] = e + 1


for directory in glob("transformed/*"):
    dataset = Path(directory).name
    for path in glob(directory + "/*.csv"):
        for row in csv.DictReader(open(path)):
            row.setdefault("organisation", "")
            row["pipeline"] = dataset
            row["value"] = row[dataset]
            lookup[key(row)] = row


w = csv.DictWriter(open("pipeline/lookup.csv", "w", newline=""), ["pipeline", "resource", "organisation", "value", "entity"], extrasaction="ignore")
w.writeheader()

for key, row in lookup.items():
    if not row["value"]:
        next

    if not  row.get("entity", ""):
        dataset = row["pipeline"]
        row["entity"] = entity[dataset]
        entity[dataset] = entity[dataset] + 1
    w.writerow(row)
