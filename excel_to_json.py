"""
Excel to JSON Converter
Converts Excel files to JSON format using pandas
"""

import pandas as pd
import json
from pathlib import Path


def excel_to_json(excel_file, output_file=None, sheet_name=0, orient='records'):
    """
    Convert Excel file to JSON
    
    Args:
        excel_file (str or Path): Path to the Excel file
        output_file (str or Path): Path to output JSON file (optional)
        sheet_name (str/int): Sheet name or index (default: 0 for first sheet)
        orient (str): JSON orientation ('records', 'index', 'columns', 'values', 'table')
    
    Returns:
        str: JSON string or saves to file
    """
    try:
        # Convert paths to Path objects
        excel_path = Path(excel_file)
        output_path = Path(output_file) if output_file else None

        # Read Excel file
        print(f"Reading Excel file: {excel_path}")
        df = pd.read_excel(excel_path, sheet_name=sheet_name)
        
        # Convert to JSON
        json_data = df.to_json(orient=orient, indent=2, force_ascii=False)
        
        # Save to file if output_file is specified
        if output_path:
            output_path.parent.mkdir(parents=True, exist_ok=True)
            output_path.write_text(json_data, encoding='utf-8')
            print(f"JSON saved to: {output_path}")
            return None
        else:
            return json_data
            
    except FileNotFoundError:
        print(f"Error: File '{excel_path}' not found")
        return None
    except Exception as e:
        print(f"Error converting Excel to JSON: {e}")
        return None


def list_sheets(excel_file):
    """List all sheets in the Excel file"""
    try:
        excel_path = Path(excel_file)
        excel_data = pd.ExcelFile(excel_path)
        print(f"Available sheets in '{excel_path}':")
        for i, sheet in enumerate(excel_data.sheet_names):
            print(f"  {i}: {sheet}")
    except Exception as e:
        print(f"Error reading Excel file: {e}")


# Example usage
if __name__ == "__main__":


    file_path = "ressources_RAG/03_Outils_de_scénarisation/R_03_001_Tableau_87_Activites_Moodle_ABC.xlsx"

    # Convert Excel to JSON with default settings
    result = excel_to_json(file_path, "output.json")
    
    
