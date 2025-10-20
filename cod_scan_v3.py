import requests
import json
import csv
import re

def parse_formula(formula):
    composition = {}
    # Remove any leading/trailing dashes or spaces
    formula = formula.strip().strip('-').strip()
    # Use regex to find element-symbol followed by optional number
    matches = re.findall(r'([A-Z][a-z]?)(\d*)', formula)
    for elem, num_str in matches:
        num = int(num_str) if num_str else 1
        composition[elem] = composition.get(elem, 0) + num
    return composition

# Parameters for searching materials containing 'carbonate' in metadata and elements H, C, O
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
    
    # Filter entries where the number of oxygen atoms is exactly 3
    filtered_data = []
    for entry in data:
        if 'formula' in entry:
            comp = parse_formula(entry['formula'])
            if 'O' in comp and comp['O'] == 3:
                filtered_data.append(entry)
    
    # Write to CSV with more detailed fields
    with open('cod_results_filtered.csv', 'w', newline='') as csvfile:
        fieldnames = ['ID', 'Name/Details', 'Formula', 'Spacegroup', 'Volume', 'a', 'b', 'c', 'alpha', 'beta', 'gamma', 'Cell Temperature']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        
        writer.writeheader()
        
        for entry in filtered_data:
            row = {
                'ID': entry.get('file', ''),
                'Name/Details': entry.get('text', ''),  # Contains chemical name, mineral name, authors, etc.
                'Formula': entry.get('formula', ''),
                'Spacegroup': entry.get('sg', ''),
                'Volume': entry.get('vol', ''),
                'a': entry.get('a', ''),
                'b': entry.get('b', ''),
                'c': entry.get('c', ''),
                'alpha': entry.get('alpha', ''),
                'beta': entry.get('beta', ''),
                'gamma': entry.get('gamma', ''),
                'Cell Temperature': entry.get('celltemp', '')
            }
            writer.writerow(row)
    
    print(f"Filtered results (with exactly 3 oxygen atoms) saved to cod_results_filtered.csv. Found {len(filtered_data)} entries.")
else:
    print(f"Error fetching data: {response.status_code}")