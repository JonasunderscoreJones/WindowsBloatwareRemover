# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'done.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_done(object):
    def setupUi(self, done):
        done.setObjectName("done")
        done.resize(248, 182)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("src/icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        done.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(done)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(80, 20, 91, 31))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(40, 50, 171, 61))
        self.label_2.setObjectName("label_2")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(70, 120, 91, 34))
        self.pushButton.setObjectName("pushButton")
        done.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(done)
        self.statusbar.setObjectName("statusbar")
        done.setStatusBar(self.statusbar)

        self.retranslateUi(done)
        QtCore.QMetaObject.connectSlotsByName(done)

    def retranslateUi(self, done):
        _translate = QtCore.QCoreApplication.translate
        done.setWindowTitle(_translate("done", "All Done!"))
        self.label.setText(_translate("done", "<html><head/><body><p><span style=\" font-size:14pt; font-weight:600;\">All Done!</span></p></body></html>"))
        self.label_2.setText(_translate("done", "Thanks for using this tool\n"
" and enjoy your now less\n"
" bloaty Windows installation!"))
        self.pushButton.setText(_translate("done", "Exit Program"))


def show():
    import sys
    app = QtWidgets.QApplication(sys.argv)
    done = QtWidgets.QMainWindow()
    ui = Ui_done()
    ui.setupUi(done)
    done.show()
    sys.exit(app.exec_())
