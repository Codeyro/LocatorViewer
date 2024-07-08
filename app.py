# Импортируем библиотеки
from sys import argv
from time import sleep
from math import sin, cos
from PyQt6 import QtWidgets
from PyQt6.QtCore import pyqtSignal, QObject
import threading
import pyqtgraph as pg
import serial.tools.list_ports
import design

# Задаём переменные
selectedPort = None
selectedSpeed = 9600
ser = serial.Serial()
points = []
x = []
y = []


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
        self.graphWidget.setBackground('#eef0f0')
        self.graphWidget.showGrid(x=True, y=True)
        self.rotatelButton.setDisabled(True)
        self.rotaterButton.setDisabled(True)
        self.runButton.setDisabled(True)
        self.updateButton.clicked.connect(self.updatePorts)
        self.rotatelButton.pressed.connect(self.turnl)
        self.rotaterButton.pressed.connect(self.turnr)
        self.runButton.clicked.connect(self.scan)
        self.connectButton.clicked.connect(self.connect)
        self.clearButton.clicked.connect(self.clearOutput)
        self.updatePorts()  # Обновляем порты
        self.clearOutput()  # Очищаем вывод

    def output(self):
        global x, y
        x = []
        y = []
        if len(points) > 0:
            for i in points:
                a = str(i).split('%')
                b = 0.0174533 * float(a[0])
                if float(a[1]) < 5000:
                    x.append(sin(b) * (float(a[1]) + 30))
                    y.append(cos(b) * (float(a[1]) + 30))
        pen = pg.mkPen(color=(10, 50, 255), width=3)
        self.graphWidget.clear()
        self.graphWidget.plot(x, y, pen=pen, symbol="o", symbolSize=10, symbolBrush="b", symbolPen=None)
        self.graphWidget.plot([0], [0], pen=pen, symbol="o", symbolSize=16, symbolBrush="#00aa22", symbolPen=None)

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

    def clearOutput(self):
        global x, y
        x, y = [], []
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
