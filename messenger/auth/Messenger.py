from datetime import datetime

from PyQt5 import QtWidgets, QtCore
import requests
from messenger.auth import authui, clientui


# окно авторизации
class Authorization(QtWidgets.QMainWindow, authui.Ui_authorization):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.send_login)

    # отправка логина и пароля на сервер
    def send_login(self):
        login = self.login.text()
        password = self.password.text()
        try:
            # отправка самого токена
            response = requests.post(
                'http://127.0.0.1:5000/auth',
                json={'login': login, 'password': password}
            )
            if response:
                self.init_handlers()

        except:
            print('Упс.. что-то пошло не так')

            return

    # если ввод логина и пароля правильные, то открывается мессенджер и закрывается окно авторизации
    def init_handlers(self):  # обработка нажатия для октрытия 2 окна
        self.pushButton.clicked.connect(self.show_window_2)

    # собственно открытие второго окна
    def show_window_2(self):
        window.close()
        self.messenger = MessengerWindow()
        self.messenger.show()


# окно самого мессенджера
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
            # получение токена
            response = requests.get(
                'http://127.0.0.1:5000/messages',
                params={'after': self.after}
            )
        except:
            return

        # вывод сообщения в messageBox
        for message in response.json()['messages']:
            dt = datetime.fromtimestamp(message['time'])
            dt = dt.strftime('%H:%M:%S')
            self.messagesBox.append((dt + ' ' + message['login']))
            self.messagesBox.append(message['text'])
            self.messagesBox.append('')
            self.after = message['time']

    #  отправка сообщения
    def send_message(self):
        # получение токена с авторизации, и отправка токена с  именем пользователя(логина) и сообщением
        response = requests.get('http://127.0.0.1:5000/auth_logs')
        login = 0
        for i in response.json()['auth']:
            login = i['login']

        text = self.messagesInput.toPlainText()
        try:
            # сам токена с именем и сообщением
            response = requests.post(
                'http://127.0.0.1:5000/send',
                json={'text': text, 'login': login}
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


app = QtWidgets.QApplication([])
window = Authorization()
window.show()
app.exec_()
