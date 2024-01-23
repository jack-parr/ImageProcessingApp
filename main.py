'''
This is the main running file for the app.
'''

import sys
import PyQt6.QtWidgets as pyqtWidgets
import model
import view
import controller

def main():
    # this is the main running function.
    app = pyqtWidgets.QApplication([])
    mainWindow = view.MainWindow()
    mainWindow.show()
    controller.MainController(model=model.MainModel, view=mainWindow)
    sys.exit(app.exec())


if __name__ == '__main__':
    main()
