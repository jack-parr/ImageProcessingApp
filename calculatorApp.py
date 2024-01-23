'''
Tutorial: https://realpython.com/python-pyqt-gui-calculator/

This is the calculator example shown in this tutorial. Uses the Model-View-Controller (MVC) design pattern.
Model: handles logic.
View: handles GUI, hosting widgets and receives user actions and events.
Controller: connects model and the view. In this example receives target maths expressions from GUI, asks model to perform calculations, then updates GUI with result.

How this app works:
1. The user performs action or request on the view.
2. View notifies the controller about the user action.
3. Controller gets the request and queries the model for a response.
4. Model processes controller's query, performs the required computations, returns result.
5. Controller receives the model's response and updates the view.
6. User finally sees the requested result on the view.
'''

import sys
import ast
from functools import partial  # used to connect signals with methods that need extra arguments.
from PyQt6.QtCore import Qt
import PyQt6.QtWidgets as pyqtWidgets

ERROR_MSG = 'ERROR'
WINDOW_SIZE = 235
DISPLAY_HEIGHT = 35
BUTTON_SIZE = 40

class CalculatorWindow(pyqtWidgets.QMainWindow):
    # this is the main window (view).
    def __init__(self):
        # initialises.
        super().__init__()
        self.setWindowTitle('Calculator')
        self.setFixedSize(WINDOW_SIZE, WINDOW_SIZE)
        self.generalLayout = pyqtWidgets.QVBoxLayout()
        centralWidget = pyqtWidgets.QWidget(self)
        centralWidget.setLayout(self.generalLayout)
        self.setCentralWidget(centralWidget)
        self._createDisplay()
        self._createButtons()
    
    def _createDisplay(self):
        # creates the calculator display.
        self.display = pyqtWidgets.QLineEdit()
        self.display.setFixedHeight(DISPLAY_HEIGHT)
        self.display.setAlignment(Qt.AlignmentFlag.AlignRight)
        self.display.setReadOnly(True)
        self.generalLayout.addWidget(self.display)
    
    def _createButtons(self):
        # creates the calculator buttons.
        self.buttonMap = {}
        buttonsLayout = pyqtWidgets.QGridLayout()
        keyBoard = [
            ['7', '8', '9', '/', 'C'],
            ['4', '5', '6', '*', 'R'],
            ['1', '2', '3', '-', '.'],
            ['0', '(', ')', '+', '='],
        ]

        for row, keys in enumerate(keyBoard):
            for col, key in enumerate(keys):
                self.buttonMap[key] = pyqtWidgets.QPushButton(key)
                self.buttonMap[key].setFixedSize(BUTTON_SIZE, BUTTON_SIZE)
                buttonsLayout.addWidget(self.buttonMap[key], row, col)
        
        self.generalLayout.addLayout(buttonsLayout)

    def setDisplayText(self, text):
        # this sets the text in the display.
        self.display.setText(text)
    
    def getDisplayText(self):
        # this retrieves the text in the display.
        return self.display.text()
    
    def clearDisplay(self):
        # this clears the display.
        self.setDisplayText('')


def evaluateExpression(expression):
    # this evaluates the given expression (model).
    try:
        node = ast.parse(expression, mode='eval')
        result = str(eval(compile(node, '<string>', 'eval')))
    except Exception:
        result = ERROR_MSG
    return result


class CalculatorController:
    # this is the controller class.
    def __init__(self, model, view):
        self._evaluate = model
        self._view = view
        self._connectSignalsAndSlots()
    
    def _calculateResult(self):
        # this calculates and displays the result.
        result = self._evaluate(expression=self._view.getDisplayText())
        self._view.setDisplayText(result)

    def _buildExpression(self, subExpression):
        # this concatenates the display with every new value the user enters.
        if self._view.getDisplayText() == ERROR_MSG:
            self._view.clearDisplay()
        expression = self._view.getDisplayText() + subExpression
        self._view.setDisplayText(expression)
    
    def _demolishExpression(self):
        # this removes the last inputted character if possible.
        if self._view.getDisplayText() == ERROR_MSG or self._view.getDisplayText() == '':
            self._view.clearDisplay()
        else:
            expression = self._view.getDisplayText()[:-1]
            self._view.setDisplayText(expression)

    def _connectSignalsAndSlots(self):
        for keySymbol, button in self._view.buttonMap.items():
            if keySymbol not in {'=', 'C', 'R'}:
                button.clicked.connect(partial(self._buildExpression, keySymbol))
        self._view.buttonMap['='].clicked.connect(self._calculateResult)
        self._view.buttonMap['R'].clicked.connect(self._demolishExpression)
        self._view.buttonMap['C'].clicked.connect(self._view.clearDisplay)
    

def main():
    # this is the main running function.
    calcApp = pyqtWidgets.QApplication([])
    calcWindow = CalculatorWindow()
    calcWindow.show()
    CalculatorController(model=evaluateExpression, view=calcWindow)
    sys.exit(calcApp.exec())


if __name__ == '__main__':
    main()
