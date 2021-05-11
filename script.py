import csv
import re
# (?P<name>[\w\s-]*)
rows = []
r = "(?P<prefix>mrs|miss|mr|Dr|ms|Mister|Prof)"


with open('examples.csv', 'r',) as file:
    reader = csv.reader(file, delimiter = '\t')
    for row in reader:
         rows.append(row[0])

    
for item in rows:
        x = re.match(r, item, re.MULTILINE | re.IGNORECASE)
        print(item)
        print(x)
