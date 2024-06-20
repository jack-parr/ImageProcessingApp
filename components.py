'''
This file contains classes for the custom components that make up the view.
'''

import PyQt6.QtWidgets as pyqtWidgets
import config
import random

class TreeStage(pyqtWidgets.QWidget):

    def __init__(self):
        super().__init__()

        # RANDOM COLOUR ASSIGNMENT FOR TESTING
        i = random.randint(1, 6)
        if i == 1:
            self.setStyleSheet('background-color: pink')
        elif i == 2:
            self.setStyleSheet('background-color: red')
        elif i == 3:
            self.setStyleSheet('background-color: orange')
        elif i == 4:
            self.setStyleSheet('background-color: yellow')
        elif i == 5:
            self.setStyleSheet('background-color: blue')

        self.setFixedHeight(config.TREE_STAGE_HEIGHT)

        self.titleBox = pyqtWidgets.QLabel('Title')
        self.titleBox.setFixedSize(int(config.TREE_PANEL_WIDTH - config.TREE_MOVE_BTN_WIDTH - (config.TREE_STAGE_HEIGHT / 2)), int(config.TREE_STAGE_HEIGHT / 2))
        self.titleBox.setStyleSheet("border: 1px solid black;")
        self.paramsBox = pyqtWidgets.QLabel('Params')
        self.paramsBox.setFixedSize(int(config.TREE_PANEL_WIDTH - config.TREE_MOVE_BTN_WIDTH - (config.TREE_STAGE_HEIGHT / 2)), int(config.TREE_STAGE_HEIGHT / 2))
        self.paramsBox.setStyleSheet("border: 1px solid black;")
        self.editBtn = pyqtWidgets.QPushButton(u'\u270E')
        self.editBtn.setFixedSize(int(config.TREE_STAGE_HEIGHT / 2), int(config.TREE_STAGE_HEIGHT / 2))
        self.deleteBtn = pyqtWidgets.QPushButton('D')
        self.deleteBtn.setFixedSize(int(config.TREE_STAGE_HEIGHT / 2), int(config.TREE_STAGE_HEIGHT / 2))
        self.moveBtn1 = pyqtWidgets.QPushButton(u'\u2191')
        self.moveBtn1.setFixedSize(int(config.TREE_MOVE_BTN_WIDTH), int(config.TREE_STAGE_HEIGHT / 2))
        self.moveBtn2 = pyqtWidgets.QPushButton(u'\u2193')
        self.moveBtn2.setFixedSize(int(config.TREE_MOVE_BTN_WIDTH), int(config.TREE_STAGE_HEIGHT / 2))

        self.topPanel = pyqtWidgets.QWidget()
        self.topPanelLayout = pyqtWidgets.QHBoxLayout()
        self.topPanelLayout.setSpacing(0)
        self.topPanelLayout.setContentsMargins(0, 0, 0, 0)
        self.topPanelLayout.addWidget(self.titleBox)
        self.topPanelLayout.addWidget(self.deleteBtn)
        self.topPanelLayout.addWidget(self.moveBtn1)
        self.topPanel.setLayout(self.topPanelLayout)

        self.bottomPanel = pyqtWidgets.QWidget()
        self.bottomPanelLayout = pyqtWidgets.QHBoxLayout()
        self.bottomPanelLayout.setSpacing(0)
        self.bottomPanelLayout.setContentsMargins(0, 0, 0, 0)
        self.bottomPanelLayout.addWidget(self.paramsBox)
        self.bottomPanelLayout.addWidget(self.editBtn)
        self.bottomPanelLayout.addWidget(self.moveBtn2)
        self.bottomPanel.setLayout(self.bottomPanelLayout)

        self.mainLayout = pyqtWidgets.QVBoxLayout()
        self.mainLayout.setSpacing(0)
        self.mainLayout.setContentsMargins(0, 0, 0, 0)
        self.mainLayout.addWidget(self.topPanel)
        self.mainLayout.addWidget(self.bottomPanel)
        self.setLayout(self.mainLayout)
