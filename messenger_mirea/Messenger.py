import sys
from datetime import datetime

import requests
from PyQt5 import QtWidgets, QtCore

from messenger_mirea.auth import authui, clientui, sign_up_ui


# окно авторизации

class Authorization(QtWidgets.QMainWindow, authui.Ui_authorization):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.sign_in.clicked.connect(self.send_login)
        self.sign_up.clicked.connect(self.window_registration)

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
                window.close()
                messenger.show()

        except:
            # print('Упс.. что-то пошло не так')
            return

    @staticmethod
    def window_registration():
        window.close()
        registration_window.show()


# регистрационное окно
class Registration(QtWidgets.QMainWindow, sign_up_ui.Ui_registration):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.cancel_reg.clicked.connect(self.cancel_window_reg)
        # отправка формы регистрации
        self.send_reg_form.clicked.connect(self.send_form)

    def send_form(self):
        login = self.login_regist.text()
        password = self.password_regist.text()
        confirm_password = self.confirm_regist.text()
        try:
            response = requests.post(
                'http://127.0.0.1:5000/auth',
                json={'login': login, 'password': password, 'confirm_password': confirm_password}
            )
            if response:
                self.cancel_window_reg()
        except:
            return

    # закрытие регистрационного окна
    @staticmethod
    def cancel_window_reg():
        registration_window.close()
        window.show()  # открытие авторизации


# окно самого мессенджера
class MessengerWindow(QtWidgets.QMainWindow, clientui.Ui_messenger_window):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.messagesPush.clicked.connect(self.send_message)
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
            self.messagesBox.append('Введите сообщение ')
            self.messagesBox.append('')
            self.messagesBox.repaint()
            return

        # очистка строки отправки сообщения
        self.messagesInput.clear()
        self.messagesInput.repaint()


if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    registration_window = Registration()
    window = Authorization()
    messenger = MessengerWindow()
    window.show()
    sys.exit(app.exec_())
