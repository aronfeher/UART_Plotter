
# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.9.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import helpwindow as HW
import serial
import serial.tools.list_ports
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
import matplotlib.pyplot as plt
import sys
from threading import Thread
import time
import numpy as np
from collections import deque
import scipy.fftpack



class Ui_MainWindow(object):

    is_connected = False
    is_started = False
    plot_mode = 1
    custom_i = 0

    rec_data1 = []
    rec_data2 = []

    send_packet = bytearray([0xF1, 0x05, 0x00, 0x00, 0xF3, 0x0D, 0x0A])
    receive_packet = bytearray([0xF2, 0x07, 0xFF, 0xFF, 0xFF, 0xFF, 0xF3, 0x0D, 0x0A])


    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(843, 620)
        MainWindow.setMinimumSize(QtCore.QSize(840, 620))
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setObjectName("centralWidget")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.centralWidget)
        self.gridLayout_3.setContentsMargins(11, 11, 11, 11)
        self.gridLayout_3.setSpacing(6)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.controlsLayout = QtWidgets.QVBoxLayout()
        self.controlsLayout.setSpacing(6)
        self.controlsLayout.setObjectName("controlsLayout")
        self.PortControlsBox = QtWidgets.QGroupBox(self.centralWidget)
        self.PortControlsBox.setFlat(False)
        self.PortControlsBox.setCheckable(False)
        self.PortControlsBox.setObjectName("PortControlsBox")
        self.gridLayout = QtWidgets.QGridLayout(self.PortControlsBox)
        self.gridLayout.setContentsMargins(11, 11, 11, 11)
        self.gridLayout.setSpacing(6)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setSpacing(6)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSpacing(6)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.labelPort = QtWidgets.QLabel(self.PortControlsBox)
        self.labelPort.setMaximumSize(QtCore.QSize(50, 16777215))
        self.labelPort.setObjectName("labelPort")
        self.horizontalLayout.addWidget(self.labelPort)
        self.comboPort = QtWidgets.QComboBox(self.PortControlsBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboPort.sizePolicy().hasHeightForWidth())
        self.comboPort.setSizePolicy(sizePolicy)
        self.comboPort.setMinimumSize(QtCore.QSize(69, 0))
        self.comboPort.setMaximumSize(QtCore.QSize(69, 16777215))
        self.comboPort.setObjectName("comboPort")
        self.horizontalLayout.addWidget(self.comboPort)
        self.verticalLayout_3.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setSpacing(6)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.labelBaud = QtWidgets.QLabel(self.PortControlsBox)
        self.labelBaud.setMaximumSize(QtCore.QSize(50, 16777215))
        self.labelBaud.setObjectName("labelBaud")
        self.horizontalLayout_2.addWidget(self.labelBaud)
        self.comboBaud = QtWidgets.QComboBox(self.PortControlsBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBaud.sizePolicy().hasHeightForWidth())
        self.comboBaud.setSizePolicy(sizePolicy)
        self.comboBaud.setMinimumSize(QtCore.QSize(69, 0))
        self.comboBaud.setMaximumSize(QtCore.QSize(69, 16777215))
        self.comboBaud.setEditable(False)
        self.comboBaud.setObjectName("comboBaud")
        self.horizontalLayout_2.addWidget(self.comboBaud)
        self.verticalLayout_3.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setSpacing(6)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.labelData = QtWidgets.QLabel(self.PortControlsBox)
        self.labelData.setMaximumSize(QtCore.QSize(50, 16777215))
        self.labelData.setObjectName("labelData")
        self.horizontalLayout_3.addWidget(self.labelData)
        self.comboData = QtWidgets.QComboBox(self.PortControlsBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboData.sizePolicy().hasHeightForWidth())
        self.comboData.setSizePolicy(sizePolicy)
        self.comboData.setMinimumSize(QtCore.QSize(69, 0))
        self.comboData.setMaximumSize(QtCore.QSize(69, 16777215))
        self.comboData.setObjectName("comboData")
        self.horizontalLayout_3.addWidget(self.comboData)
        self.verticalLayout_3.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setSpacing(6)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.labelParity = QtWidgets.QLabel(self.PortControlsBox)
        self.labelParity.setMaximumSize(QtCore.QSize(50, 16777215))
        self.labelParity.setObjectName("labelParity")
        self.horizontalLayout_4.addWidget(self.labelParity)
        self.comboParity = QtWidgets.QComboBox(self.PortControlsBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboParity.sizePolicy().hasHeightForWidth())
        self.comboParity.setSizePolicy(sizePolicy)
        self.comboParity.setMinimumSize(QtCore.QSize(69, 0))
        self.comboParity.setMaximumSize(QtCore.QSize(69, 16777215))
        self.comboParity.setObjectName("comboParity")
        self.horizontalLayout_4.addWidget(self.comboParity)
        self.verticalLayout_3.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setSpacing(6)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.labelStop = QtWidgets.QLabel(self.PortControlsBox)
        self.labelStop.setMaximumSize(QtCore.QSize(50, 16777215))
        self.labelStop.setObjectName("labelStop")
        self.horizontalLayout_5.addWidget(self.labelStop)
        self.comboStop = QtWidgets.QComboBox(self.PortControlsBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboStop.sizePolicy().hasHeightForWidth())
        self.comboStop.setSizePolicy(sizePolicy)
        self.comboStop.setMinimumSize(QtCore.QSize(69, 0))
        self.comboStop.setMaximumSize(QtCore.QSize(69, 16777215))
        self.comboStop.setObjectName("comboStop")
        self.horizontalLayout_5.addWidget(self.comboStop)
        self.verticalLayout_3.addLayout(self.horizontalLayout_5)
        self.connectButton = QtWidgets.QPushButton(self.PortControlsBox)
        self.connectButton.setMinimumSize(QtCore.QSize(0, 0))
        self.connectButton.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.connectButton.setObjectName("connectButton")
        self.verticalLayout_3.addWidget(self.connectButton)
        self.gridLayout.addLayout(self.verticalLayout_3, 0, 0, 1, 1)
        self.controlsLayout.addWidget(self.PortControlsBox)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.controlsLayout.addItem(spacerItem)
        self.PlotControlsBox = QtWidgets.QGroupBox(self.centralWidget)
        self.PlotControlsBox.setObjectName("PlotControlsBox")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.PlotControlsBox)
        self.gridLayout_2.setContentsMargins(11, 11, 11, 11)
        self.gridLayout_2.setSpacing(6)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.plotControlsLayout = QtWidgets.QVBoxLayout()
        self.plotControlsLayout.setSpacing(6)
        self.plotControlsLayout.setObjectName("plotControlsLayout")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setSpacing(6)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.labelAxes = QtWidgets.QLabel(self.PlotControlsBox)
        self.labelAxes.setMinimumSize(QtCore.QSize(0, 0))
        self.labelAxes.setMaximumSize(QtCore.QSize(50, 16777215))
        self.labelAxes.setObjectName("labelAxes")
        self.horizontalLayout_6.addWidget(self.labelAxes)
        self.comboAxes = QtWidgets.QComboBox(self.PlotControlsBox)
        self.comboAxes.setMinimumSize(QtCore.QSize(69, 0))
        self.comboAxes.setMaximumSize(QtCore.QSize(69, 16777215))
        self.comboAxes.setObjectName("comboAxes")
        self.horizontalLayout_6.addWidget(self.comboAxes)
        self.plotControlsLayout.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setSpacing(6)
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.pointsLabel = QtWidgets.QLabel(self.PlotControlsBox)
        self.pointsLabel.setMinimumSize(QtCore.QSize(50, 0))
        self.pointsLabel.setMaximumSize(QtCore.QSize(50, 16777215))
        self.pointsLabel.setObjectName("pointsLabel")
        self.horizontalLayout_10.addWidget(self.pointsLabel)
        self.spinPoints = QtWidgets.QSpinBox(self.PlotControlsBox)
        self.spinPoints.setMinimumSize(QtCore.QSize(69, 0))
        self.spinPoints.setMaximumSize(QtCore.QSize(69, 16777215))
        self.spinPoints.setMinimum(10)
        self.spinPoints.setMaximum(10000)
        self.spinPoints.setProperty("value", 1024)
        self.spinPoints.setObjectName("spinPoints")
        self.horizontalLayout_10.addWidget(self.spinPoints)
        self.plotControlsLayout.addLayout(self.horizontalLayout_10)
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_11.setSpacing(6)
        self.horizontalLayout_11.setObjectName("horizontalLayout_10")
        self.freqLabel = QtWidgets.QLabel(self.PlotControlsBox)
        self.freqLabel.setMinimumSize(QtCore.QSize(50, 0))
        self.freqLabel.setMaximumSize(QtCore.QSize(50, 16777215))
        self.freqLabel.setObjectName("freqLabel")
        self.horizontalLayout_11.addWidget(self.freqLabel)
        self.spinFreqs = QtWidgets.QDoubleSpinBox(self.PlotControlsBox)
        self.spinFreqs.setMinimumSize(QtCore.QSize(69, 0))
        self.spinFreqs.setMaximumSize(QtCore.QSize(69, 16777215))
        self.spinFreqs.setMinimum(0.01)
        self.spinFreqs.setMaximum(1000)
        self.spinFreqs.setProperty("value", 10.00)
        self.spinFreqs.setObjectName("spinFreqs")
        self.horizontalLayout_11.addWidget(self.spinFreqs)
        self.plotControlsLayout.addLayout(self.horizontalLayout_11)
        self.saveJPGButton = QtWidgets.QPushButton(self.PlotControlsBox)
        self.saveJPGButton.setObjectName("saveJPGButton")
        self.plotControlsLayout.addWidget(self.saveJPGButton)
        self.startPlotButton = QtWidgets.QPushButton(self.PlotControlsBox)
        self.startPlotButton.setMinimumSize(QtCore.QSize(0, 0))
        self.startPlotButton.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.startPlotButton.setObjectName("startPlotButton")
        self.plotControlsLayout.addWidget(self.startPlotButton)
        self.gridLayout_2.addLayout(self.plotControlsLayout, 0, 0, 1, 1)
        self.controlsLayout.addWidget(self.PlotControlsBox)
        self.gridLayout_3.addLayout(self.controlsLayout, 0, 0, 1, 1)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setSpacing(6)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        spacerItem1 = QtWidgets.QSpacerItem(675, 1, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout_2.addItem(spacerItem1)
        self.gridLayout_3.addLayout(self.verticalLayout_2, 0, 1, 1, 1)
        MainWindow.setCentralWidget(self.centralWidget)
        self.statusBar = QtWidgets.QStatusBar(MainWindow)
        self.statusBar.setObjectName("statusBar")
        MainWindow.setStatusBar(self.statusBar)
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 843, 21))
        self.menuBar.setObjectName("menuBar")
        self.menuHelo = QtWidgets.QMenu(self.menuBar)
        self.menuHelo.setObjectName("menuHelo")
        MainWindow.setMenuBar(self.menuBar)
        self.actionHow_to_use = QtWidgets.QAction(MainWindow)
        self.actionHow_to_use.setObjectName("actionHow_to_use")
        self.menuHelo.addAction(self.actionHow_to_use)
        self.menuBar.addAction(self.menuHelo.menuAction())

        # User code section starts here

        self.comboAxes.setCurrentIndex(-1)
        self.comboAxes.blockSignals(False)
        self.comboAxes.activated.connect(self.plotType)


        self.figure1 = plt.figure()
        self.canvas1 = FigureCanvas(self.figure1)
        self.verticalLayout_2.addWidget(self.canvas1)


        self.axes = plt.gca()
        self.axes.set_xlim([0, self.spinPoints.value()])
        self.axes.set_autoscale_on(False)
        self.axes.set_xticks(np.arange(0, 1024, 100))

        self.figure2 = plt.figure()
        self.canvas2 = FigureCanvas(self.figure2)
        self.verticalLayout_2.addWidget(self.canvas2)

        self.axes = plt.gca()
        self.axes.set_xlim([0, self.spinPoints.value()])
        self.axes.set_autoscale_on(False)
        self.axes.set_xticks(np.arange(0, 1024, 100))

        self.actionHow_to_use.triggered.connect(self.openHelp)

        self.HelpWindow = QtWidgets.QDialog()
        self.ui = HW.Ui_HelpWindow()
        self.ui.setupUi(self.HelpWindow)

        self.comboAxes.addItems(["Raw", "Processed", "Both"])
        self.comboData.addItems(["8", "9"])
        self.comboParity.addItems(["None", "Even", "Odd"])
        self.comboStop.addItems(["1", "2"])
        self.comboBaud.addItems(["9600", "19200", "38400", "57600", "115200"])

        self.comboPort.addItems(Ui_MainWindow.serial_ports())

        self.connectButton.clicked.connect(self._connect)

        self.startPlotButton.clicked.connect(self._start)

        self.len = self.spinPoints.value()

        Ui_MainWindow.rec_data1 = deque([0]*self.len, self.len)
        Ui_MainWindow.rec_data2 = deque([0]*self.len, self.len)

        self.freq = self.spinFreqs.value()

        self.spinFreqs.valueChanged.connect(self._change_freq)
        self.spinPoints.valueChanged.connect(self._change_sample_len)


        self.work_thread = Thread(target=self.plot_thread)
        self.work_thread.start()

        #self.resetPlotButton.clicked.connect(self._reset)
        self.saveJPGButton.clicked.connect(self._print)

        # User code section ends here

        self.retranslateUi(MainWindow)
        self.comboAxes.setCurrentIndex(-1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def _change_freq(self):
       self.freq = self.spinFreqs.value()

    def _change_sample_len(self):
        self.len = self.spinPoints.value()
        Ui_MainWindow.rec_data1 = deque([0] * self.len, self.len)
        Ui_MainWindow.rec_data2 = deque([0] * self.len, self.len)

    def plotType(self):
        temp_text = self.comboAxes.currentText()
        if temp_text == 'Raw':
            Ui_MainWindow.plot_mode = 1
        elif temp_text == 'Processed':
            Ui_MainWindow.plot_mode = 2
        elif temp_text == 'Both':
            Ui_MainWindow.plot_mode = 3
        else:
            pass


    def plot_thread(self):

        while(True):
            if Ui_MainWindow.is_started is True:
                if self.ser.in_waiting > 0:
                    # There is data waiting to be processed do it here
                    #1.  Parse the data
                    temp_raw_container = self.ser.read_all()
                    temp_parsed_container = temp_raw_container.splitlines()
                    #2. Check for packet features
                    for temp in temp_parsed_container:
                        temp_bytes = bytearray(temp)
                        if temp_bytes[0] == Ui_MainWindow.receive_packet[0]:
                            if len(temp_bytes) == Ui_MainWindow.receive_packet[1]:
                                #3. The packet is intact, the data can be stored
                                temp = temp_bytes[2]*8 + temp_bytes[3]

                                temp = temp / 65536.0 * 3.3

                                Ui_MainWindow.rec_data1.append(temp)

                                temp = temp_bytes[4] * 8 + temp_bytes[5]

                                temp = temp / 65536.0 * 3.3

                                Ui_MainWindow.rec_data2.append(temp)

                                #4. Plot the updated np buffer
                                self.figure1.clear()
                                ax = self.figure1.add_subplot(111)
                                if Ui_MainWindow.plot_mode == 1:
                                    ax.plot(Ui_MainWindow.rec_data1, 'r-')
                                elif Ui_MainWindow.plot_mode == 2:
                                    ax.plot(Ui_MainWindow.rec_data2, 'b-')
                                elif Ui_MainWindow.plot_mode == 3:
                                    ax.plot(Ui_MainWindow.rec_data1, 'r-')
                                    ax.plot(Ui_MainWindow.rec_data2, 'b-')
                                self.canvas1.draw()

                                # 5. FFT

                                X = np.linspace(0, self.freq*1000 // 2, self.len // 2)
                                self.figure2.clear()
                                ax = self.figure2.add_subplot(111)
                                if Ui_MainWindow.plot_mode == 1:
                                    temp_np_array = np.array(Ui_MainWindow.rec_data1, dtype=np.float32)
                                    np_fft_array = scipy.fftpack.fft(temp_np_array)
                                    ax.plot(X, np.abs(np_fft_array[:self.len // 2]), 'r-')
                                elif Ui_MainWindow.plot_mode == 2:
                                    temp_np_array = np.array(Ui_MainWindow.rec_data2, dtype=np.float32)
                                    np_fft_array = scipy.fftpack.fft(temp_np_array)
                                    ax.plot(X, np.abs(np_fft_array[:self.len // 2]), 'g-')
                                elif Ui_MainWindow.plot_mode == 3:
                                    temp_np_array = np.array(Ui_MainWindow.rec_data1, dtype=np.float32)
                                    np_fft_array = scipy.fftpack.fft(temp_np_array)
                                    ax.plot(X, np.abs(np_fft_array[:self.len // 2]), 'r-')
                                    temp_np_array = np.array(Ui_MainWindow.rec_data2, dtype=np.float32)
                                    np_fft_array = scipy.fftpack.fft(temp_np_array)
                                    ax.plot(X, np.abs(np_fft_array[:self.len // 2]), 'g-')
                                self.canvas2.draw()

                                #6. Redraw plot gridlines
                                plt.grid()

                            else:
                                pass
                        else:
                            pass

                else:
                    pass
            time.sleep(0.1)

    @staticmethod
    def serial_ports():
        ports = serial.tools.list_ports.comports()
        result = []
        for port in ports:
            result.append(port.device)
        return result

    def _connect(self):
        if Ui_MainWindow.is_connected is False:
            try:
                port_num = str(self.comboPort.currentText())
                baud = str(self.comboBaud.currentText())
                parity = str(self.comboParity.currentText())
                if parity == "None":
                    parity = serial.PARITY_NONE
                if parity == "Odd":
                    parity = serial.PARITY_ODD
                if parity == "Even":
                    parity = serial.PARITY_NONE
                stop_bit = str(self.comboStop.currentText())
                if stop_bit == "1":
                    stop_bit = serial.STOPBITS_ONE
                if stop_bit == "2":
                    stop_bit = serial.STOPBITS_TWO

                self.ser = serial.Serial(port=port_num, baudrate=int(baud), stopbits=stop_bit, parity=parity)
                Ui_MainWindow.is_connected = True
                self.connectButton.setText("Disconnect")
            except:
                wr = QtWidgets.QMessageBox.warning(self.centralWidget, "Error", "Can't connect to device!")


        else:
            if Ui_MainWindow.is_started is True:
                wr = QtWidgets.QMessageBox.warning(self.centralWidget, "Warning", "Stop acquisition!")
            else:
                try:
                    self.ser.close()
                    Ui_MainWindow.is_connected = False
                    self.connectButton.setText("Connect")
                except:
                    wr = QtWidgets.QMessageBox.error(self.centralWidget, "Error", "Can't disconnect from device!")

    def _start(self):
        if Ui_MainWindow.is_connected is True:
            temp = self.send_packet
            if Ui_MainWindow.is_started is True:
                temp[3] = 0x31
                self.ser.write(self.send_packet)
                self.startPlotButton.setText("Start Plot")
                Ui_MainWindow.is_started = False
                self.ser.flushInput()
            else:
                self.startPlotButton.setText("Stop Plot")
                temp[3] = 0x32
                self.ser.write(temp)
                Ui_MainWindow.is_started = True
        else:
            wr = QtWidgets.QMessageBox.warning(self.centralWidget, "Warning", "Connect to device first!")

    def _reset(self):
        # reset everything
        pass

    def _print(self):
        self.figure1.savefig('./plot1.png')
        self.figure2.savefig('./plot2.png')


    def closeEvent(self, event):
        if Ui_MainWindow.is_connected is True:
            wr = QtWidgets.QMessageBox.warning(self.centralWidget, "Warning", "Disconnect device first!")
            event.ignore()
        else:
            if Ui_MainWindow.is_started is True:
                wr = QtWidgets.QMessageBox.warning(self.centralWidget, "Warning", "Stop data flow first!")
                event.ignore()

            else:
                wr = QtWidgets.QMessageBox.question(self.centralWidget, "Are you sure enough?",
                                                    QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No)
                if wr == QtWidgets.QMessageBox.Yes:
                    event.accept()
                else:
                    event.ignore()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.PortControlsBox.setTitle(_translate("MainWindow", "PORT CONTROLS"))
        self.labelPort.setText(_translate("MainWindow", "PORT"))
        self.labelBaud.setText(_translate("MainWindow", "BAUD"))
        self.labelData.setText(_translate("MainWindow", "DATA"))
        self.labelParity.setText(_translate("MainWindow", "PARITY"))
        self.labelStop.setText(_translate("MainWindow", "STOP"))
        self.connectButton.setText(_translate("MainWindow", "Connect"))
        self.PlotControlsBox.setTitle(_translate("MainWindow", "PLOT CONTROLS"))
        self.labelAxes.setText(_translate("MainWindow", "AXES"))
        self.pointsLabel.setText(_translate("MainWindow", "Samples"))
        self.freqLabel.setText(_translate("MainWindow", "Fs(kHz)"))
        self.saveJPGButton.setText(_translate("MainWindow", "Save JPG"))
        self.startPlotButton.setText(_translate("MainWindow", "Start Plot"))
        self.menuHelo.setTitle(_translate("MainWindow", "Help"))
        self.actionHow_to_use.setText(_translate("MainWindow", "How to use "))

    def openHelp(self):
        self.HelpWindow.show()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())