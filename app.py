# Импортируем библиотеки
from sys import argv
from time import sleep
from math import sin, cos
from PyQt6 import QtWidgets, QtCore, QtGui
from PyQt6.QtCore import pyqtSignal, QObject
import threading
import serial.tools.list_ports
import design

# Задаём переменные
selectedPort = None
selectedSpeed = 9600
zoom = 0.1
ser = serial.Serial()
points = []


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
        self.rotatelButton.setDisabled(True)
        self.rotaterButton.setDisabled(True)
        self.runButton.setDisabled(True)
        self.updateButton.clicked.connect(self.updatePorts)
        self.rotatelButton.pressed.connect(self.turnl)
        self.rotaterButton.pressed.connect(self.turnr)
        self.runButton.clicked.connect(self.scan)
        self.connectButton.clicked.connect(self.connect)
        self.clearButton.clicked.connect(self.clearOutput)
        self.zoomrButton.clicked.connect(self.zoomr)
        self.zoompButton.clicked.connect(self.zoomp)
        self.zoommButton.clicked.connect(self.zoomm)
        self.updatePorts()  # Обновляем порты
        self.clearOutput()  # Обновляем вывод

    def output(self):
        scene = QtWidgets.QGraphicsScene()
        self.graphicsView.setScene(scene)
        pen = QtGui.QPen(QtCore.Qt.PenStyle.NoPen)
        brush = QtGui.QBrush(QtCore.Qt.GlobalColor.lightGray)

        for i in range(1, 10):
            fig = QtCore.QRectF(QtCore.QPointF((800 * i - 4000) * zoom, -3200 * zoom), QtCore.QSizeF(1, 6400 * zoom))
            scene.addRect(fig, brush=brush, pen=pen)

        for i in range(1, 10):
            fig = QtCore.QRectF(QtCore.QPointF(-3200 * zoom, (800 * i - 4000) * zoom), QtCore.QSizeF(6400 * zoom, 1))
            scene.addRect(fig, brush=brush, pen=pen)

        brush = QtGui.QBrush(QtCore.Qt.GlobalColor.darkGreen)
        fig = QtCore.QRectF(QtCore.QPointF(-7, -8), QtCore.QSizeF(15, 16))
        scene.addEllipse(fig, brush=brush, pen=pen)

        brush = QtGui.QBrush(QtCore.Qt.GlobalColor.darkBlue)
        if len(points) > 0:
            for i in points:
                a = str(i).split('%')
                b = 0.0174533 * float(a[0])
                if float(a[1]) < 5000:
                    x = sin(b) * (float(a[1]) + 30) * zoom
                    y = cos(b) * (float(a[1]) + 30) * zoom
                    fig = QtCore.QRectF(QtCore.QPointF(x - 2, y - 2), QtCore.QSizeF(5, 5))
                    scene.addEllipse(fig, brush=brush, pen=pen)

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
            self.combobox.addItem('Устройства не найдены')
            self.connectButton.setDisabled(True)

    def connect(self, checked):
        global ser
        global selectedPort

        if checked:
            self.updateButton.setDisabled(True)
            selectedPort = self.combobox.currentText()
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
            self.updateButton.setEnabled(True)

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
        self.scanner.progress.connect(self.update_progress)  # Подключаем сигнал прогресса
        self.scanner.finished.connect(self.task_complete)  # Подключаем сигнал окончания
        thread = threading.Thread(target=self.scanner.run)
        thread.start()

    def update_progress(self):
        self.output()

    def task_complete(self):
        self.runButton.setEnabled(True)  # Включаем кнопку
        self.rotatelButton.setEnabled(True)  # Включаем кнопку
        self.rotaterButton.setEnabled(True)  # Включаем кнопку


# Основной скрипт
if __name__ == '__main__':  # Если мы запускаем файл напрямую, а не импортируем, то:
    app = QtWidgets.QApplication(argv)  # Создаём новый экземпляр QApplication
    window = MainWindow()  # Создаём объект окна из класса MainWindow
    window.show()  # Показываем окно
    app.exec()  # Запускаем приложение
