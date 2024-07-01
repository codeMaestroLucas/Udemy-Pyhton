# STRING MODULE
# Usefull to make long texts and use variables in this texts.
# doc: https://docs.python.org/3/library/string.html#template-strings

def main() -> None:
    """Function used to run the main code."""
    import string as s
    from pathlib import Path
    
    file = Path(__file__).parent / 'aula298.txt'
    
    data = dict(
        name= 'Lucas',
        value= 323.50,
        date= '2024-05-21',
        enteprise= 'LS Enterprise',
        number= '+88 (99) 4444-2222'
    )

    with open(file, 'r', encoding= 'utf8') as file:
        text = file.read()
        template = s.Template(text)
        text_formatted = template.substitute(data)
        print(text_formatted)

if __name__ == '__main__':
    main()