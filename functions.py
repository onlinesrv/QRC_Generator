import os
from PyQt5.QtWidgets import QApplication, QMessageBox, QPushButton, QCheckBox, QVBoxLayout, QFileDialog
from PyQt5.QtGui import  QDesktopServices
from PyQt5.QtCore import QUrl



import modul


def open_folder_dialog(self,lineEdit):
        options = QFileDialog.Options()
        folder_path = QFileDialog.getExistingDirectory(self, "Select Folder", options=options)
        if folder_path:
            lineEdit.setText(folder_path)
            

def chek_inputs(self):
    msg = ""
    if self.path_prog_le.text() == "":
        msg = msg + "\n" + "مسار مجلد البرنامج غير محدد"

    elif  self.path_files_le.text() == "":
        msg = msg + "\n" + "مسار مجلد الملفات غير محدد"

    if msg != "":       
        QMessageBox.warning(self,"QRC Generator", msg)
    else:
        createQRCfile(self)


def get_all_folders(main_folder):
    all_folders = []
    
    for dirpath, dirnames, filenames in os.walk(main_folder):
       
        all_folders.extend([os.path.join(dirpath, dirname) for dirname in dirnames])
        
    
    return all_folders

def get_all_folders_and_files(main_folder):
   
    all_folders = []
    all_files = []

    for dirpath, dirnames, filenames in os.walk(main_folder):
        for dirname in dirnames:
            folder_path = os.path.normpath(os.path.join(dirpath, dirname))
            all_folders.append(folder_path)

        for filename in filenames:
            file_path = os.path.normpath(os.path.join(dirpath, filename))
            all_files.append(file_path)
    
    return all_folders, all_files




def createQRCfile(self):
    msg = ""
    if self.path_prog_le.text() == "":
        msg = msg + "\n" + "مسار مجلد البرنامج غير محدد"

    if  self.path_files_le.text() == "":
        msg = msg + "\n" + "مسار مجلد الملفات غير محدد"

    if msg != "":       
        QMessageBox.warning(self,"QRC Generator", msg)
    

    else:
        self.project_path = self.path_prog_le.text()
        self.files_path = self.path_files_le.text()
        
        if self.show_chb.isChecked():
            open = True
        else:
            open = False

        if self.py_convert.isChecked():
            convert = True
        else:
            convert = False

        if self.project_path in self.files_path and self.files_path != self.project_path:
            self.CreateQRCFileThread = modul.CreateQRCFile(self.project_path,self.files_path,open,convert)
            self.CreateQRCFileThread.start()
            
            self.CreateQRCFileThread.statu_info.connect(self.CreateQRCFileThreadStatus)
            self.CreateQRCFileThread.link_info.connect(self.CreateQRCFileThreadLink)
            self.CreateQRCFileThread.wrinting_file_error.connect(self.CreateQRCFileThreadwrinting_file_error)
            
            
            
        else:
            QMessageBox.warning(self,"QRC Generator", "لابد لمجلد الملفات ان يكون داخل مجلد البرنامج")



def open_link(self):
    QDesktopServices.openUrl(QUrl("https://www.facebook.com/pythonprog"))



