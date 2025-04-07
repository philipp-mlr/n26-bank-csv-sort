import csv
from collections import defaultdict

# Read the CSV
input_file = "input.csv"
accounts = defaultdict(list)

# Read all rows and group by account name
with open(input_file, newline='', encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile)
    header = reader.fieldnames
    
    for row in reader:
        account_name = row["Account Name"]
        if account_name:  # Only process rows with a valid account name
            accounts[account_name].append(row)

# Write each account's data into its own CSV file
for account, rows in accounts.items():
    filename = f"{account.lower()}.csv"
    with open(filename, mode="w", newline='', encoding='utf-8') as outfile:
        writer = csv.DictWriter(outfile, fieldnames=header)
        writer.writeheader()
        writer.writerows(rows)

print("Files written for accounts:", ", ".join(accounts.keys()))
