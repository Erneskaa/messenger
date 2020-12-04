# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'messenger.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_messenger(object):
    def setupUi(self, messenger):
        messenger.setObjectName("messenger")
        messenger.resize(522, 589)
        self.centralwidget = QtWidgets.QWidget(messenger)
        self.centralwidget.setObjectName("centralwidget")
        self.messagesInput = QtWidgets.QTextEdit(self.centralwidget)
        self.messagesInput.setGeometry(QtCore.QRect(40, 490, 341, 41))
        self.messagesInput.setTabStopWidth(80)
        self.messagesInput.setObjectName("messagesInput")
        self.messagesPush = QtWidgets.QPushButton(self.centralwidget)
        self.messagesPush.setGeometry(QtCore.QRect(390, 490, 93, 41))
        self.messagesPush.setObjectName("messagesPush")
        self.messagesBox = QtWidgets.QTextBrowser(self.centralwidget)
        self.messagesBox.setGeometry(QtCore.QRect(40, 100, 441, 371))
        self.messagesBox.setObjectName("messagesBox")
        self.nameChat = QtWidgets.QLabel(self.centralwidget)
        self.nameChat.setGeometry(QtCore.QRect(220, 20, 101, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.nameChat.setFont(font)
        self.nameChat.setLineWidth(1)
        self.nameChat.setObjectName("nameChat")
        self.nameLabel = QtWidgets.QLabel(self.centralwidget)
        self.nameLabel.setGeometry(QtCore.QRect(298, 71, 55, 16))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.nameLabel.sizePolicy().hasHeightForWidth())
        self.nameLabel.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.nameLabel.setFont(font)
        self.nameLabel.setObjectName("nameLabel")
        self.name = QtWidgets.QLineEdit(self.centralwidget)
        self.name.setGeometry(QtCore.QRect(367, 70, 113, 22))
        self.name.setObjectName("name")
        messenger.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(messenger)
        self.statusbar.setObjectName("statusbar")
        messenger.setStatusBar(self.statusbar)

        self.retranslateUi(messenger)
        QtCore.QMetaObject.connectSlotsByName(messenger)

    def retranslateUi(self, messenger):
        _translate = QtCore.QCoreApplication.translate
        messenger.setWindowTitle(_translate("messenger", "MainWindow"))
        self.messagesInput.setPlaceholderText(_translate("messenger", "Введите сообщение.."))
        self.messagesPush.setText(_translate("messenger", "Отправить"))
        self.nameChat.setText(_translate("messenger", "Messenger"))
        self.nameLabel.setText(_translate("messenger", "Name:"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    messenger = QtWidgets.QMainWindow()
    ui = Ui_messenger()
    ui.setupUi(messenger)
    messenger.show()
    sys.exit(app.exec_())