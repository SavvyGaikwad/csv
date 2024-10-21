import csv
import json

# File paths
csv_file_path = 'scores.csv'  # Path to your input CSV file
json_file_path = 'scores_dynamodb.json'  # Path for the output JSON file

# List to hold items for JSON output
items = []

# Read the CSV file
with open(csv_file_path, mode='r', newline='', encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile)  # Use DictReader to read CSV into a dictionary
    for row in reader:
        # Prepare the item format for DynamoDB
        item = {
            "PutRequest": {
                "Item": {
                    "SrNo": {"N": row["Sr. No."]},  # Use Number type
                    "GameName": {"S": row["GameName"] if row["GameName"] else "undefined"},  # Use String type
                    "Score": {"N": row["Score"] if row["Score"] and row["Score"] != "null" else "0"},  # Use Number type
                    "Timestamp": {"S": row["Timestamp"]}  # Use String type
                }
            }
        }
        items.append(item)  # Add the item to the list

# Write to JSON file
with open(json_file_path, 'w') as jsonfile:
    json.dump(items, jsonfile, indent=4)  # Write the JSON data with pretty formatting

print(f"JSON file created at: {json_file_path}")  # Confirmation message
