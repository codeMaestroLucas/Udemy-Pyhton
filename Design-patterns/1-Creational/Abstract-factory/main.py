from abs_factory import GUIFactory, WindowsFactory, MacFactory
from buttons import Button
from checkboxes import Checkbox


def create_gui(factory: GUIFactory):
    """Function to create a GUI using the given factory."""
    btn: Button = factory.create_button()
    check: Checkbox = factory.create_checkbox()

    print(btn.click())
    print(check.check())



def main() -> None:
    """Function used to run the main code."""
    
    awnser = input("Windows/MAC ? ").strip().lower()
    factory: GUIFactory
    
    if awnser == 'windows':
        factory = WindowsFactory()

    elif awnser =='mac':
        factory = MacFactory()

    else:
        print("Invalid input. Please try again.")
        return

    create_gui(factory)


if __name__ == '__main__':
    main()