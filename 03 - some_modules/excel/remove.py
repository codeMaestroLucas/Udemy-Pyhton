from openpyxl import Workbook

def remove_sheet(workbook: Workbook, sheet_name: str) -> None:
    workbook.remove(workbook[sheet_name])