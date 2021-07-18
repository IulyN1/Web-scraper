import requests
from bs4 import BeautifulSoup as bs
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
import sys

class MyWindow(QMainWindow):
    def __init__(self):
        super(MyWindow,self).__init__()
        self.resize(600,150)
        self.setWindowTitle("Web Scraper")
        self.initGui()

    def initGui(self):
        self.label = QtWidgets.QLabel(self)
        self.label.setText("GitHub user: ")
        self.label.move(10,10)

        self.inp = QtWidgets.QLineEdit(self)
        self.inp.move(80,10)

        self.btn = QtWidgets.QPushButton(self)
        self.btn.setText("Get profile picture")
        self.btn.clicked.connect(self.clicked)
        self.btn.move(10,60)

        self.link = QtWidgets.QLineEdit(self)
        self.link.setDisabled(True)
        self.link.setGeometry(120,60,400,30)
    
    def clicked(self):
        self.link.setDisabled(False)
        pic = self.get_profile()
        self.link.setText(pic)
        
    def get_profile(self):
        user = self.inp.text()
        if user != "":
            url = "https://github.com/" + user
            req = requests.get(url)
            soup = bs(req.content,"html.parser")
            profile = soup.find("img",{"alt":"Avatar"})["src"]
            return profile
        else:
            self.link.setDisabled(True)
            msg = QMessageBox()
            msg.setWindowTitle("Warning!")
            msg.setText("Please input a username!")
            msg.setIcon(QMessageBox.Warning)
            msg.exec_()     

def window():
    app = QApplication(sys.argv)
    win = MyWindow()
    win.show()
    sys.exit(app.exec_())

window()