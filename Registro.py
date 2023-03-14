# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Registro.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1440, 1024)
        MainWindow.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setEnabled(True)
        self.label.setGeometry(QtCore.QRect(630, 20, 190, 305))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setBaseSize(QtCore.QSize(70, 55))
        self.label.setText("")
        self.label.setTextFormat(QtCore.Qt.RichText)
        self.label.setPixmap(QtGui.QPixmap(":/ADCOLogo/Oaks.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(650, 360, 161, 41))
        font = QtGui.QFont()
        font.setFamily("Inter")
        font.setPointSize(18)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.label_2.setFont(font)
        self.label_2.setTextFormat(QtCore.Qt.RichText)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(510, 430, 111, 41))
        font = QtGui.QFont()
        font.setFamily("Inter")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.label_3.setFont(font)
        self.label_3.setTextFormat(QtCore.Qt.RichText)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(510, 540, 171, 41))
        font = QtGui.QFont()
        font.setFamily("Inter")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.label_4.setFont(font)
        self.label_4.setTextFormat(QtCore.Qt.RichText)
        self.label_4.setObjectName("label_4")
        self.Usr = QtWidgets.QLineEdit(self.centralwidget)
        self.Usr.setGeometry(QtCore.QRect(510, 480, 441, 41))
        font = QtGui.QFont()
        font.setFamily("Inter")
        font.setPointSize(12)
        self.Usr.setFont(font)
        self.Usr.setStyleSheet("QWidget#Usr{\n"
"background: rgb(238, 238, 238);\n"
"}\n"
"\n"
"QWidget:focus#Usr{\n"
"border: 1.5px solid rgb(77, 181, 127); \n"
"}")
        self.Usr.setAlignment(QtCore.Qt.AlignJustify|QtCore.Qt.AlignTop)
        self.Usr.setObjectName("Usr")
        self.Pss = QtWidgets.QLineEdit(self.centralwidget)
        self.Pss.setGeometry(QtCore.QRect(510, 600, 441, 41))
        font = QtGui.QFont()
        font.setFamily("Inter")
        font.setPointSize(10)
        self.Pss.setFont(font)
        self.Pss.setStyleSheet("QWidget#Pss{\n"
"background: rgb(238, 238, 238);\n"
"}\n"
"\n"
"QWidget:focus#Pss{\n"
"border: 1.5px solid rgb(77, 181, 127); \n"
"}")
        self.Pss.setInputMethodHints(QtCore.Qt.ImhHiddenText|QtCore.Qt.ImhNoAutoUppercase|QtCore.Qt.ImhNoPredictiveText|QtCore.Qt.ImhSensitiveData)
        self.Pss.setEchoMode(QtWidgets.QLineEdit.Password)
        self.Pss.setPlaceholderText("")
        self.Pss.setObjectName("Pss")
        self.R = QtWidgets.QPushButton(self.centralwidget)
        self.R.setGeometry(QtCore.QRect(530, 690, 391, 61))
        font = QtGui.QFont()
        font.setFamily("Inter")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.R.setFont(font)
        self.R.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.R.setAcceptDrops(False)
        self.R.setStyleSheet("QWidget#R{\n"
"border-radius: 17px;\n"
"color: white;\n"
"background: rgb(77, 181, 127);\n"
"}\n"
"\n"
"QWidget:hover#R{\n"
"background-color: rgb(83, 197, 136);\n"
"}\n"
"\n"
"QWidget:pressed#R{\n"
"background-color: rgb(62, 148, 102);\n"
"}\n"
"\n"
"\n"
"\n"
"")
        self.R.setObjectName("R")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(760, 800, 71, 21))
        font = QtGui.QFont()
        font.setFamily("Inter")
        font.setPointSize(10)
        self.label_5.setFont(font)
        self.label_5.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(600, 800, 161, 21))
        font = QtGui.QFont()
        font.setFamily("Inter")
        font.setPointSize(10)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setEnabled(True)
        self.label_7.setGeometry(QtCore.QRect(670, 870, 101, 41))
        self.label_7.setText("")
        self.label_7.setPixmap(QtGui.QPixmap(":/ADCOLogo/Adco.png"))
        self.label_7.setScaledContents(True)
        self.label_7.setObjectName("label_7")
        self.test = QtWidgets.QRadioButton(self.centralwidget)
        self.test.setGeometry(QtCore.QRect(230, 710, 95, 20))
        self.test.setObjectName("test")
        self.test2 = QtWidgets.QPushButton(self.centralwidget)
        self.test2.setGeometry(QtCore.QRect(180, 560, 93, 28))
        self.test2.setStyleSheet("QWidget:pressed#test2{\n"
"QWidget::Normal#Pss\n"
"}")
        self.test2.setObjectName("test2")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(310, 410, 55, 16))
        self.label_8.setObjectName("label_8")
        MainWindow.setCentralWidget(self.centralwidget)
        self.label.setBuddy(self.label)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_2.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#2e2e2e;\">REGISTRO</span></p></body></html>"))
        self.label_3.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#2e2e2e;\">USUARIO</span></p></body></html>"))
        self.label_4.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#2e2e2e;\">CONTRASEÑA</span></p></body></html>"))
        self.R.setText(_translate("MainWindow", "Registrarse"))
        self.label_5.setToolTip(_translate("MainWindow", "<html><head/><body><p><a href=\"-\"><span style=\" text-decoration: underline; color:#0000ff;\">Accede</span></a></p></body></html>"))
        self.label_5.setText(_translate("MainWindow", "<html><head/><body><p><a href=\"---\"><span style=\" text-decoration: underline; color:#4db57f;\">Accede</span></a></p></body></html>"))
        self.label_6.setText(_translate("MainWindow", "¿Ya tienes cuenta?"))
        self.test.setText(_translate("MainWindow", "RadioButton"))
        self.test2.setText(_translate("MainWindow", "PushButton"))
        self.label_8.setText(_translate("MainWindow", "TextLabel"))
import login_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
