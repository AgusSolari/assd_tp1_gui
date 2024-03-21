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

from matplotlib.backends.backend_qt5agg import (NavigationToolbar2QT as NavigationToolbar)

class signal:
    tt = []
    st = []
    
class signal_f:
    tf = []
    sf = []

class data_class:
    def __init__(self):
        self.input_signal = signal()
        self.input_signal_f = signal_f()
        
        self.sample_signal = signal()
        self.sample_signal_f = signal_f()
        
    

    


class MainWindow(QMainWindow, Ui_MainWindow):
    
    
    def __init__(self):
        
        super().__init__()
        self.setupUi(self)
        
        self.setWindowTitle('ASSD - GUI - Muestreo de señales')
        
        self.data = data_class()
        
        self.show()
        
        self.connect_signals()
        

    def connect_signals(self):
        print('connect_signals')
        self.spin_frecInputSignal.valueChanged.connect(lambda: fp.generate_input_signal(self))
        self.spin_dutyInputSignal.valueChanged.connect(lambda: fp.generate_input_signal(self))
        self.box_typeInputSignal.currentIndexChanged.connect(lambda: fp.generate_input_signal(self))
        
        self.check_FAA.toggled.connect(lambda: fp.generate_input_signal(self))
        self.spin_freqFAA.valueChanged.connect(lambda: fp.generate_input_signal(self))
        self.check_FR.toggled.connect(lambda: fp.generate_input_signal(self))
        self.spin_freqFR.valueChanged.connect(lambda: fp.generate_input_signal(self))
        
        self.spin_frecControlSignal.valueChanged.connect(lambda: fp.generate_input_signal(self))
        self.check_sampleHold.toggled.connect(lambda: fp.generate_input_signal(self))
        self.spin_dutyControlSignalSH.valueChanged.connect(lambda: fp.generate_input_signal(self))
        self.check_analogSwitch.toggled.connect(lambda: fp.generate_input_signal(self))
        self.spin_dutyControlSignalAS.valueChanged.connect(lambda: fp.generate_input_signal(self))
        
        self.spin_samplesInputSignal.valueChanged.connect(lambda: fp.generate_input_signal(self))
        self.spin_paddingLength.valueChanged.connect(lambda: fp.generate_input_signal(self))
        
        self.import_button.clicked.connect(lambda: fp.generate_input_signal(self))
        self.import_button.clicked.connect(lambda: fp.import_file)

        


        
        
    
def main():
    
    
    app = QApplication([])
    window = MainWindow()
    app.exec_()
    
if __name__ == '__main__':
    main()
    