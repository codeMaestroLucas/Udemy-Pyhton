# EXCEL

# pip install openpyxl
#? Doc: https://openpyxl.readthedocs.io/en/stable/


def main() -> None:
    """Function used to run the main code."""
    from pathlib import Path
    from openpyxl.worksheet.worksheet import Worksheet
    from openpyxl.workbook.workbook import Workbook
    from create import create_sheet
    from remove import remove_sheet
    from adding_data import adding_data
    from reading import reading
    from update  import update

    ROOT_PATH = Path(__file__).parent
    WORKBOOK = ROOT_PATH / 'controll-grades.xlsx'

    worksheet: Worksheet ; workbook: Workbook

    
    worksheet, workbook = create_sheet()


    adding_data(worksheet)


    remove_sheet(workbook, 'Sheet')


    update(worksheet, 'a', 2, 'Carlão')


    reading(worksheet)


    
    workbook.save(WORKBOOK)

if __name__ == '__main__':
    main()