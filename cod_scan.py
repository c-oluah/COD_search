import requests
import json
import csv

# Parameters for searching materials containing 'carbonate' in metadata (e.g., name) and hydrogen (H) as an element
params = {
    'text': 'carbonate',      # Keyword search in metadata (chemical name, mineral name, etc.)
    'el1': 'H',              # Must contain hydrogen
    'el2': 'C',              # Must contain carbon (for CO3)
    'el3': 'O',              # Must contain oxygen (for CO3)
    'format': 'json'         # Return results in JSON format for easy parsing
}

url = 'https://www.crystallography.net/cod/result'

response = requests.get(url, params=params)

if response.status_code == 200:
    data = json.loads(response.text)
    
    # Assuming data is a list of dictionaries with keys like 'file', 'formula', 'text' (text contains names and bibliography)
    # We extract ID (file), formula, and name (using text as proxy for name/details)
    
    with open('cod_results.csv', 'w', newline='') as csvfile:
        fieldnames = ['ID', 'Formula', 'Name/Details']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        
        writer.writeheader()
        
        for entry in data:
            row = {
                'ID': entry.get('file', ''),
                'Formula': entry.get('formula', ''),
                'Name/Details': entry.get('text', '')  # This field contains chemical name, mineral name, authors, etc.
            }
            writer.writerow(row)
    
    print("Results saved to cod_results.csv")
else:
    print(f"Error fetching data: {response.status_code}")
