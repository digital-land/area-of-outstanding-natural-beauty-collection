#!/usr/bin/env python3

import csv

w = csv.DictWriter(open("pipeline/lookup.csv", "w", newline=""), ["prefix", "reference", "entity"], extrasaction="ignore")
w.writeheader()

for n in range(1,37):

   row = {}
   row["prefix"] = "area-of-outstanding-natural-beauty"
   row["reference"] = str(n)
   row["entity"] = str(1000000 + n)

   w.writerow(row) 
