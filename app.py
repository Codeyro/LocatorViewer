# Импортируем библиотеки
from math import sin, cos
from sys import argv
from time import sleep
import threading
import serial.tools.list_ports
from PyQt6 import QtWidgets, QtCore, QtGui
from PyQt6.QtCore import pyqtSignal, QObject
import design

# Задаём переменные
ser = serial.Serial()
points = []
selectedPort = None
selectedSpeed = 9600
zoom = 0.1


# Создаём классы
class Scanner(QObject):
    finished = pyqtSignal()
    progress = pyqtSignal()

    def __init__(self):
        super().__init__()

    def run(self):
        global ser
        global points

        points.clear()
        ser.write(b"w")
        read = ser.readline().decode().strip()
        while read != 'e':
            points.append(read)
            read = ser.readline().decode().strip()
            self.progress.emit()
        self.finished.emit()


class MainWindow(QtWidgets.QMainWindow, design.Ui_MainWindow):
    def __init__(self):  # Функция для доступа к переменным, методам и т.д. в файле design.py
        super().__init__()
        self.setupUi(self)  # Инициализация дизайна
        self.scanner = None
        self.updateButton.clicked.connect(self.updatePorts)
        self.combobox.currentTextChanged.connect(self.selectPort)
        self.rotatelButton.setDisabled(True)
        self.rotaterButton.setDisabled(True)
        self.runButton.setDisabled(True)
        self.rotatelButton.pressed.connect(self.turnl)
        self.rotaterButton.pressed.connect(self.turnr)
        self.runButton.clicked.connect(self.scan)
        self.connectButton.clicked.connect(self.connect)
        self.clearButton.clicked.connect(self.clearOutput)
        self.zoomrButton.clicked.connect(self.zoomr)
        self.zoompButton.clicked.connect(self.zoomp)
        self.zoommButton.clicked.connect(self.zoomm)
        self.updatePorts()  # Обновляем порты
        self.output()
        points.clear()

    def output(self):
        scene = QtWidgets.QGraphicsScene()
        self.graphicsView.setScene(scene)
        pen = QtGui.QPen(QtCore.Qt.PenStyle.NoPen)
        brush = QtGui.QBrush(QtCore.Qt.GlobalColor.lightGray)

        i = 1
        while i < 10:
            rect = QtCore.QRectF(QtCore.QPointF((800 * i - 4000) * zoom, -3200 * zoom), QtCore.QSizeF(1, 6400 * zoom))
            scene.addRect(rect, brush=brush, pen=pen)
            i = i + 1

        i = 1
        while i < 10:
            rect = QtCore.QRectF(QtCore.QPointF(-3200 * zoom, (800 * i - 4000) * zoom), QtCore.QSizeF(6400 * zoom, 1))
            scene.addRect(rect, brush=brush, pen=pen)
            i = i + 1

        brush = QtGui.QBrush(QtCore.Qt.GlobalColor.darkGray)
        rect = QtCore.QRectF(QtCore.QPointF((800 * 5 - 4000) * zoom, -3200 * zoom), QtCore.QSizeF(1, 6400 * zoom))
        scene.addRect(rect, brush=brush, pen=pen)
        rect = QtCore.QRectF(QtCore.QPointF((800 * 1 - 4000) * zoom, -3200 * zoom), QtCore.QSizeF(1, 6400 * zoom))
        scene.addRect(rect, brush=brush, pen=pen)
        rect = QtCore.QRectF(QtCore.QPointF((800 * 9 - 4000) * zoom, -3200 * zoom), QtCore.QSizeF(1, 6400 * zoom))
        scene.addRect(rect, brush=brush, pen=pen)
        rect = QtCore.QRectF(QtCore.QPointF(-3200 * zoom, (800 * 5 - 4000) * zoom), QtCore.QSizeF(6400 * zoom, 1))
        scene.addRect(rect, brush=brush, pen=pen)
        rect = QtCore.QRectF(QtCore.QPointF(-3200 * zoom, (800 * 1 - 4000) * zoom), QtCore.QSizeF(6400 * zoom, 1))
        scene.addRect(rect, brush=brush, pen=pen)
        rect = QtCore.QRectF(QtCore.QPointF(-3200 * zoom, (800 * 9 - 4000) * zoom), QtCore.QSizeF(6400 * zoom, 1))
        scene.addRect(rect, brush=brush, pen=pen)

        brush = QtGui.QBrush(QtCore.Qt.GlobalColor.darkGreen)
        rect = QtCore.QRectF(QtCore.QPointF(-5, -6), QtCore.QSizeF(11, 12))
        scene.addEllipse(rect, brush=brush, pen=pen)

        brush = QtGui.QBrush(QtCore.Qt.GlobalColor.darkBlue)
        if len(points) > 1:
            i = 1
            while i != len(points):
                a = str(points[i])
                b = a.split('%')
                if float(b[1]) < int(5000):
                    x = sin(0.0174533 * float(b[0])) * float(b[1]) * zoom
                    y = cos(0.0174533 * float(b[0])) * float(b[1]) * zoom
                    rect = QtCore.QRectF(QtCore.QPointF(x, y), QtCore.QSizeF(3, 3))
                    scene.addRect(rect, brush=brush, pen=pen)
                i = i + 1

    def updatePorts(self):
        global selectedPort
        ports = serial.tools.list_ports.comports()
        portsList = []

        for port in ports:
            if port.serial_number is not None:
                portsList.append(port.name)

        self.combobox.clear()

        if len(portsList) > 0:
            self.combobox.setEnabled(True)
            self.combobox.addItems(portsList)
            selectedPort = self.combobox.currentText()
            self.connectButton.setEnabled(True)
        else:
            self.combobox.setDisabled(True)
            self.combobox.addItem('Портов не найдено')
            self.connectButton.setDisabled(True)

    def selectPort(self):
        global selectedPort
        selectedPort = self

    def connect(self, checked):
        global ser
        global selectedPort
        if checked:
            ser = serial.Serial(selectedPort, baudrate=selectedSpeed)
            self.combobox.setDisabled(True)
            sleep(2)
            self.rotatelButton.setEnabled(True)
            self.rotaterButton.setEnabled(True)
            self.runButton.setEnabled(True)
        else:
            ser.close()
            self.rotatelButton.setDisabled(True)
            self.rotaterButton.setDisabled(True)
            self.runButton.setDisabled(True)
            self.combobox.setEnabled(True)

    @staticmethod
    def turnr():
        global ser
        ser.write(b"r")
        ser.write(b"r")
        ser.write(b" ")

    @staticmethod
    def turnl():
        global ser
        ser.write(b"l")
        ser.write(b"l")
        ser.write(b" ")

    def zoomr(self):
        global zoom
        zoom = 0.1
        self.output()
        self.zoommButton.setEnabled(True)

    def zoomp(self):
        global zoom
        zoom = zoom + 0.05
        self.output()
        self.zoommButton.setEnabled(True)

    def zoomm(self):
        global zoom
        if zoom > 0.09:
            zoom = zoom - 0.05
            self.output()
            if zoom < 0.09:
                self.zoommButton.setDisabled(True)

    def clearOutput(self):
        points.clear()
        self.output()

    def scan(self):
        self.runButton.setDisabled(True)  # Выключаем кнопку
        self.rotatelButton.setDisabled(True)  # Выключаем кнопку
        self.rotaterButton.setDisabled(True)  # Выключаем кнопку

        self.scanner = Scanner()  # Create a scanner thread
        self.scanner.progress.connect(self.update_progress)  # Connect the progress signal
        self.scanner.finished.connect(self.task_complete)  # Connect the finished signal
        thread = threading.Thread(target=self.scanner.run)
        thread.start()

    def update_progress(self):
        self.output()

    def task_complete(self):
        self.runButton.setEnabled(True)  # Включаем кнопку
        self.rotatelButton.setEnabled(True)  # Включаем кнопку
        self.rotaterButton.setEnabled(True)  # Включаем кнопку


# Основная программа
if __name__ == '__main__':  # Если мы запускаем файл напрямую, а не импортируем, то:
    app = QtWidgets.QApplication(argv)  # Создаём новый экземпляр QApplication
    window = MainWindow()  # Создаём объект окна из класса MainWindow
    window.show()  # Показываем окно
    app.exec()  # Запускаем приложение
