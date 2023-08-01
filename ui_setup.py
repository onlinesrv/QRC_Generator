from PyQt5.QtWidgets import QPushButton,QHeaderView
from PyQt5.QtCore import QSize,QTime,QPropertyAnimation,QSize
from PyQt5.QtGui import QIcon,QPixmap


import functions



def setup_ui(self):

    btn_list = [self.browse_prog_btn,self.browse_files_btn,self.create_btn,self.exit_btn]

    self.browse_prog_btn.setIcon(QIcon(QPixmap(r":\icons\browse_01.png")))
    self.browse_prog_btn.clicked.connect(lambda: functions.open_folder_dialog(self,self.path_prog_le))



    self.browse_files_btn.setIcon(QIcon(QPixmap(r":\icons\browse_02.png")))
    self.browse_files_btn.clicked.connect(lambda: functions.open_folder_dialog(self,self.path_files_le))





    self.create_btn.setIcon(QIcon(QPixmap(r":\icons\create.png")))
    self.create_btn.clicked.connect(lambda: functions.createQRCfile(self))



    self.exit_btn.setIcon(QIcon(QPixmap(r":icons\exit.png")))
    self.exit_btn.clicked.connect(self.close)

    for btn in btn_list:
        btn.setIconSize(QSize(30,30))
       

    self.me_pic.setPixmap(QPixmap(":photos\profile_picture.png"))
   
    self.me.clicked.connect(lambda: functions.open_link(self))
    
    



