import csv
import re

FILENAME = 'CategoryUpdates.mbox'

# read file
mboxFile = open(FILENAME, encoding="utf8")

emails = {}
for line in mboxFile:
    if "From:" in line:
        email = re.findall(r'[\w\.-]+@[\w\.-]+', line)
        if len(email) > 0:
            if email[0] in emails:
                emails[email[0]] += 1
            else:
                emails.update({email[0]: 1})
mboxFile.close()

# Output to CSV
field_names = ['Email', 'Count']
with open('Emails.csv', 'w') as f:
    writer = csv.DictWriter(f, fieldnames=field_names)
    writer.writeheader()
    for key in emails:
        writer.writerow({'Email': key, 'Count': emails[key]})