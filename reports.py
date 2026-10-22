"""CSV export for reports (no database code here)."""
import csv
import os
from datetime import datetime

REPORT_DIR = "reports"


def write_csv(name, headers, rows):
    """Write rows to reports/<name>_<timestamp>.csv and return the file path."""
    os.makedirs(REPORT_DIR, exist_ok=True)
    stamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    path = os.path.join(REPORT_DIR, f"{name}_{stamp}.csv")
    with open(path, "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(headers)
        writer.writerows(rows)
    return path
