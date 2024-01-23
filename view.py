import PyQt6.QtWidgets as pyqtWidgets
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QPalette
import config

class MainWindow(pyqtWidgets.QMainWindow):
    # this is the main window (view).
    def __init__(self):
        # initialises.
        super().__init__()
        self.setWindowTitle('My App')
        self.setFixedSize(config.WINDOW_SIZE, config.WINDOW_SIZE)

        self.baseLayout = pyqtWidgets.QVBoxLayout()
        self.baseLayout.setSpacing(0)
        self.baseLayout.setContentsMargins(0, 0, 0, 0)
        self.centralWidget = pyqtWidgets.QWidget()
        self.centralWidget.setLayout(self.baseLayout)
        self.setCentralWidget(self.centralWidget)

        self._createFrame()
    
    def _createFrame(self):
        # MENU
        menuLayout = pyqtWidgets.QHBoxLayout()
        menuLayout.setSpacing(0)
        menuLayout.setContentsMargins(0, 0, 0, 0)
        self.menuBtn1 = pyqtWidgets.QPushButton('1')
        self.menuBtn1.setFixedHeight(config.MENU_BTN_HEIGHT)
        self.menuBtn2 = pyqtWidgets.QPushButton('2')
        self.menuBtn2.setFixedHeight(config.MENU_BTN_HEIGHT)
        self.menuBtn3 = pyqtWidgets.QPushButton('3')
        self.menuBtn3.setFixedHeight(config.MENU_BTN_HEIGHT)
        self.menuBtn4 = pyqtWidgets.QPushButton('4')
        self.menuBtn4.setFixedHeight(config.MENU_BTN_HEIGHT)
        self.menuBtn5 = pyqtWidgets.QPushButton('5')
        self.menuBtn5.setFixedHeight(config.MENU_BTN_HEIGHT)
        
        menuLayout.addWidget(self.menuBtn1)
        menuLayout.addWidget(self.menuBtn2)
        menuLayout.addWidget(self.menuBtn3)
        menuLayout.addWidget(self.menuBtn4)
        menuLayout.addWidget(self.menuBtn5)

        menuPanel = pyqtWidgets.QWidget()
        menuPanel.setFixedHeight(config.MENU_BTN_HEIGHT)
        menuPanel.setLayout(menuLayout)
        self.baseLayout.addWidget(menuPanel)


        # BODY BASE LAYOUT
        bodyBaseLayout = pyqtWidgets.QHBoxLayout()
        bodyBaseLayout.setSpacing(0)
        bodyBaseLayout.setContentsMargins(0, 0, 0, 0)

        # TREE
        self.treeDisplay = pyqtWidgets.QLabel()
        self.treeDisplay.setStyleSheet('background-color: green')
        bodyBaseLayout.addWidget(self.treeDisplay)

        # IMAGE AND TUNING BOARD
        bodyRightLayout = pyqtWidgets.QVBoxLayout()
        bodyRightLayout.setSpacing(0)
        bodyRightLayout.setContentsMargins(0, 0, 0, 0)

        self.imageDisplay = pyqtWidgets.QLabel()
        self.imageDisplay.setStyleSheet('background-color: red')
        bodyRightLayout.addWidget(self.imageDisplay)

        self.tuningDisplay = pyqtWidgets.QLabel()
        self.tuningDisplay.setStyleSheet('background-color: blue')
        bodyRightLayout.addWidget(self.tuningDisplay)

        bodyRightPanel = pyqtWidgets.QWidget()
        bodyRightPanel.setLayout(bodyRightLayout)
        bodyBaseLayout.addWidget(bodyRightPanel)

        # ADDING TO BODY BASE
        bodyBasePanel = pyqtWidgets.QWidget()
        bodyBasePanel.setLayout(bodyBaseLayout)
        self.baseLayout.addWidget(bodyBasePanel)
    
    def _changeImageBoxColour(self):
        print(1)
        self.imageDisplay.setStyleSheet('background-color: pink')
