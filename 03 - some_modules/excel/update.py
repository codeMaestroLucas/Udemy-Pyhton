from openpyxl.worksheet.worksheet import Worksheet

def update(worksheet: Worksheet, col: str, row: int, value) -> None:
    col_row: str = f'{col.capitalize().strip()}{row}'
    
    print(f'Changing the value of the Cell in {col_row} from {worksheet[col_row].value} to {value}')
    worksheet[col_row].value = value