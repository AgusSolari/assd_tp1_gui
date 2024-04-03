import subprocess
import function_plot as fp
import input_signals as isig

subprocess.run(["pyuic5", "-x", "qt_gui.ui", "-o", "py_gui.py"])

from PyQt5.QtWidgets import QApplication
from PyQt5.QtGui import *
from PyQt5.QtWidgets import QMainWindow
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow
from py_gui import Ui_MainWindow
import pyqtgraph as pg

from matplotlib.backends.backend_qt5agg import (NavigationToolbar2QT as NavigationToolbar)

class SignalData:
    """Class for storing signal information"""
    tt = []
    st = []
    tf = []
    sf = []

class SignalsData:
    """Class for storing signals in each node of the sampling process"""
    def __init__(self):
        self.input_signal = SignalData()
        self.aaf_signal = SignalData()
        self.sh_signal = SignalData()
        self.as_signal = SignalData()
        self.rf_signal = SignalData()
        self.custom_signal = SignalData()

class MainWindow(QMainWindow, Ui_MainWindow):
    
    
    def __init__(self):
        
        super().__init__()
        self.setupUi(self)
        
        self.setWindowTitle('ASSD - GUI - Muestreo de señales')
        self.setWindowIcon(QIcon('logo.jpg'))
        
        self.data = SignalsData()
        
        self.show()
        
        self.connect_signals()
        

    def connect_signals(self):
        self.spin_frecInputSignal.valueChanged.connect(lambda: fp.generate_node_signal(self))
        self.spin_perExtInputSignal.valueChanged.connect(lambda: fp.generate_node_signal(self))
        self.spin_frecPortInputSignal.valueChanged.connect(lambda: fp.generate_node_signal(self))
        self.spin_frecModInputSignal.valueChanged.connect(lambda: fp.generate_node_signal(self))
        self.spin_dutyInputSignal.valueChanged.connect(lambda: fp.generate_node_signal(self))
        self.box_typeInputSignal.currentIndexChanged.connect(lambda: fp.generate_node_signal(self))

        self.check_AAF.toggled.connect(lambda: fp.generate_node_signal(self))
        self.spin_freqAAF.valueChanged.connect(lambda: fp.generate_node_signal(self))
        self.check_RF.toggled.connect(lambda: fp.generate_node_signal(self))
        self.spin_freqRF.valueChanged.connect(lambda: fp.generate_node_signal(self))

        self.spin_frecControlSignal.valueChanged.connect(lambda: fp.generate_node_signal(self))
        self.check_sampleHold.toggled.connect(lambda: fp.generate_node_signal(self))
        self.spin_dutyControlSignalSH.valueChanged.connect(lambda: fp.generate_node_signal(self))
        self.check_analogSwitch.toggled.connect(lambda: fp.generate_node_signal(self))
        self.spin_dutyControlSignalAS.valueChanged.connect(lambda: fp.generate_node_signal(self))

        self.spin_samplesInputSignal.valueChanged.connect(lambda: fp.generate_node_signal(self))
        self.spin_paddingLength.valueChanged.connect(lambda: fp.generate_node_signal(self))

        self.import_button.clicked.connect(lambda: fp.generate_node_signal(self))
        
        self.tab_plots.currentChanged.connect(lambda: fp.generate_node_signal(self))
        
        self.check_customInput.toggled.connect(lambda: fp.generate_node_signal(self))
        self.check_customAAF.toggled.connect(lambda: fp.generate_node_signal(self))
        self.check_customSH.toggled.connect(lambda: fp.generate_node_signal(self))
        self.check_customAS.toggled.connect(lambda: fp.generate_node_signal(self))
        self.check_customRF.toggled.connect(lambda: fp.generate_node_signal(self))

        self.import_button.clicked.connect(lambda: fp.import_file(self))

    #     self.menu_aa.triggered.connect(self.configPlots)
    #     self.menu_bgColorBlack.triggered.connect(self.selectBlackBg)
    #     self.menu_bgColorWhite.triggered.connect(self.selectWhiteBg)
        
    # def selectBlackBg(self):
    #     if(self.menu_bgColorBlack.isChecked()):
    #         self.menu_bgColorWhite.setChecked(False)
    #         self.configPlots()
    #     else:
    #         self.menu_bgColorWhite.setChecked(True)
    #         self.selectWhiteBg()

    # def selectWhiteBg(self):
    #     if(self.menu_bgColorWhite.isChecked()):
    #         self.menu_bgColorBlack.setChecked(False)
    #         self.configPlots()
    #     else:
    #         self.menu_bgColorBlack.setChecked(True)
    #         self.selectBlackBg()

    # def configPlots(self):
    #     if self.menu_bgColorBlack.isChecked():
    #         print('hola')
    #         pg.setConfigOption('background', 'w')
    #         pg.setConfigOption('foreground', 'k')
    #     else:
    #         pg.setConfigOption('background', 'k')
    #         pg.setConfigOption('foreground', 'w')
    #     if self.menu_aa.isChecked():
    #         pg.setConfigOption('antialias', True)
    #     else:
    #         pg.setConfigOption('antialias', False)

def main():
    app = QApplication([])
    window = MainWindow()
    app.exec_()
    
if __name__ == '__main__':
    main()
    