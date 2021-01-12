import json
import csv

csvFile = "sandbox-installs.csv"
jsonFilePath = "jsonOutput.json"

# Read the CSV file and add data to dictionary
data = {}
with open(csvFile, encoding="utf8") as csvFile:
    csvReader = csv.DictReader(csvFile)
    for rows in csvReader:
        id = rows["user_pseudo_id"]
        data[id] = rows

# Write data to JSON file
with open(jsonFilePath, "w") as jsonFile:
    jsonFile.write(json.dumps(data, indent=4))
