# Form implementation generated from reading ui file '.\design.ui'
#
# Created by: PyQt6 UI code generator 6.9.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(638, 480)
        MainWindow.setMinimumSize(QtCore.QSize(480, 350))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(".\\images/icon.svg"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet("QWidget {\n"
"    background-color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(238, 238, 239);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgba(6, 192, 37, 40);\n"
"}\n"
"\n"
"QPushButton#updateButton {\n"
"    border-top: 1px solid rgb(160, 160, 160);\n"
"    border-bottom: 1px solid rgb(160, 160, 160);\n"
"    border-right: 1px solid rgb(160, 160, 160);\n"
"    border-left: none;\n"
"}\n"
"\n"
"QPushButton#zoommButton {\n"
"    border: 1px solid rgb(160, 160, 160);\n"
"    border-top-left-radius: 4px;\n"
"    border-bottom-left-radius: 4px;\n"
"}\n"
"\n"
"QPushButton#zoomrButton {\n"
"    border-top: 1px solid rgb(160, 160, 160);\n"
"    border-bottom: 1px solid rgb(160, 160, 160);\n"
"}\n"
"\n"
"QPushButton#zoompButton {\n"
"    border: 1px solid rgb(160, 160, 160);\n"
"    border-top-right-radius: 4px;\n"
"    border-bottom-right-radius: 4px;\n"
"}\n"
"\n"
"QPushButton#connectButton {\n"
"    border: 1px solid rgb(160, 160, 160);\n"
"    border-left: none;\n"
"    border-top-right-radius: 4px;\n"
"    border-bottom-right-radius: 4px;\n"
"    icon: url(images/connect.svg);\n"
"}\n"
"\n"
"QPushButton#connectButton:checked {\n"
"    icon: url(images/disconnect.svg);\n"
"    background-color: rgba(6, 192, 37, 40);\n"
"}\n"
"\n"
"QPushButton#runButton, QPushButton#clearButton, QPushButton#menuButton, QPushButton#exportButton,\n"
"QPushButton#resetButton, QPushButton#menuButton {\n"
"    border: 1px solid rgb(160, 160, 160);\n"
"    border-radius: 4px;\n"
"}\n"
"\n"
"QPushButton#clearButton:pressed {\n"
"    background-color: rgb(255, 200, 203);\n"
"}\n"
"\n"
"QPushButton#rotatelButton {\n"
"    border: 1px solid rgb(160, 160, 160);\n"
"    border-top-left-radius: 4px;\n"
"    border-bottom-left-radius: 4px;\n"
"}\n"
"\n"
"QPushButton#rotaterButton {\n"
"    border: 1px solid rgb(160, 160, 160);\n"
"    border-left: none;\n"
"    border-top-right-radius: 4px;\n"
"    border-bottom-right-radius: 4px;\n"
"}\n"
"\n"
"\n"
"QComboBox {\n"
"    background-color: rgb(255, 255, 255);\n"
"    border: 1px solid rgb(160, 160, 160);\n"
"    border-top-left-radius: 4px;\n"
"    border-bottom-left-radius: 4px;\n"
"    padding-left: 9px;    \n"
"    padding-right: 0px;\n"
"    color: rgb(0, 0, 0);\n"
"}\n"
"\n"
"QComboBox:hover {\n"
"    background-color: rgb(243, 243, 243);\n"
"}\n"
"\n"
"QComboBox:on {\n"
"    background-color: rgba(6, 192, 37, 40);\n"
"}\n"
"\n"
"QComboBox::down-arrow:disabled {\n"
"    image: none;\n"
"}\n"
"\n"
"QComboBox::drop-down {\n"
"    border: 0px;\n"
"}\n"
"\n"
"QComboBox::down-arrow {\n"
"    image: url(images/arrow_down.svg);\n"
"    width: 10px;\n"
"    margin-right: 14px;\n"
"}\n"
"\n"
"QComboBox::down-arrow:on {\n"
"    image: url(images/arrow_up.svg);\n"
"    width: 10px;\n"
"    margin-right: 14px;\n"
"}\n"
"\n"
"QComboBox QAbstractItemView {\n"
"    border: none;\n"
"    outline: none;\n"
"    background-color: rgb(255, 255, 255);\n"
"    text-size: 12px;\n"
"    color: rgb(0, 0, 0);\n"
"}\n"
"\n"
"QComboBox QListView {\n"
"    border: none;\n"
"}\n"
"\n"
"QComboBox QAbstractItemView::item {\n"
"    border: none;\n"
"    outline: none;\n"
"    height: 30px;\n"
"    text-size: 12px;\n"
"    color: rgb(0, 0, 0);\n"
"    border-radius: 4px;\n"
"    margin: 4px;\n"
"    padding-left: 8px;\n"
"    background-color: transparent;\n"
"}\n"
"\n"
"QComboBox QAbstractItemView::item:hover{\n"
"    background-color:  rgb(238, 238, 239);\n"
"}\n"
"\n"
"\n"
"QScrollBar {\n"
"    background-color: rgb(238, 240, 240);\n"
"    border: none;\n"
"}\n"
"\n"
"QComboBox QScrollBar {\n"
"    background-color: rgba(255, 255, 255, 0);\n"
"}\n"
"\n"
"QScrollBar:vertical {\n"
"    width: 10px;\n"
"}\n"
"\n"
"QScrollBar::add-line, QScrollBar::sub-line {\n"
"    height: 0px;\n"
"}\n"
"\n"
"QScrollBar::add-page, QScrollBar::sub-page {\n"
"    background: none;\n"
"    border: none;\n"
"}\n"
"\n"
"QScrollBar::handle {\n"
"    background-color: rgba(183, 183, 184, 180);\n"
"    border-radius: 3px;\n"
"    margin: 2px;\n"
"}\n"
"\n"
"QScrollBar::handle:hover {\n"
"    background-color: rgba(183, 183, 184, 255);\n"
"}")
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.widget = QtWidgets.QWidget(parent=self.centralwidget)
        self.widget.setObjectName("widget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout.setContentsMargins(5, 5, 5, 5)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.comboBox = QtWidgets.QComboBox(parent=self.widget)
        self.comboBox.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBox.sizePolicy().hasHeightForWidth())
        self.comboBox.setSizePolicy(sizePolicy)
        self.comboBox.setMinimumSize(QtCore.QSize(0, 30))
        self.comboBox.setMaximumSize(QtCore.QSize(200, 30))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.comboBox.setFont(font)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.horizontalLayout.addWidget(self.comboBox)
        self.updateButton = QtWidgets.QPushButton(parent=self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.updateButton.sizePolicy().hasHeightForWidth())
        self.updateButton.setSizePolicy(sizePolicy)
        self.updateButton.setMinimumSize(QtCore.QSize(29, 30))
        self.updateButton.setMaximumSize(QtCore.QSize(29, 30))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(".\\images/update.svg"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.updateButton.setIcon(icon1)
        self.updateButton.setIconSize(QtCore.QSize(16, 16))
        self.updateButton.setObjectName("updateButton")
        self.horizontalLayout.addWidget(self.updateButton)
        self.connectButton = QtWidgets.QPushButton(parent=self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.connectButton.sizePolicy().hasHeightForWidth())
        self.connectButton.setSizePolicy(sizePolicy)
        self.connectButton.setMinimumSize(QtCore.QSize(29, 30))
        self.connectButton.setMaximumSize(QtCore.QSize(29, 30))
        self.connectButton.setIconSize(QtCore.QSize(16, 16))
        self.connectButton.setCheckable(True)
        self.connectButton.setObjectName("connectButton")
        self.horizontalLayout.addWidget(self.connectButton)
        spacerItem = QtWidgets.QSpacerItem(5, 20, QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.rotatelButton = QtWidgets.QPushButton(parent=self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.rotatelButton.sizePolicy().hasHeightForWidth())
        self.rotatelButton.setSizePolicy(sizePolicy)
        self.rotatelButton.setMinimumSize(QtCore.QSize(30, 30))
        self.rotatelButton.setMaximumSize(QtCore.QSize(30, 30))
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(".\\images/rotate_l.svg"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.rotatelButton.setIcon(icon2)
        self.rotatelButton.setIconSize(QtCore.QSize(16, 16))
        self.rotatelButton.setObjectName("rotatelButton")
        self.horizontalLayout.addWidget(self.rotatelButton)
        self.rotaterButton = QtWidgets.QPushButton(parent=self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.rotaterButton.sizePolicy().hasHeightForWidth())
        self.rotaterButton.setSizePolicy(sizePolicy)
        self.rotaterButton.setMinimumSize(QtCore.QSize(29, 30))
        self.rotaterButton.setMaximumSize(QtCore.QSize(30, 30))
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(".\\images/rotate_r.svg"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.rotaterButton.setIcon(icon3)
        self.rotaterButton.setIconSize(QtCore.QSize(16, 16))
        self.rotaterButton.setObjectName("rotaterButton")
        self.horizontalLayout.addWidget(self.rotaterButton)
        spacerItem1 = QtWidgets.QSpacerItem(5, 20, QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.runButton = QtWidgets.QPushButton(parent=self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.runButton.sizePolicy().hasHeightForWidth())
        self.runButton.setSizePolicy(sizePolicy)
        self.runButton.setMinimumSize(QtCore.QSize(30, 30))
        self.runButton.setMaximumSize(QtCore.QSize(30, 30))
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(".\\images/start.svg"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.runButton.setIcon(icon4)
        self.runButton.setIconSize(QtCore.QSize(16, 16))
        self.runButton.setObjectName("runButton")
        self.horizontalLayout.addWidget(self.runButton)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.resetButton = QtWidgets.QPushButton(parent=self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.resetButton.sizePolicy().hasHeightForWidth())
        self.resetButton.setSizePolicy(sizePolicy)
        self.resetButton.setMinimumSize(QtCore.QSize(30, 30))
        self.resetButton.setMaximumSize(QtCore.QSize(30, 30))
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(".\\images/reset.svg"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.resetButton.setIcon(icon5)
        self.resetButton.setIconSize(QtCore.QSize(16, 16))
        self.resetButton.setObjectName("resetButton")
        self.horizontalLayout.addWidget(self.resetButton)
        spacerItem3 = QtWidgets.QSpacerItem(5, 20, QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout.addItem(spacerItem3)
        self.exportButton = QtWidgets.QPushButton(parent=self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.exportButton.sizePolicy().hasHeightForWidth())
        self.exportButton.setSizePolicy(sizePolicy)
        self.exportButton.setMinimumSize(QtCore.QSize(30, 30))
        self.exportButton.setMaximumSize(QtCore.QSize(30, 30))
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(".\\images/export.svg"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.exportButton.setIcon(icon6)
        self.exportButton.setIconSize(QtCore.QSize(16, 16))
        self.exportButton.setObjectName("exportButton")
        self.horizontalLayout.addWidget(self.exportButton)
        spacerItem4 = QtWidgets.QSpacerItem(5, 20, QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout.addItem(spacerItem4)
        self.clearButton = QtWidgets.QPushButton(parent=self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.clearButton.sizePolicy().hasHeightForWidth())
        self.clearButton.setSizePolicy(sizePolicy)
        self.clearButton.setMinimumSize(QtCore.QSize(30, 30))
        self.clearButton.setMaximumSize(QtCore.QSize(30, 30))
        self.clearButton.setStyleSheet("")
        self.clearButton.setText("")
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(".\\images/clear.svg"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.clearButton.setIcon(icon7)
        self.clearButton.setIconSize(QtCore.QSize(16, 16))
        self.clearButton.setObjectName("clearButton")
        self.horizontalLayout.addWidget(self.clearButton)
        self.verticalLayout.addWidget(self.widget)
        self.graphWidget = PlotWidget(parent=self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.graphWidget.sizePolicy().hasHeightForWidth())
        self.graphWidget.setSizePolicy(sizePolicy)
        self.graphWidget.setMinimumSize(QtCore.QSize(427, 300))
        self.graphWidget.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.CrossCursor))
        self.graphWidget.setObjectName("graphWidget")
        self.verticalLayout.addWidget(self.graphWidget)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Locator Viewer"))
        self.comboBox.setToolTip(_translate("MainWindow", "Порт устройства"))
        self.comboBox.setItemText(0, _translate("MainWindow", "Устройства не найдены"))
        self.updateButton.setToolTip(_translate("MainWindow", "Обновить список портов (ALT+R)"))
        self.updateButton.setShortcut(_translate("MainWindow", "Alt+R"))
        self.connectButton.setToolTip(_translate("MainWindow", "Подключиться (ALT+C)"))
        self.connectButton.setShortcut(_translate("MainWindow", "Alt+C"))
        self.rotatelButton.setToolTip(_translate("MainWindow", "Повернуть влево (LEFT)"))
        self.rotatelButton.setShortcut(_translate("MainWindow", "Left"))
        self.rotaterButton.setToolTip(_translate("MainWindow", "Повернуть вправо (RIGHT)"))
        self.rotaterButton.setShortcut(_translate("MainWindow", "Right"))
        self.runButton.setToolTip(_translate("MainWindow", "Начать сканирование (ENTER)"))
        self.runButton.setShortcut(_translate("MainWindow", "Return"))
        self.resetButton.setToolTip(_translate("MainWindow", "Сбросить масштаб (CTRL+M)"))
        self.resetButton.setShortcut(_translate("MainWindow", "Ctrl+M"))
        self.exportButton.setToolTip(_translate("MainWindow", "Сохранить график (CTRL+S)"))
        self.exportButton.setShortcut(_translate("MainWindow", "Ctrl+S"))
        self.clearButton.setToolTip(_translate("MainWindow", "Очистить график (CTRL+D)"))
        self.clearButton.setShortcut(_translate("MainWindow", "Ctrl+D"))
from pyqtgraph import PlotWidget
