import os
import gspread
from dotenv import load_dotenv
from gspread_formatting import (
    cellFormat, textFormat, color,
    set_column_width, set_frozen, format_cell_range,
    GridRange, ConditionalFormatRule, BooleanRule, BooleanCondition,
    set_conditional_formatting
)

load_dotenv()

PROJECT_TRACKERS = os.getenv("PROJECT_TRACKERS")

CELL_CONTENT = {
        "B2": "Total Hours",
        "B4": "Activity",
        "C4": "Type",
        "D4": "Start Date",
        "E4": "Due Date",
        "F4": "Responsible"
    }

def create_sheet(sheet_name, dates):
    """Creates a new project tracker in Google Sheets."""
    gc = gspread.service_account(filename="service_account.json")
    sh = gc.create(sheet_name, folder=PROJECT_TRACKERS)
    ws = sh.sheet1
    # Formatting
    fmt_bold = cellFormat(textFormat=textFormat(bold=True))
    fmt_highlight = cellFormat(backgroundColor=color(red=183, green=225, blue=205))
    set_column_width(ws, "A:A", 21)
    set_frozen(ws, rows=1)
    set_frozen(ws, cols=1)
    format_cell_range(ws, "1:4", fmt_bold)

    # Conditional Formatting
    rule = ConditionalFormatRule(
        ranges=[GridRange.from_a1_range("A1:A"), ws],
        booleanRule=BooleanRule(
            condition=BooleanCondition("CUSTOM_FORMULA", ["=LEN(A1)>0"]),
            format=fmt_highlight
        )
    )
    set_conditional_formatting(ws, [rule])

    # Auto-resize
    sh.batch_update({
        "requests": [
            {
                "autoResizeDimensions": {
                    "dimensions": {
                        "sheetId": ws.id,
                        "dimension": "ROWS",
                        "startIndex": 0,
                        "endIndex": 1
                    }
                }
            },
            {
                "autoResizeDimensions": {
                    "dimensions": {
                        "sheetId": ws.id,
                        "dimension": "COLUMNS",
                        "startIndex": 1,
                        "endIndex": 2
                    }
                }
            }
        ]
    })

    # Add dates and cell content
    for i, d in enumerate(dates):
        column_name = chr(ord("G") + i)
        ws.update(f"{column_name}1", d)

    for key, value in CELL_CONTENT.items():
        ws.update(key, value)

    return sh