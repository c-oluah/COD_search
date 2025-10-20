# COD_search
A Python pipeline for screening the **Crystallography Open Database (COD)** to identify **carbonate and hydrogen-containing materials** for potential **thermochemical heat storage (TCHS)** applications.

<div style="background-color:#e8f4ff;border-left:4px solid #2b7be4;padding:12px;border-radius:6px">
### 🔷 Features
- Connects directly to COD via MySQL (read-only access)  
- Searches for compounds containing C, H, and O with carbonate/bicarbonate keywords  
- Downloads corresponding CIF structures  
- Uses `pymatgen` to:
    - Detect CO₃ motifs (C bonded to 3 O atoms with ~120° O–C–O angles)
    - Identify OH and H₂O hydration features
    - Filter out organics and very large cells  
- Outputs a clean CSV (`cod_candidates_filtered.csv`) for DFT/MD pre-screening

### ⚙️ Requirements
- Python ≥ 3.10  
- Install dependencies:
```bash
pip install pymatgen mysql-connector-python tqdm requests
```

### 🔷 Quick start
1. Ensure Python and dependencies are installed.  
2. Configure COD MySQL read-only credentials (in the script or env variables).  
3. Run:
```bash
python cod_scan_v3.py
```
</div>

## 🚀 Usage

Run the main scan script from the project root:

```bash
python cod_scan_v3.py
```

Notes:
- Ensure Python ≥ 3.10 and the dependencies listed above are installed.
- Configure COD MySQL read-only credentials either in the script or via environment variables before running.

## 📊 Result

- `cod_candidates_filtered.csv` — shortlisted candidate materials for follow-up DFT/MD screening.
- `cifs/` — directory containing downloaded CIF structure files for the candidates.

## 👩🏽‍🔬 Author

Chukwumaobi Oluah — TU Eindhoven  
For research on thermochemical heat storage materials (4TUnaTES project).