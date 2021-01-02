

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_messenger_window(object):
    def setupUi(self, messenger_window):
        messenger_window.setObjectName("messenger_window")
        messenger_window.resize(522, 589)
        self.centralwidget = QtWidgets.QWidget(messenger_window)
        self.centralwidget.setStyleSheet("QWidget{\n"
                                         "background-color: white\n"
                                         "}")
        self.centralwidget.setObjectName("centralwidget")
        self.messagesInput = QtWidgets.QTextEdit(self.centralwidget)
        self.messagesInput.setGeometry(QtCore.QRect(40, 490, 341, 41))
        self.messagesInput.setStyleSheet("QTextEdit{\n"
                                         "border: 1px solid rgb(188, 188, 186);\n"
                                         "border-radius: 15px;\n"
                                         "}")
        self.messagesInput.setTabStopWidth(80)
        self.messagesInput.setObjectName("messagesInput")
        self.messagesPush = QtWidgets.QPushButton(self.centralwidget)
        self.messagesPush.setGeometry(QtCore.QRect(390, 490, 93, 41))
        self.messagesPush.setStyleSheet("QPushButton{\n"
                                        "border: 1px solid rgb(188, 188, 186);\n"
                                        "border-radius: 15px;\n"
                                        "background-color: rgb(219, 255, 246)\n"
                                        "}")
        self.messagesPush.setObjectName("messagesPush")
        self.messagesBox = QtWidgets.QTextBrowser(self.centralwidget)
        self.messagesBox.setGeometry(QtCore.QRect(40, 80, 441, 391))
        self.messagesBox.setStyleSheet("QTextBrowser{\n"
                                       "border: 1px solid rgb(188, 188, 186);\n"
                                       "border-radius: 15px;\n"
                                       "}")
        self.messagesBox.setObjectName("messagesBox")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(190, 40, 131, 31))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label.setFont(font)
        self.label.setObjectName("label")
        messenger_window.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(messenger_window)
        self.statusbar.setObjectName("statusbar")
        messenger_window.setStatusBar(self.statusbar)

        self.retranslateUi(messenger_window)
        QtCore.QMetaObject.connectSlotsByName(messenger_window)

    def retranslateUi(self, messenger_window):
        _translate = QtCore.QCoreApplication.translate
        messenger_window.setWindowTitle(_translate("messenger_window", "MainWindow"))
        self.messagesInput.setPlaceholderText(_translate("messenger_window", "Введите сообщение.."))
        self.messagesPush.setText(_translate("messenger_window", "Отправить"))
        self.label.setText(_translate("messenger_window", "Mihalich-zver"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    messenger_window = QtWidgets.QMainWindow()
    ui = Ui_messenger_window()
    ui.setupUi(messenger_window)
    messenger_window.show()
    sys.exit(app.exec_())
