import PyQt6.QtWidgets as pyqtWidgets
from PyQt6.QtCore import Qt
import config
import components

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
        self.menuBtn1 = pyqtWidgets.QPushButton('New Stage')
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
        self.treeDisplay = pyqtWidgets.QWidget()
        self.treeDisplay.setStyleSheet('background-color: green')
        self.treeLayout = pyqtWidgets.QVBoxLayout()
        self.treeLayout.setAlignment(Qt.AlignmentFlag.AlignTop)
        self.treeLayout.setSpacing(10)
        self.treeLayout.setContentsMargins(0, 0, 0, 0)
        self.treeDisplay.setLayout(self.treeLayout)
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
    
    def changeImageBoxColour(self):
        self.imageDisplay.setStyleSheet('background-color: pink')
    
    def addToTree(self):
        newStage = components.TreeStage()
        self.treeLayout.addWidget(newStage)
        newStage.moveBtn1.clicked.connect(self.moveStageUp)
        newStage.moveBtn2.clicked.connect(self.moveStageDown)
    
    def moveStageUp(self):
        stage = self.sender().parent().parent()  # getting the TreeStage object.
        currIdx = self.treeLayout.indexOf(stage)
        if currIdx == 0:  # can't move up if at the top already.
            return False
        self.treeLayout.removeWidget(stage)
        self.treeLayout.insertWidget(currIdx - 1, stage)


    def moveStageDown(self):
        stage = self.sender().parent().parent()  # getting the TreeStage object.
        currIdx = self.treeLayout.indexOf(stage)
        if currIdx == self.treeLayout.count() - 1:  # can't move down if at the bottom already.
            return False
        self.treeLayout.removeWidget(stage)
        self.treeLayout.insertWidget(currIdx + 1, stage)

