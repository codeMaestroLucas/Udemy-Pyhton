from text import SimpleText
from txt_decorator import UpperTextDecorator, EndExclamationTextDecorator

def main() -> None:
    """Function used to run the main code."""
    s_txt: SimpleText = SimpleText('Hello World')
    print(s_txt.render())
    
    upper_txt: UpperTextDecorator = UpperTextDecorator(s_txt)
    print(upper_txt.render())

    exclamation_txt: EndExclamationTextDecorator = EndExclamationTextDecorator(upper_txt)
    print(exclamation_txt.render())



if __name__ == '__main__':
    main()