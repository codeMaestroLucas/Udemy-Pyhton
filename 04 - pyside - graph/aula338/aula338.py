# Graph Interface (GUI)

# pip install pyside6

"""
This lib uses another lib called Qt to make the graphs => C++
    
The Pyside & PyQt are just the bridge - binding - between this lib and Python.

#? Doc: https://doc.qt.io/qtforpython/

#! OBS: License ©
#! PyQt => GPL;
#!    U can make only opensource softwares.
#! PySide => LGPL;
#!    U can make every type of software as long as u don't change the original
#! lib.
#! https://tldrlegal.com/license/gnu-lesser-general-public-license-v3-(lgpl-3)
"""

def main() -> None:
    """Function used to run the main code."""
    from PySide6.QtWidgets import QApplication, QPushButton
    
    app = QApplication()
    app.exec()
    
    btn = QPushButton('Txt for the Button.')
    btn.setStyleSheet('font-size: 40px; color: red;') # Just like CSS.
    btn.show()


if __name__ == '__main__':
    main()