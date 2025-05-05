import threading
from math import sin, cos
from sys import argv
from time import sleep

import pyqtgraph as pg
import pyqtgraph.exporters
import serial.tools.list_ports
from PyQt6.QtWidgets import QMainWindow, QFileDialog, QApplication
from PyQt6.QtCore import pyqtSignal, QObject

import design


# Задаём переменные
selectedPort = None
selectedSpeed = 9600
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
            try:
                read = ser.readline().decode().strip()
            except serial.serialutil.SerialException:
                self.finished.emit()
                break
            self.progress.emit()
        self.finished.emit()


class MainWindow(QMainWindow, design.Ui_MainWindow):
    def __init__(self):  # Функция для доступа к переменным, методам и т.д. в файле design.py
        super().__init__()
        self.setupUi(self)  # Инициализация дизайна
        self.scanner = None
        self.graphWidget.setBackground('#eef0f0')
        self.graphWidget.showGrid(x=True, y=True)
        self.graphWidget.hideButtons()
        self.graphWidget.setAspectLocked()
        self.rotatelButton.setDisabled(True)
        self.rotaterButton.setDisabled(True)
        self.runButton.setDisabled(True)
        self.updateButton.clicked.connect(self.updatePorts)
        self.rotaterButton.pressed.connect(self.turnRight)
        self.rotatelButton.pressed.connect(self.turnLeft)
        self.runButton.clicked.connect(self.scan)
        self.connectButton.clicked.connect(self.connect)
        self.clearButton.clicked.connect(self.clearOutput)
        self.exportButton.clicked.connect(self.export)
        self.resetButton.clicked.connect(lambda: self.graphWidget.enableAutoRange())
        self.updatePorts()  # Обновляем порты
        self.clearOutput()  # Очищаем вывод

    def output(self):
        x = []
        y = []
        if len(points) > 0:
            for i in points:
                a = i.split(',')
                b = 0.0174533 * float(a[0])
                if float(a[1]) < 5000:
                    x.append(sin(b) * float(a[1]))
                    y.append(cos(b) * float(a[1]))
        pen = pg.mkPen(color=(10, 50, 255), width=3)
        self.graphWidget.clear()
        self.graphWidget.plot(x, y, pen=pen, symbol="o", symbolSize=10, symbolBrush="b", symbolPen=None)
        self.graphWidget.plot([0], [0], pen=pen, symbol="o", symbolSize=16, symbolBrush="#00aa22", symbolPen=None)

    def updatePorts(self):
        global selectedPort
        ports = serial.tools.list_ports.comports()
        ports_list = []

        for port in ports:
            if port.serial_number is not None:
                ports_list.append(port.name)

        self.comboBox.clear()

        if len(ports_list) > 0:
            self.comboBox.setEnabled(True)
            self.comboBox.addItems(ports_list)
            selectedPort = self.comboBox.currentText()
            self.connectButton.setEnabled(True)
        else:
            self.comboBox.setDisabled(True)
            self.comboBox.addItem('Устройства не найдены')
            self.connectButton.setDisabled(True)

    def connect(self, checked):
        global ser
        global selectedPort
        self.updatePorts()

        if checked:
            try:
                selectedPort = self.comboBox.currentText()
                ser = serial.Serial(selectedPort, baudrate=selectedSpeed)
            except serial.serialutil.SerialException:
                self.disconnect()
            else:
                self.updateButton.setDisabled(True)
                self.comboBox.setDisabled(True)
                sleep(2)
                self.rotatelButton.setEnabled(True)
                self.rotaterButton.setEnabled(True)
                self.runButton.setEnabled(True)
                self.connectButton.setToolTip('Отключиться')
        else:
            self.disconnect()

    def disconnect(self):
        global ser
        ser.close()
        self.rotatelButton.setDisabled(True)
        self.rotaterButton.setDisabled(True)
        self.runButton.setDisabled(True)
        self.comboBox.setEnabled(True)
        self.updateButton.setEnabled(True)
        self.connectButton.setChecked(False)
        self.connectButton.setToolTip('Подключиться')
        self.updatePorts()

    def turnRight(self):
        global ser
        try:
            ser.write(b"r")
            ser.write(b"r")
            ser.write(b" ")
        except serial.serialutil.SerialException:
            self.disconnect()

    def turnLeft(self):
        global ser
        try:
            ser.write(b"l")
            ser.write(b"l")
            ser.write(b" ")
        except serial.serialutil.SerialException:
            self.disconnect()

    def clearOutput(self):
        global points
        points = []
        self.output()

    def export(self):
        file = QFileDialog.getSaveFileName(caption='Сохранение графика', filter='(*.png)')
        if file:
            exporter = pg.exporters.ImageExporter(self.graphWidget.plotItem)
            exporter.export(file[0])  # Экспорт в файл

    def scan(self):
        try:
            ser.read_all()
        except serial.serialutil.SerialException:
            self.disconnect()
        else:
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
        try:
            ser.read_all()
        except serial.serialutil.SerialException:
            self.disconnect()
        else:
            self.runButton.setEnabled(True)  # Включаем кнопку
            self.rotatelButton.setEnabled(True)  # Включаем кнопку
            self.rotaterButton.setEnabled(True)  # Включаем кнопку


if __name__ == '__main__':  # Если мы запускаем файл напрямую, а не импортируем, то:
    app = QApplication(argv)  # Создаём новый экземпляр QApplication
    window = MainWindow()  # Создаём объект окна из класса MainWindow
    window.show()  # Показываем окно
    app.exec()  # Запускаем приложение
