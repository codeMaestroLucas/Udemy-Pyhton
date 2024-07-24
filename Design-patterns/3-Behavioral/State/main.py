# main.py
from document import Document
from state import Draft

def main() -> None:
    document = Document()

    
    document.publish()
    document.publish()
    document.reject()

    
    document.set_state(Draft())
    document.reject()
    document.publish()
    document.reject()

if __name__ == "__main__":
    main()
