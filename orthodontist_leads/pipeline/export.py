"""Spreadsheet export for the lead lists."""

from __future__ import annotations

import csv
from pathlib import Path

from openpyxl import Workbook
from openpyxl.styles import Alignment, Font, PatternFill
from openpyxl.utils import get_column_letter

HEADER_FILL = PatternFill("solid", fgColor="1F3B57")
HEADER_FONT = Font(color="FFFFFF", bold=True)
MAX_WIDTH = 52
# openpyxl's worksheet limit is 1,048,576 rows; keep well inside it.
SHEET_ROW_LIMIT = 1_000_000

NUMERIC_COLUMNS = {
    "median_household_income", "median_household_income_zip",
    "median_household_income_county", "provider_count", "services_covered",
    "address_shared_by_practices",
}


def csv_to_xlsx(csv_path: Path, xlsx_path: Path, sheet_name: str = "Leads") -> int:
    with open(csv_path, newline="", encoding="utf-8") as fh:
        reader = csv.reader(fh)
        header = next(reader)
        rows = list(reader)

    if len(rows) > SHEET_ROW_LIMIT:
        raise ValueError(
            f"{csv_path.name} has {len(rows):,} rows, too many for one worksheet; "
            "export the CSV instead"
        )

    wb = Workbook()
    ws = wb.active
    ws.title = sheet_name[:31]
    ws.append(header)
    numeric_idx = {i for i, name in enumerate(header) if name in NUMERIC_COLUMNS}

    for row in rows:
        ws.append([
            (int(v) if (i in numeric_idx and v.strip().lstrip("-").isdigit()) else v)
            for i, v in enumerate(row)
        ])

    for cell in ws[1]:
        cell.fill = HEADER_FILL
        cell.font = HEADER_FONT
        cell.alignment = Alignment(vertical="center")
    ws.freeze_panes = "A2"
    ws.auto_filter.ref = ws.dimensions

    widths: dict[int, int] = {}
    for row in ws.iter_rows(min_row=1, max_row=min(ws.max_row, 400)):
        for cell in row:
            length = len(str(cell.value)) if cell.value is not None else 0
            widths[cell.column] = min(max(widths.get(cell.column, 10), length + 2), MAX_WIDTH)
    for col, width in widths.items():
        ws.column_dimensions[get_column_letter(col)].width = width

    xlsx_path.parent.mkdir(parents=True, exist_ok=True)
    wb.save(xlsx_path)
    return len(rows)
