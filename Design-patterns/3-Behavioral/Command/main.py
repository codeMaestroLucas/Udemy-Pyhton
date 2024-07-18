from text_editor import TxtEditor
from command import TextEditorInvoker, WriteCommand

def main() -> None:
    """Function used to run the main code."""
    editor = TxtEditor()
    invoker = TextEditorInvoker()

    com1 = WriteCommand(editor, 'Hello, ')
    com2 = WriteCommand(editor, 'Wolrd')
    com3 = WriteCommand(editor, '!')

    invoker.execute_command(com1)
    invoker.execute_command(com2)
    invoker.execute_command(com3)

    print(editor.get_txt())

    invoker.undo_last_command()
    print(editor.get_txt())
    
    invoker.undo_last_command()
    print(editor.get_txt())



if __name__ == '__main__':
    main()