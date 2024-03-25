# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'qt_gui.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1190, 733)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tab_plots = QtWidgets.QTabWidget(self.centralwidget)
        self.tab_plots.setGeometry(QtCore.QRect(350, 10, 831, 671))
        self.tab_plots.setAutoFillBackground(False)
        self.tab_plots.setTabPosition(QtWidgets.QTabWidget.North)
        self.tab_plots.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.tab_plots.setObjectName("tab_plots")
        self.tab_in = QtWidgets.QWidget()
        self.tab_in.setAccessibleName("")
        self.tab_in.setObjectName("tab_in")
        self.plot_a_time_in = PlotWidget(self.tab_in)
        self.plot_a_time_in.setGeometry(QtCore.QRect(10, 10, 801, 301))
        self.plot_a_time_in.setObjectName("plot_a_time_in")
        self.plot_a_freq_in = PlotWidget(self.tab_in)
        self.plot_a_freq_in.setGeometry(QtCore.QRect(10, 320, 801, 301))
        self.plot_a_freq_in.setObjectName("plot_a_freq_in")
        self.tab_plots.addTab(self.tab_in, "")
        self.tab_aaf = QtWidgets.QWidget()
        self.tab_aaf.setObjectName("tab_aaf")
        self.plot_a_freq_aaf = PlotWidget(self.tab_aaf)
        self.plot_a_freq_aaf.setGeometry(QtCore.QRect(10, 320, 801, 301))
        self.plot_a_freq_aaf.setObjectName("plot_a_freq_aaf")
        self.plot_a_time_aaf = PlotWidget(self.tab_aaf)
        self.plot_a_time_aaf.setGeometry(QtCore.QRect(10, 10, 801, 301))
        self.plot_a_time_aaf.setObjectName("plot_a_time_aaf")
        self.tab_plots.addTab(self.tab_aaf, "")
        self.tab_sh = QtWidgets.QWidget()
        self.tab_sh.setObjectName("tab_sh")
        self.plot_a_freq_sh = PlotWidget(self.tab_sh)
        self.plot_a_freq_sh.setGeometry(QtCore.QRect(10, 320, 801, 301))
        self.plot_a_freq_sh.setObjectName("plot_a_freq_sh")
        self.plot_a_time_sh = PlotWidget(self.tab_sh)
        self.plot_a_time_sh.setGeometry(QtCore.QRect(10, 10, 801, 301))
        self.plot_a_time_sh.setObjectName("plot_a_time_sh")
        self.tab_plots.addTab(self.tab_sh, "")
        self.tab_as = QtWidgets.QWidget()
        self.tab_as.setObjectName("tab_as")
        self.plot_a_freq_as = PlotWidget(self.tab_as)
        self.plot_a_freq_as.setGeometry(QtCore.QRect(10, 320, 801, 301))
        self.plot_a_freq_as.setObjectName("plot_a_freq_as")
        self.plot_a_time_as = PlotWidget(self.tab_as)
        self.plot_a_time_as.setGeometry(QtCore.QRect(10, 10, 801, 301))
        self.plot_a_time_as.setObjectName("plot_a_time_as")
        self.tab_plots.addTab(self.tab_as, "")
        self.tab_rf = QtWidgets.QWidget()
        self.tab_rf.setObjectName("tab_rf")
        self.plot_a_freq_rf = PlotWidget(self.tab_rf)
        self.plot_a_freq_rf.setGeometry(QtCore.QRect(10, 320, 801, 301))
        self.plot_a_freq_rf.setObjectName("plot_a_freq_rf")
        self.plot_a_time_rf = PlotWidget(self.tab_rf)
        self.plot_a_time_rf.setGeometry(QtCore.QRect(10, 10, 801, 301))
        self.plot_a_time_rf.setObjectName("plot_a_time_rf")
        self.tab_plots.addTab(self.tab_rf, "")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.plot_a_time_custom = PlotWidget(self.tab)
        self.plot_a_time_custom.setGeometry(QtCore.QRect(10, 10, 801, 301))
        self.plot_a_time_custom.setObjectName("plot_a_time_custom")
        self.plot_a_freq_custom = PlotWidget(self.tab)
        self.plot_a_freq_custom.setGeometry(QtCore.QRect(10, 320, 801, 301))
        self.plot_a_freq_custom.setObjectName("plot_a_freq_custom")
        self.tab_plots.addTab(self.tab, "")
        self.box_signalSampling = QtWidgets.QGroupBox(self.centralwidget)
        self.box_signalSampling.setGeometry(QtCore.QRect(10, 10, 331, 671))
        self.box_signalSampling.setCheckable(False)
        self.box_signalSampling.setObjectName("box_signalSampling")
        self.box_inputSignals = QtWidgets.QGroupBox(self.box_signalSampling)
        self.box_inputSignals.setGeometry(QtCore.QRect(10, 20, 311, 181))
        self.box_inputSignals.setFlat(False)
        self.box_inputSignals.setObjectName("box_inputSignals")
        self.box_typeInputSignal = QtWidgets.QComboBox(self.box_inputSignals)
        self.box_typeInputSignal.setGeometry(QtCore.QRect(10, 20, 89, 31))
        self.box_typeInputSignal.setObjectName("box_typeInputSignal")
        self.box_typeInputSignal.addItem("")
        self.box_typeInputSignal.addItem("")
        self.box_typeInputSignal.addItem("")
        self.box_typeInputSignal.addItem("")
        self.box_typeInputSignal.addItem("")
        self.label_frecInputSignal = QtWidgets.QLabel(self.box_inputSignals)
        self.label_frecInputSignal.setGeometry(QtCore.QRect(20, 60, 90, 21))
        self.label_frecInputSignal.setObjectName("label_frecInputSignal")
        self.spin_frecInputSignal = QtWidgets.QSpinBox(self.box_inputSignals)
        self.spin_frecInputSignal.setGeometry(QtCore.QRect(210, 60, 91, 21))
        self.spin_frecInputSignal.setMaximum(100000)
        self.spin_frecInputSignal.setProperty("value", 15000)
        self.spin_frecInputSignal.setObjectName("spin_frecInputSignal")
        self.label_frecInputDuty = QtWidgets.QLabel(self.box_inputSignals)
        self.label_frecInputDuty.setGeometry(QtCore.QRect(20, 90, 85, 21))
        self.label_frecInputDuty.setObjectName("label_frecInputDuty")
        self.spin_dutyInputSignal = QtWidgets.QSpinBox(self.box_inputSignals)
        self.spin_dutyInputSignal.setGeometry(QtCore.QRect(210, 90, 91, 21))
        self.spin_dutyInputSignal.setMaximum(100)
        self.spin_dutyInputSignal.setProperty("value", 50)
        self.spin_dutyInputSignal.setObjectName("spin_dutyInputSignal")
        self.import_button = QtWidgets.QPushButton(self.box_inputSignals)
        self.import_button.setEnabled(False)
        self.import_button.setGeometry(QtCore.QRect(180, 20, 125, 28))
        self.import_button.setMouseTracking(False)
        self.import_button.setCheckable(False)
        self.import_button.setAutoDefault(False)
        self.import_button.setDefault(False)
        self.import_button.setFlat(False)
        self.import_button.setObjectName("import_button")
        self.spin_samplesInputSignal = QtWidgets.QSpinBox(self.box_inputSignals)
        self.spin_samplesInputSignal.setGeometry(QtCore.QRect(210, 120, 91, 21))
        self.spin_samplesInputSignal.setMinimum(1)
        self.spin_samplesInputSignal.setMaximum(100000)
        self.spin_samplesInputSignal.setProperty("value", 1000)
        self.spin_samplesInputSignal.setObjectName("spin_samplesInputSignal")
        self.label_samplesInputSignal = QtWidgets.QLabel(self.box_inputSignals)
        self.label_samplesInputSignal.setGeometry(QtCore.QRect(20, 120, 142, 21))
        self.label_samplesInputSignal.setObjectName("label_samplesInputSignal")
        self.label_paddingLength = QtWidgets.QLabel(self.box_inputSignals)
        self.label_paddingLength.setGeometry(QtCore.QRect(20, 150, 87, 21))
        self.label_paddingLength.setObjectName("label_paddingLength")
        self.spin_paddingLength = QtWidgets.QSpinBox(self.box_inputSignals)
        self.spin_paddingLength.setGeometry(QtCore.QRect(210, 150, 91, 21))
        self.spin_paddingLength.setMinimum(1)
        self.spin_paddingLength.setMaximum(100000)
        self.spin_paddingLength.setProperty("value", 1000)
        self.spin_paddingLength.setObjectName("spin_paddingLength")
        self.box_samplingType = QtWidgets.QGroupBox(self.box_signalSampling)
        self.box_samplingType.setGeometry(QtCore.QRect(10, 270, 311, 101))
        self.box_samplingType.setObjectName("box_samplingType")
        self.check_sampleHold = QtWidgets.QCheckBox(self.box_samplingType)
        self.check_sampleHold.setGeometry(QtCore.QRect(10, 40, 154, 20))
        self.check_sampleHold.setObjectName("check_sampleHold")
        self.spin_dutyControlSignalSH = QtWidgets.QSpinBox(self.box_samplingType)
        self.spin_dutyControlSignalSH.setGeometry(QtCore.QRect(210, 40, 91, 21))
        self.spin_dutyControlSignalSH.setMaximum(100)
        self.spin_dutyControlSignalSH.setProperty("value", 50)
        self.spin_dutyControlSignalSH.setObjectName("spin_dutyControlSignalSH")
        self.label_dutyControlSignalSH = QtWidgets.QLabel(self.box_samplingType)
        self.label_dutyControlSignalSH.setGeometry(QtCore.QRect(230, 15, 42, 21))
        self.label_dutyControlSignalSH.setObjectName("label_dutyControlSignalSH")
        self.check_analogSwitch = QtWidgets.QCheckBox(self.box_samplingType)
        self.check_analogSwitch.setGeometry(QtCore.QRect(10, 70, 133, 20))
        self.check_analogSwitch.setObjectName("check_analogSwitch")
        self.spin_dutyControlSignalAS = QtWidgets.QSpinBox(self.box_samplingType)
        self.spin_dutyControlSignalAS.setGeometry(QtCore.QRect(210, 70, 91, 21))
        self.spin_dutyControlSignalAS.setMaximum(100)
        self.spin_dutyControlSignalAS.setProperty("value", 50)
        self.spin_dutyControlSignalAS.setObjectName("spin_dutyControlSignalAS")
        self.box_filters = QtWidgets.QGroupBox(self.box_signalSampling)
        self.box_filters.setGeometry(QtCore.QRect(10, 380, 311, 101))
        self.box_filters.setObjectName("box_filters")
        self.check_AAF = QtWidgets.QCheckBox(self.box_filters)
        self.check_AAF.setGeometry(QtCore.QRect(10, 40, 163, 21))
        self.check_AAF.setCheckable(True)
        self.check_AAF.setChecked(False)
        self.check_AAF.setObjectName("check_AAF")
        self.check_RF = QtWidgets.QCheckBox(self.box_filters)
        self.check_RF.setGeometry(QtCore.QRect(10, 70, 168, 20))
        self.check_RF.setObjectName("check_RF")
        self.label_2 = QtWidgets.QLabel(self.box_filters)
        self.label_2.setGeometry(QtCore.QRect(230, 15, 39, 21))
        self.label_2.setObjectName("label_2")
        self.spin_freqAAF = QtWidgets.QSpinBox(self.box_filters)
        self.spin_freqAAF.setGeometry(QtCore.QRect(210, 40, 91, 21))
        self.spin_freqAAF.setMaximum(1000000)
        self.spin_freqAAF.setProperty("value", 40000)
        self.spin_freqAAF.setObjectName("spin_freqAAF")
        self.spin_freqRF = QtWidgets.QSpinBox(self.box_filters)
        self.spin_freqRF.setGeometry(QtCore.QRect(210, 70, 91, 21))
        self.spin_freqRF.setMaximum(1000000)
        self.spin_freqRF.setProperty("value", 40000)
        self.spin_freqRF.setObjectName("spin_freqRF")
        self.box_controlSignal = QtWidgets.QGroupBox(self.box_signalSampling)
        self.box_controlSignal.setGeometry(QtCore.QRect(10, 210, 311, 51))
        self.box_controlSignal.setObjectName("box_controlSignal")
        self.label_frecControlSignal = QtWidgets.QLabel(self.box_controlSignal)
        self.label_frecControlSignal.setGeometry(QtCore.QRect(20, 20, 90, 21))
        self.label_frecControlSignal.setObjectName("label_frecControlSignal")
        self.spin_frecControlSignal = QtWidgets.QSpinBox(self.box_controlSignal)
        self.spin_frecControlSignal.setGeometry(QtCore.QRect(210, 20, 91, 21))
        self.spin_frecControlSignal.setMaximum(1000000)
        self.spin_frecControlSignal.setProperty("value", 100000)
        self.spin_frecControlSignal.setObjectName("spin_frecControlSignal")
        self.box_custom = QtWidgets.QGroupBox(self.box_signalSampling)
        self.box_custom.setEnabled(False)
        self.box_custom.setGeometry(QtCore.QRect(10, 490, 311, 171))
        self.box_custom.setCheckable(False)
        self.box_custom.setObjectName("box_custom")
        self.check_customInput = QtWidgets.QCheckBox(self.box_custom)
        self.check_customInput.setGeometry(QtCore.QRect(10, 20, 70, 17))
        self.check_customInput.setObjectName("check_customInput")
        self.check_customAS = QtWidgets.QCheckBox(self.box_custom)
        self.check_customAS.setGeometry(QtCore.QRect(10, 80, 70, 17))
        self.check_customAS.setObjectName("check_customAS")
        self.check_customRF = QtWidgets.QCheckBox(self.box_custom)
        self.check_customRF.setGeometry(QtCore.QRect(10, 100, 70, 17))
        self.check_customRF.setObjectName("check_customRF")
        self.check_customSH = QtWidgets.QCheckBox(self.box_custom)
        self.check_customSH.setGeometry(QtCore.QRect(10, 60, 70, 17))
        self.check_customSH.setObjectName("check_customSH")
        self.check_customAAF = QtWidgets.QCheckBox(self.box_custom)
        self.check_customAAF.setGeometry(QtCore.QRect(10, 40, 70, 17))
        self.check_customAAF.setObjectName("check_customAAF")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1190, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tab_plots.setCurrentIndex(0)
        self.box_typeInputSignal.setCurrentIndex(-1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.tab_plots.setTabText(self.tab_plots.indexOf(self.tab_in), _translate("MainWindow", "Input"))
        self.tab_plots.setTabText(self.tab_plots.indexOf(self.tab_aaf), _translate("MainWindow", "AAF"))
        self.tab_plots.setTabText(self.tab_plots.indexOf(self.tab_sh), _translate("MainWindow", "S/H"))
        self.tab_plots.setTabText(self.tab_plots.indexOf(self.tab_as), _translate("MainWindow", "AS"))
        self.tab_plots.setTabText(self.tab_plots.indexOf(self.tab_rf), _translate("MainWindow", "RF"))
        self.tab_plots.setTabText(self.tab_plots.indexOf(self.tab), _translate("MainWindow", "Custom"))
        self.box_signalSampling.setTitle(_translate("MainWindow", "Signal Sampling"))
        self.box_inputSignals.setTitle(_translate("MainWindow", "Input Signal"))
        self.box_typeInputSignal.setItemText(0, _translate("MainWindow", "Sinusoidal"))
        self.box_typeInputSignal.setItemText(1, _translate("MainWindow", "Exponential"))
        self.box_typeInputSignal.setItemText(2, _translate("MainWindow", "Triangular"))
        self.box_typeInputSignal.setItemText(3, _translate("MainWindow", "Square"))
        self.box_typeInputSignal.setItemText(4, _translate("MainWindow", "Audio"))
        self.label_frecInputSignal.setText(_translate("MainWindow", "Frecuency [Hz]"))
        self.label_frecInputDuty.setText(_translate("MainWindow", "Duty Cycle [%]"))
        self.import_button.setText(_translate("MainWindow", "Import Audio [WAV]"))
        self.label_samplesInputSignal.setText(_translate("MainWindow", "Number of Samples: N"))
        self.label_paddingLength.setText(_translate("MainWindow", "Padding Length"))
        self.box_samplingType.setTitle(_translate("MainWindow", "Sampling Type"))
        self.check_sampleHold.setText(_translate("MainWindow", "S/H: Sample and Hold"))
        self.label_dutyControlSignalSH.setText(_translate("MainWindow", "DC [%]"))
        self.check_analogSwitch.setText(_translate("MainWindow", "AS: Analog Switch"))
        self.box_filters.setTitle(_translate("MainWindow", "Filters"))
        self.check_AAF.setText(_translate("MainWindow", "AAF: Anti-Aliasing Filter"))
        self.check_RF.setText(_translate("MainWindow", "RF: Reconstruction Filter"))
        self.label_2.setText(_translate("MainWindow", "fp [Hz]"))
        self.box_controlSignal.setTitle(_translate("MainWindow", "Control Signal"))
        self.label_frecControlSignal.setText(_translate("MainWindow", "Frecuency [Hz]"))
        self.box_custom.setTitle(_translate("MainWindow", "Visible Traces"))
        self.check_customInput.setText(_translate("MainWindow", "Input"))
        self.check_customAS.setText(_translate("MainWindow", "AS"))
        self.check_customRF.setText(_translate("MainWindow", "RF"))
        self.check_customSH.setText(_translate("MainWindow", "S/H"))
        self.check_customAAF.setText(_translate("MainWindow", "AAF"))
from pyqtgraph import PlotWidget


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
