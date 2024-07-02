'''
This file is the main window (view). It contains any function that directly build or alter the view.
'''

import PyQt6.QtWidgets as pyqtWidgets
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QAction, QPixmap
import config
import components
import matplotlib.image as mpimg
from PIL import Image

class MainWindow(pyqtWidgets.QMainWindow):

    def __init__(self):
        # initialises.
        super().__init__()
        self.setWindowTitle('My App')
        self.setFixedSize(config.WINDOW_SIZE, config.WINDOW_SIZE)

        self.baseLayout = pyqtWidgets.QHBoxLayout()
        self.baseLayout.setSpacing(0)
        self.baseLayout.setContentsMargins(0, 0, 0, 0)
        self.centralWidget = pyqtWidgets.QWidget()
        self.centralWidget.setLayout(self.baseLayout)
        self.setCentralWidget(self.centralWidget)

        self._createFrame()
    
    def _createFrame(self):
        # MENU
        menuBar = self.menuBar()
        self._createActions()

        imageMenu = pyqtWidgets.QMenu("&Image", self)
        menuBar.addMenu(imageMenu)
        imageMenu.addAction(self.importImageAction)
        imageMenu.addAction(self.exportImageAction)
        imageMenu.addAction(self.clearImageAction)

        treeMenu = menuBar.addMenu("&Tree")
        treeMenu.addAction(self.importTreeAction)
        treeMenu.addAction(self.exportTreeAction)
        treeMenu.addAction(self.clearTreeAction)

        newStageMenu = menuBar.addMenu("&New Stage")
        newStageMenu.addAction(self.stage1Action)
        newStageMenu.addAction(self.stage2Action)

        # TREE
        self.treeDisplay = pyqtWidgets.QWidget()
        self.treeDisplay.setStyleSheet('background-color: green')
        self.treeLayout = pyqtWidgets.QVBoxLayout()
        self.treeLayout.setAlignment(Qt.AlignmentFlag.AlignTop)
        self.treeLayout.setSpacing(10)
        self.treeLayout.setContentsMargins(0, 0, 0, 0)
        self.treeDisplay.setLayout(self.treeLayout)
        self.baseLayout.addWidget(self.treeDisplay)

        # IMAGE AND TUNING BOARD
        baseRightLayout = pyqtWidgets.QVBoxLayout()
        baseRightLayout.setSpacing(0)
        baseRightLayout.setContentsMargins(0, 0, 0, 0)

        self.imageDisplay = pyqtWidgets.QLabel()
        self.imageDisplay.setStyleSheet('background-color: black')
        baseRightLayout.addWidget(self.imageDisplay)

        self.tuningDisplay = pyqtWidgets.QLabel()
        self.tuningDisplay.setStyleSheet('background-color: blue')
        baseRightLayout.addWidget(self.tuningDisplay)

        bodyRightPanel = pyqtWidgets.QWidget()
        bodyRightPanel.setLayout(baseRightLayout)
        self.baseLayout.addWidget(bodyRightPanel)

    
    def _createActions(self):
        # creates the actions to trigger the menu buttons.
        self.importImageAction = QAction("&Import", self)
        self.importImageAction.triggered.connect(self.importImage)
        self.exportImageAction = QAction("&Export", self)
        self.clearImageAction = QAction("&Clear", self)
        
        self.importTreeAction = QAction("&Import", self)
        self.exportTreeAction = QAction("&Export", self)
        self.clearTreeAction = QAction("&Clear", self)
        self.clearTreeAction.triggered.connect(self.clearTree)

        self.stage1Action = QAction("&Stage 1", self)
        self.stage1Action.triggered.connect(self.addToTree)
        self.stage2Action = QAction("&Stage 2", self)

    
    def importImage(self):
        # imports an image into the QLabel.
        fname = pyqtWidgets.QFileDialog.getOpenFileName(self, "Choose Image", "", "Image Files (*.jpg, *.png)")[0]
        pixmap = QPixmap(fname)  # opening image as a pixmap.
        img = pixmap.toImage()  # getting image data.
        h = self.imageDisplay.height()
        w = self.imageDisplay.width()
        self.imageDisplay.setPixmap(pixmap.scaled(w, h, Qt.AspectRatioMode.KeepAspectRatio))  # inserting pixmap into QLabel.

    
    def clearTree(self):
        for i in reversed(range(self.treeLayout.count())): 
            self.treeLayout.itemAt(i).widget().setParent(None)

    
    def addToTree(self):
        newStage = components.TreeStage()
        self.treeLayout.addWidget(newStage)
        newStage.deleteBtn.clicked.connect(self.removeStage)
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


    def removeStage(self):
        stage = self.sender().parent().parent()  # getting the TreeStage object.
        self.treeLayout.removeWidget(stage)

