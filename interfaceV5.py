from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QPixmap, QColor
import cv2
from PyQt5.QtCore import Qt, QThread, pyqtSlot, pyqtSignal
import numpy as np
#import get

class VideoThread(QThread):
    change_pixmap_signal = pyqtSignal(np.ndarray)
    def run(self):
#        get.runMain()
        cap = cv2.VideoCapture(0)
        while True:
            ret, cv_img = cap.read()
            cv_img = cv2.flip(cv_img, 1)
            if ret:
                self.change_pixmap_signal.emit(cv_img)

    def stopCam(self):
        pass

class Ui_MainWindow(object):

        
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1178, 900)
        MainWindow.setStyleSheet("color: rgb(0, 0, 0);\n"
"background-color: rgb(228, 230, 191);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.LogoKhoaDien = QtWidgets.QFrame(self.centralwidget)
        self.LogoKhoaDien.setGeometry(QtCore.QRect(20, 20, 100, 100))
        self.LogoKhoaDien.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.LogoKhoaDien.setFrameShadow(QtWidgets.QFrame.Raised)
        self.LogoKhoaDien.setObjectName("LogoKhoaDien")
        self.LogoBkMaker = QtWidgets.QFrame(self.centralwidget)
        self.LogoBkMaker.setGeometry(QtCore.QRect(980, 20, 100, 100))
        self.LogoBkMaker.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.LogoBkMaker.setFrameShadow(QtWidgets.QFrame.Raised)
        self.LogoBkMaker.setObjectName("LogoBkMaker")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(130, 20, 841, 101))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.header = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(19)
        self.header.setFont(font)
        self.header.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.header.setAutoFillBackground(False)
        self.header.setAlignment(QtCore.Qt.AlignCenter)
        self.header.setWordWrap(False)
        self.header.setObjectName("header")
        self.verticalLayout.addWidget(self.header)
        self.studentName = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(19)
        self.studentName.setFont(font)
        self.studentName.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.studentName.setAutoFillBackground(False)
        self.studentName.setAlignment(QtCore.Qt.AlignCenter)
        self.studentName.setWordWrap(False)
        self.studentName.setObjectName("studentName")
        self.verticalLayout.addWidget(self.studentName)
        self.teacherName = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(19)
        self.teacherName.setFont(font)
        self.teacherName.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.teacherName.setAutoFillBackground(False)
        self.teacherName.setAlignment(QtCore.Qt.AlignCenter)
        self.teacherName.setWordWrap(False)
        self.teacherName.setObjectName("teacherName")
        self.verticalLayout.addWidget(self.teacherName)
        self.formLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.formLayoutWidget.setGeometry(QtCore.QRect(720, 200, 341, 131))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 0, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.formLayout.setItem(2, QtWidgets.QFormLayout.LabelRole, spacerItem)
        self.line = QtWidgets.QFrame(self.formLayoutWidget)
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.line)
        self.name = QtWidgets.QLabel(self.formLayoutWidget)
        self.name.setObjectName("name")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.name)
        self.infoName = QtWidgets.QLabel(self.formLayoutWidget)
        self.infoName.setEnabled(True)
        self.infoName.setStyleSheet("border: 2px soild;\n"
"border-color: rgb(0, 0, 0);\n"
"\n"
"background-color: rgb(211, 215, 207);")
        self.infoName.setText("")
        self.infoName.setObjectName("infoName")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.infoName)
        self.birthDay = QtWidgets.QLabel(self.formLayoutWidget)
        self.birthDay.setObjectName("birthDay")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.birthDay)
        self.infoDay = QtWidgets.QLabel(self.formLayoutWidget)
        self.infoDay.setStyleSheet("border: 2px soild;\n"
"border-color: rgb(0, 0, 0);\n"
"\n"
"background-color: rgb(211, 215, 207);")
        self.infoDay.setText("")
        self.infoDay.setObjectName("infoDay")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.infoDay)
        self.job = QtWidgets.QLabel(self.formLayoutWidget)
        self.job.setObjectName("job")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.LabelRole, self.job)
        self.infoJob = QtWidgets.QLabel(self.formLayoutWidget)
        self.infoJob.setStyleSheet("border: 2px soild;\n"
"border-color: rgb(0, 0, 0);\n"
"\n"
"background-color: rgb(211, 215, 207);")
        self.infoJob.setText("")
        self.infoJob.setObjectName("infoJob")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.FieldRole, self.infoJob)
        self.information = QtWidgets.QLabel(self.formLayoutWidget)
        self.information.setObjectName("information")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.SpanningRole, self.information)
        self.formLayoutWidget_3 = QtWidgets.QWidget(self.centralwidget)
        self.formLayoutWidget_3.setGeometry(QtCore.QRect(720, 540, 341, 181))
        self.formLayoutWidget_3.setObjectName("formLayoutWidget_3")
        self.formLayout_4 = QtWidgets.QFormLayout(self.formLayoutWidget_3)
        self.formLayout_4.setContentsMargins(0, 0, 0, 0)
        self.formLayout_4.setObjectName("formLayout_4")
        self.addMember = QtWidgets.QLabel(self.formLayoutWidget_3)
        self.addMember.setObjectName("addMember")
        self.formLayout_4.setWidget(1, QtWidgets.QFormLayout.SpanningRole, self.addMember)
        spacerItem1 = QtWidgets.QSpacerItem(40, 0, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.formLayout_4.setItem(2, QtWidgets.QFormLayout.LabelRole, spacerItem1)
        self.nameAdd = QtWidgets.QLabel(self.formLayoutWidget_3)
        self.nameAdd.setObjectName("nameAdd")
        self.formLayout_4.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.nameAdd)
        self.nameEdit = QtWidgets.QLineEdit(self.formLayoutWidget_3)
        self.nameEdit.setObjectName("nameEdit")
        self.formLayout_4.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.nameEdit)
        self.birthDayAdd = QtWidgets.QLabel(self.formLayoutWidget_3)
        self.birthDayAdd.setObjectName("birthDayAdd")
        self.formLayout_4.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.birthDayAdd)
        self.dateEdit = QtWidgets.QDateEdit(self.formLayoutWidget_3)
        self.dateEdit.setStyleSheet("font: 57 11pt \"Ubuntu\";\n"
"font: 11pt \"Ubuntu\";")
        self.dateEdit.setObjectName("dateEdit")
        self.formLayout_4.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.dateEdit)
        self.jobAdd = QtWidgets.QLabel(self.formLayoutWidget_3)
        self.jobAdd.setObjectName("jobAdd")
        self.formLayout_4.setWidget(6, QtWidgets.QFormLayout.LabelRole, self.jobAdd)
        self.jobEdit = QtWidgets.QComboBox(self.formLayoutWidget_3)
        self.jobEdit.setObjectName("jobEdit")
        self.jobEdit.addItem("")
        self.jobEdit.addItem("")
        self.jobEdit.addItem("")
        self.formLayout_4.setWidget(6, QtWidgets.QFormLayout.FieldRole, self.jobEdit)
        self.getDataButton = QtWidgets.QPushButton(self.centralwidget)
        self.getDataButton.setGeometry(QtCore.QRect(720, 730, 141, 51))
        self.getDataButton.setStyleSheet("font: 13pt \"Ubuntu\";\n"
"\n"
"background-color: rgb(233, 185, 110);\n"
"\n"
"\n"
"")
        self.getDataButton.setCheckable(False)
        self.getDataButton.setObjectName("getDataButton")
        
        self.getDataButton.clicked.connect(self.get_clicked)
        self.getDataButton.show()
        self.trainButton = QtWidgets.QPushButton(self.centralwidget)
        self.trainButton.setGeometry(QtCore.QRect(920, 730, 141, 51))
        self.trainButton.setStyleSheet("font: 13pt \"Ubuntu\";\n"
"\n"
"\n"
"background-color: rgb(78, 154, 6);\n"
"\n"
"\n"
"")
        self.trainButton.setCheckable(False)
        self.trainButton.setObjectName("trainButton")

        self.trainButton.clicked.connect(self.train_clicked)
        self.trainButton.show()

        self.imageFace = QtWidgets.QFrame(self.centralwidget)
        self.imageFace.setGeometry(QtCore.QRect(810, 330, 160, 160))
        self.imageFace.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.imageFace.setFrameShadow(QtWidgets.QFrame.Raised)
        self.imageFace.setObjectName("imageFace")
        self.webcam = QtWidgets.QLabel(self.centralwidget)
        self.webcam.setGeometry(QtCore.QRect(60, 200, 600, 600))
       # grey = QPixmap(600,600)
        #grey.fill(QColor('darkGray'))
        # set the image image to the grey pixmap
        #self.webcam.setPixmap(grey)
#        cv_img = cv2.imread('image.jpg')
#        qt_img = self.convert_cv_qt(cv_img)
#        self.webcam.setPixmap(qt_img)
        self.thread = VideoThread()
        self.thread.change_pixmap_signal.connect(self.update_image)
#        self.thread.start()
#

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.header.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; font-weight:600; color:#ef2929;\">APPLICATION OF ARTIFICIAL INTELLGENCE TO MANAGE LABORATORY</span></p></body></html>"))
        self.studentName.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:600; color:#2e3436;\">Student\'s Name: Phan Ben, Phan Trong Huu - Class: 18TDH1</span></p></body></html>"))
        self.teacherName.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:600; color:#2e3436;\">Supervisor\'s Name: PhD. Ngo Dinh Thanh</span></p></body></html>"))
        self.name.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600; color:#2e3436;\">Name</span></p></body></html>"))
        self.birthDay.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600; color:#2e3436;\">Birthday</span></p></body></html>"))
        self.job.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600; color:#2e3436;\">Job</span></p></body></html>"))
        self.information.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:600; color:#2e3436;\">Information</span></p></body></html>"))
        self.addMember.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:600; color:#2e3436;\">Add Member</span></p></body></html>"))
        self.nameAdd.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600; color:#2e3436;\">Name</span></p></body></html>"))
        self.birthDayAdd.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600; color:#2e3436;\">Birthday</span></p></body></html>"))
        self.jobAdd.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600; color:#2e3436;\">Job</span></p></body></html>"))
        self.jobEdit.setItemText(0, _translate("MainWindow", "Student"))
        self.jobEdit.setItemText(1, _translate("MainWindow", "Teacher"))
        self.jobEdit.setItemText(2, _translate("MainWindow", "Other"))
        self.getDataButton.setText(_translate("MainWindow", "Get Data"))
        self.trainButton.setText(_translate("MainWindow", "Train"))
    
#    @pyqtSlot(np.ndarray)
    def update_image(self, cv_img):
        """Updates the image_label with a new opencv image"""
        qt_img = self.convert_cv_qt(cv_img)
        self.webcam.setPixmap(qt_img)
    def convert_cv_qt(self, cv_img):
        """Convert from an opencv image to QPixmap"""
        rgb_image = cv2.cvtColor(cv_img, cv2.COLOR_BGR2RGB)
        h, w, ch = rgb_image.shape
        bytes_per_line = ch * w
        convert_to_Qt_format = QtGui.QImage(rgb_image, w, h, bytes_per_line, QtGui.QImage.Format_RGB888)
        p = convert_to_Qt_format.scaled(600,600,Qt.KeepAspectRatio)
        return QPixmap.fromImage(p)
    def get_clicked(self):
        print('OK')
        self.thread.start()
    def train_clicked(self):
        print('Stop Camera')
        self.thread.stopCam()

import sys
def main():
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
if __name__ == '__main__':
    main()

