import csv
csvFile = "sandbox-installs.csv"

# Empty list to store counts
i = []
z = []

# Function to determine how many Samsung devices are using version 1.16.2 or earlier
def comparionLogic():
    for row in csvReader:
        if row["device_brand_name"] == "Samsung":
            if row["app_version"] <= "1.16.2":
                i.append(1)
        if row["device_brand_name"] == "Apple":
            if row["app_version"] <= "1.16.2":
                z.append(1)

# Reading CSV file
with open(csvFile, encoding="utf8") as csvFile:
    csvReader = csv.DictReader(csvFile)
    comparionLogic()
    difference = len(z)-len(i)

print("The amount of Samsung devices using version 1.16.2 or earlier is equal to:", len(i))
print("The amount of Apple devices using version 1.16.2 or earlier is equal to:", len(z))
print("There are", difference, "more Apple devices using the older version than Samsung")



