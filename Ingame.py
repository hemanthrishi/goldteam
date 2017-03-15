# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Ingame.ui'
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

class Ui_IngameMainWindow(object):
    def setupUi(self, IngameMainWindow):
        IngameMainWindow.setObjectName(_fromUtf8("IngameMainWindow"))
        IngameMainWindow.resize(800, 600)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        IngameMainWindow.setFont(font)
        IngameMainWindow.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.centralwidget = QtGui.QWidget(IngameMainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.startgameoverButton = QtGui.QPushButton(self.centralwidget)
        self.startgameoverButton.setGeometry(QtCore.QRect(110, 460, 151, 27))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Ubuntu"))
        self.startgameoverButton.setFont(font)
        self.startgameoverButton.setObjectName(_fromUtf8("startgameoverButton"))
        self.backtoMainMenuButton_ = QtGui.QPushButton(self.centralwidget)
        self.backtoMainMenuButton_.setGeometry(QtCore.QRect(470, 460, 171, 27))
        self.backtoMainMenuButton_.setFocusPolicy(QtCore.Qt.TabFocus)
        self.backtoMainMenuButton_.setObjectName(_fromUtf8("backtoMainMenuButton_"))
        self.progressBar = QtGui.QProgressBar(self.centralwidget)
        self.progressBar.setGeometry(QtCore.QRect(120, 500, 531, 23))
        self.progressBar.setCursor(QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName(_fromUtf8("progressBar"))
        self.nextcardButton = QtGui.QPushButton(self.centralwidget)
        self.nextcardButton.setGeometry(QtCore.QRect(240, 410, 281, 27))
        self.nextcardButton.setObjectName(_fromUtf8("nextcardButton"))
        IngameMainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(IngameMainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        IngameMainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(IngameMainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        IngameMainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(IngameMainWindow)
        QtCore.QMetaObject.connectSlotsByName(IngameMainWindow)

    def retranslateUi(self, IngameMainWindow):
        IngameMainWindow.setWindowTitle(_translate("IngameMainWindow", "MainWindow", None))
        self.startgameoverButton.setToolTip(_translate("IngameMainWindow", "<html><head/><body><p>Resets the cards and restarts the game</p></body></html>", None))
        self.startgameoverButton.setText(_translate("IngameMainWindow", "Start Game Over", None))
        self.backtoMainMenuButton_.setToolTip(_translate("IngameMainWindow", "<html><head/><body><p>Exits out of the game.</p></body></html>", None))
        self.backtoMainMenuButton_.setText(_translate("IngameMainWindow", "Back to Main Menu", None))
        self.progressBar.setToolTip(_translate("IngameMainWindow", "<html><head/><body><p>Indicates the amount of black cards already used in the game.</p></body></html>", None))
        self.progressBar.setWhatsThis(_translate("IngameMainWindow", "<html><head/><body><p><br/></p></body></html>", None))
        self.nextcardButton.setText(_translate("IngameMainWindow", "Next Card", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    IngameMainWindow = QtGui.QMainWindow()
    ui = Ui_IngameMainWindow()
    ui.setupUi(IngameMainWindow)
    IngameMainWindow.show()
    sys.exit(app.exec_())

