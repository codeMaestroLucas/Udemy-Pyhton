# JSON - JavaScript Object Notation
# OBS: Strings must be in "", the conversion of the string of python to json is
# automatic.

"""
PYTHON                JSON
dict                  object
list, tuple           array
str                   string
int, float            number
bool - True & False   boolean - true & false
None                  null
"""

def main() -> None:
    """Function used to run the main code."""
    import json
    
    data = {
        'name': 'lucas',
        'age': 23,
        'city': 'brasilia',
        'addresses': {
            'home': 'home st 123 nº10',
            'job': 'job st 456 nº20'
            },
        'friends': ['joao', 'maria', 'pedro'],
        'maried': False,
        'cars': None,
        'salary': 5000.0,
    }
    
    file_path = r'some_modules\\json\\'
    file_name = 'aula289.json'
    file_to_create = file_path + file_name

    with open (file_to_create, 'w', encoding= 'utf-8') as file:
        file.write(json.dumps(data, indent= 4))
        
    
    with open (file_to_create, 'r', encoding= 'utf8') as file:
        json_string = json.load(file)
        print(json_string)
    
if __name__ == '__main__':
    main()
    
    # More examples -> https://youtu.be/T17BTNKBeJY