import sys
from PyQt5.QtWidgets import QMainWindow,QMessageBox,QApplication
from PyQt5.uic import loadUiType , loadUi
from PyQt5.QtWidgets import QMainWindow  
from PyQt5.QtGui import  QIcon


import ui_setup,resources
from  main import Ui_MainWindow


class MainApp(QMainWindow,Ui_MainWindow):
    
    def __init__(self):
        QMainWindow.__init__(self)
        self.setupUi(self)
        ui_setup.setup_ui(self)
        
        self.setWindowIcon(QIcon(r":\icons\create.png"))

    def CreateQRCFileThreadStatus(self,info):
        if info == "finish":
            self.create_btn.setEnabled(True)
            self.steps.setText('')

        if info =="start":
            self.create_btn.setEnabled(False)
            self.steps.setText('يتم إنشاء الملف الرجاء الإنتظار ...')     
        if info =="no_arabic":
            QMessageBox.warning(self,"QRC Generator", "لابد أن تكون أسماء الملفات والمجلدات بالأحرف اللاتينية و الأرقام فقط")
            

    def CreateQRCFileThreadLink(self,link):
        self.path = link
        
    
    
    def CreateQRCFileThreadwrinting_file_error(self,error):
        QMessageBox.warning(self,"QRC Generator",f"حدث مشكل أثناء إنشاء الملف \n {error}" )





app = QApplication(sys.argv)
mainWindow = MainApp()
mainWindow.show()
sys.exit(app.exec())














