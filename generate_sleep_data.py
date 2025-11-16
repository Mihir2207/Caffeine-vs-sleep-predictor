# generate_sleep_data.py
import csv
import random
import math

# We'll generate 100 points
rows = []
random.seed(42)

# Typical caffeine intake range 0 - 600 mg
# Sleep quality on scale 0-10, decreasing with caffeine with noise
for i in range(100):
    # spread caffeine values more across range
    caffeine = round(random.uniform(0, 600), 1)
    # base sleep quality follows a negative slope: high caffeine -> lower quality
    # formula: base = 9.5 - 0.01 * caffeine  (so 0 mg -> 9.5, 600 mg -> 3.5)
    base = 9.5 - 0.01 * caffeine
    # add noise: normal-ish with sd 0.6
    noise = random.gauss(0, 0.6)
    quality = base + noise
    # clip to 0-10
    quality = max(0, min(10, round(quality, 2)))
    rows.append((round(caffeine,1), quality))

# write CSV
with open("caffeine_sleep.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["Caffeine_mg", "Sleep_Quality"])
    for r in rows:
        writer.writerow(r)

print("Generated caffeine_sleep.csv with", len(rows), "rows.")
