# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
import pymysql
try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Dialog(object):
    def loginCheck(self):
        print("Login Button clicked ")
        user=self.username.text()
        passw=self.password.text()
        checkArgs=(user,passw)
        db=pymysql.connect("localhost","root","","dbpython")
        cursor=db.cursor()
        query="SELECT * FROM `logindetails` WHERE USERNAME ='%s' AND PASSWORD = '%s'"%checkArgs
        print(query)
        try:
            cursor.execute(query)
            result=cursor.fetchall()
            if (len(result) > 0):
                print("Entry Found")
                for row in result:
                    print("Username  :",row[0]," Email :",row[2])
                print("Successful")
            else:
                print("Wrong username or password !")
        except(AttributeError):
            print(AttributeError)
        finally:
            db.close()
    def signUp(self):
        print("In sign in")
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(486, 272)
        Dialog.setStyleSheet(_fromUtf8("QDialog{\n"
"    background-color: qlineargradient(spread:pad, x1:0.5, y1:0.5, x2:0.5, y2:0, stop:0 rgba(0, 170, 255, 255), stop:1 rgba(255, 255, 255, 255));\n"
"}\n"
"QPushButton{\n"
"background-color:rgb(255,255,255);\n"
"border:none;\n"
"}"))
        self.loginBtn = QtGui.QPushButton(Dialog)
        self.loginBtn.setGeometry(QtCore.QRect(170, 120, 75, 23))
        self.loginBtn.setObjectName(_fromUtf8("loginBtn"))
        ########################### Login Button Event ####################################
        self.loginBtn.clicked.connect(self.loginCheck)
        ###################################End of Event####################################
        self.username = QtGui.QLineEdit(Dialog)
        self.username.setGeometry(QtCore.QRect(220, 50, 113, 20))
        self.username.setObjectName(_fromUtf8("username"))
        self.label = QtGui.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(135, 50, 61, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(133, 80, 61, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.password = QtGui.QLineEdit(Dialog)
        self.password.setGeometry(QtCore.QRect(220, 80, 111, 20))
        self.password.setObjectName(_fromUtf8("password"))
        self.password.setEchoMode(2)
        self.signupBtn = QtGui.QPushButton(Dialog)
        self.signupBtn.setGeometry(QtCore.QRect(260, 120, 75, 23))
        self.signupBtn.setObjectName(_fromUtf8("signupBtn"))
        ########################### Login Button Event ####################################
        self.signupBtn.clicked.connect(self.signUp)
        ###################################End of Event####################################
        self.label_3 = QtGui.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(200, 10, 81, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName(_fromUtf8("label_3"))

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Login Form", None))
        self.loginBtn.setText(_translate("Dialog", "Login", None))
        self.label.setText(_translate("Dialog", "Username", None))
        self.label_2.setText(_translate("Dialog", "Password", None))
        self.signupBtn.setText(_translate("Dialog", "Sign Up", None))
        self.label_3.setText(_translate("Dialog", "Login", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Dialog = QtGui.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

