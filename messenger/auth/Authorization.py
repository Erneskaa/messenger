from PyQt5 import QtWidgets
import requests
from messenger.auth import authui


class Authorization(QtWidgets.QMainWindow, authui.Ui_authorization):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.pressed.connect(self.send_login)

    def send_login(self):
        login = self.login.text()
        password = self.password.text()
        try:
            response = requests.post(
                'http://127.0.0.1:5000/auth',
                json={'login': login, 'password': password}
            )
        except:
            print('Упс.. что-то пошло не так')
            return


app = QtWidgets.QApplication([])
window = Authorization()
window.show()
app.exec_()
