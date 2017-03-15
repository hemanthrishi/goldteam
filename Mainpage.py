# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Mainpage.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

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

class Ui_PregameMainWindow(object):
    def setupUi(self, PregameMainWindow):
        PregameMainWindow.setObjectName(_fromUtf8("PregameMainWindow"))
        PregameMainWindow.resize(800, 600)
        self.centralwidget = QtGui.QWidget(PregameMainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.playgameButton = QtGui.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.playgameButton.setFont(font)
        self.playgameButton.setObjectName(_fromUtf8("playgameButton"))
        self.verticalLayout.addWidget(self.playgameButton)
        self.exitButton = QtGui.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.exitButton.setFont(font)
        self.exitButton.setObjectName(_fromUtf8("exitButton"))
        self.verticalLayout.addWidget(self.exitButton)
        self.exitButton.raise_()
        self.playgameButton.raise_()
        PregameMainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(PregameMainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 25))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        PregameMainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(PregameMainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        PregameMainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(PregameMainWindow)
        QtCore.QObject.connect(self.exitButton, QtCore.SIGNAL(_fromUtf8("clicked()")), PregameMainWindow.close)
        QtCore.QMetaObject.connectSlotsByName(PregameMainWindow)

    def retranslateUi(self, PregameMainWindow):
        PregameMainWindow.setWindowTitle(_translate("PregameMainWindow", "MainWindow", None))
        self.playgameButton.setText(_translate("PregameMainWindow", "Play Game", None))
        self.exitButton.setText(_translate("PregameMainWindow", "Exit", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    PregameMainWindow = QtGui.QMainWindow()
    ui = Ui_PregameMainWindow()
    ui.setupUi(PregameMainWindow)
    PregameMainWindow.show()
    sys.exit(app.exec_())

