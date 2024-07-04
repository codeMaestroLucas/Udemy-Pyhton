# LOCALE

def main() -> None:
    """Function used to run the main code."""
    import locale
    import calendar
    
    print('\n', '='*75)
    print(f'{"DICIONÁRIO EM PT-BR":^75}')
    print('='*75)
    locale.setlocale(locale.LC_ALL, 'pt_BR.utf-8')
    print(calendar.calendar(2024))

    print('\n', '='*75)
    print(f'{"DICIONÁRIO EM ENG":^75}')
    print('='*75)
    locale.setlocale(locale.LC_ALL, 'en_US.UTF-8') # utf-8 or UTF-8
    print(calendar.calendar(2024))
    
if __name__ == '__main__':
    main()