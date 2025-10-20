# COD_search

A Python pipeline for screening the **Crystallography Open Database (COD)** to identify **carbonate and hydrogen-containing materials** for potential **thermochemical heat storage (TCHS)** applications.

## 🔍 Features
- Connects directly to COD via MySQL (read-only access)
- Searches for compounds containing C, H, and O with carbonate/bicarbonate keywords
- Downloads corresponding CIF structures
- Uses `pymatgen` to:
  - Detect CO₃ motifs (C bonded to 3 O atoms with ~120° O–C–O angles)
  - Identify OH and H₂O hydration features
  - Filter out organics and very large cells
- Outputs a clean CSV (`cod_candidates_filtered.csv`) for DFT/MD pre-screening

## ⚙️ Requirements
Python ≥ 3.10  
Install dependencies:
```bash
pip install pymatgen mysql-connector-python tqdm requests

Usage
python cod_scan_v3.py


Results:

cod_candidates_filtered.csv → shortlisted candidates

cifs/ → downloaded CIF files

👩🏽‍🔬 Author

Developed by Chukwumaobi Oluah (TU Eindhoven)
For research on thermochemical heat storage materials, 4TUnaTES project