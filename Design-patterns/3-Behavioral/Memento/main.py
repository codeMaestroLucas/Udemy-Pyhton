from text import TextEditor
from caretaker import CareTaker

def main() -> None:
    """Function used to run the main code."""
    editor = TextEditor()
    caretaker = CareTaker(editor)
    
    editor.write('Hello,')
    caretaker.save()

    editor.write(' World')

    caretaker.save()
    
    caretaker.undo()
    print(editor.get_content())

    caretaker.undo()
    print(editor.get_content())

    caretaker.undo()
    caretaker.undo()
    caretaker.undo()
    caretaker.undo()
    caretaker.undo()

    editor.write('New word')
    print(editor.get_content())

if __name__ == '__main__':
    main()
