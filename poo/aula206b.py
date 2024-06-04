from aula206a import Person, path
import json

# Used to upload an JSON file and transform it in to a Person class

def upload_to_class(file):
    with open(file, 'r', encoding='utf8') as json_file:
        data = json.load(json_file)
        person = Person(data['name'], data['age'])
        return person

p1 = upload_to_class(path)
print(p1.__dict__)