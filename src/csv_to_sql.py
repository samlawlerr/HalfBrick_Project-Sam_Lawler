import csv

csvFile = "sandbox-installs.csv"

with open(csvFile, encoding="utf8") as csvFile:
    # Reading headers in CSV file
    reader = csv.reader(csvFile)
    header = next(reader)
    headerString = ', '.join(header)
    # Insert statement
    print("INSERT INTO \n example_table (" + headerString + ") \n VALUES")

    # Formatting rows into valid SQL value statements and printing
    for row in reader:
        values = map((lambda x: '"' + x + '"'), row)
        print("(" + ", ".join(values) + "),")
    print(";")
    csvFile.close()

