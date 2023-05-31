import uuid
import csv

# Create an empty list for the UUIDs
uuids = []

# Generate and store the UUIDs
for i in range(307):
    uuids.append(str(uuid.uuid4()).replace("-", ""))

# Create a CSV file and write the UUIDs to it
with open('uuids.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["user_id"])
    writer.writerows([[uid] for uid in uuids])

print("Unique User Id's successfully generated!")
