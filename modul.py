import os,subprocess,shutil
from PyQt5.QtCore import QThread , pyqtSignal,QUrl
from PyQt5.QtGui import  QDesktopServices
import functions


class CreateQRCFile(QThread):
    statu_info = pyqtSignal(str)
    link_info = pyqtSignal(str)
    wrinting_file_error = pyqtSignal(str)

    def __init__(self,project_path,files_path,open,convert):
        super().__init__()
        self.isRunning = True
       

        self.project_path = project_path.replace("/","\\")
        self.files_path =files_path.replace("/","\\")
        
        self.open =open
        self.convert =convert
        
        
    def run(self):
        while self.isRunning == True:
            self.statu_info.emit('start')
            all_links, all_files = functions.get_all_folders_and_files(self.files_path)
            all_links.extend(all_files)
            all_final_links =[]
            for link in all_links:
                if os.path.isdir(link):
                    for item in os.listdir(link):
                        item_path = os.path.join(link, item)
                        if os.path.isfile(item_path):
                            all_final_links.append((item_path.split(self.project_path)[1])[1:])
                if os.path.isfile(link):
                    all_final_links.append((link.split(self.project_path)[1])[1:])
            
            
            res_file = os.path.join(self.project_path,"resources.qrc")
            with open( res_file,"w") as f:
                try:
                    f.write("<!DOCTYPE RCC>\n")
                    f.write('<RCC version="1.0">\n')
                    f.write("    <qresource>\n")
                    for link in all_final_links:
                        try:
                            f.write(f"        <file>{link}</file>\n")
                        except UnicodeEncodeError: 
                            self.statu_info.emit('no_arabic')
                            break
                    f.write('    </qresource>\n')
                    f.write('</RCC>')
                    f.close() 
                    ####destination_file = os.path.join(self.project_path,"resources.qrc")
                    self.isRunning ==False          
                except Exception as e:
                    w_error = str(e)
                    self.wrinting_file_error.emit(w_error)

            if self.open ==True:
                QDesktopServices.openUrl(QUrl.fromLocalFile(self.project_path)) 

            if self.convert ==True:
                    
                    
                py_file = res_file.replace("qrc","py")
                command = f"pyrcc5 -o {py_file} {res_file}"
                    
                try:
                    output = subprocess.check_output(command, shell=True, text=True)
                    
                except subprocess.CalledProcessError as e:
                    w_error = str(e.returncode)
                    self.wrinting_file_error.emit(w_error)
                   

            self.statu_info.emit("finish")
            
            self.isRunning = False