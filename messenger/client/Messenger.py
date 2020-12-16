from datetime import datetime

import requests
from PyQt5 import QtWidgets, QtCore

from messenger.client import clientui


# наследуем основной класс Ui_messenger
class MessengerWindow(QtWidgets.QMainWindow, clientui.Ui_messenger):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.messagesPush.pressed.connect(self.send_message)
        self.after = 0
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.update_messages)
        self.timer.start(1000)

    # обновление сообщений и вывод в messagesBox
    def update_messages(self):
        try:
            response = requests.get(
                'http://127.0.0.1:5000/messages',
                params={'after': self.after}
            )
        except:
            return

        for message in response.json()['messages']:
            dt = datetime.fromtimestamp(message['time'])
            dt = dt.strftime('%H:%M:%S')

            self.messagesBox.append((dt + ' ' + message['name']))
            self.messagesBox.append(message['text'])
            self.messagesBox.append('')
            self.after = message['time']

    #  отправка сообщения
    def send_message(self):
        name = self.name.text()
        text = self.messagesInput.toPlainText()
        try:
            response = requests.post(
                'http://127.0.0.1:5000/send',
                json={'text': text, 'name': name}
            )
        except:
            # если сервер недоступен/упал
            self.messagesBox.append('Сервер недоступен, попробуйте позже')
            self.messagesBox.append('')
            self.messagesBox.repaint()
            return

        if response.status_code == 400:
            self.messagesBox.append('Неправильное имя или пароль')
            self.messagesBox.append('')
            self.messagesBox.repaint()
            return

        # очистка строки отправки сообщения
        self.messagesInput.clear()
        self.messagesInput.repaint()


# запуск приложения
app = QtWidgets.QApplication([])
window = MessengerWindow()
window.show()
app.exec_()
