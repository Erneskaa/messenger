import time
from datetime import datetime

from flask import Flask, request, abort

app = Flask(__name__)
# база данных (условная)
db = []

users = []

admin_default_log = [{
    'admin_login': 'admin',
    'admin_password': '123456'
}]


@app.route("/")
def hello():
    return "<a href='/status'> Статистика <a>  " \
           " <a href='/auth_logs'>Логины и пароли<a>" \
           " <a href='/messages'>Сообщения<a>"


# статус сервера
@app.route("/status")
def status():
    return {
        'status': True,
        'name': 'Messenger',
        'time': time.time(),
        'time1': datetime.now().strftime('%H:%M:%S %d/%m/%Y')
    }


# отправка сообщений
@app.route("/send", methods=['POST'])
def send_messages():
    print(request.json)
    # проверка токена на формат json
    if not isinstance(request.json, dict):
        return abort(400)
    # получение токена (логин и сообщение)
    text = request.json.get('text')
    login = request.json.get('login')
    # проверка на пустоту текста
    if not isinstance(text, str):
        return abort(400)
    if text == '':
        return abort(400)
    # добавление в базу данных
    db.append({
        'text': text,
        'login': login,
        'time': time.time()
    })
    return {'ok': True}


# приходящие сообщения
@app.route('/messages')
def get_messages():
    if 'after' in request.args:
        print(request.args['after'])
        try:
            # проверка формата after
            after = float(request.args['after'])
        except:
            print('error')
            # дефолтное состояние
            return abort(400)
    else:
        after = 0

    filtered_db = []
    for message in db:
        if message['time'] > after:
            filtered_db.append(message)
            if len(filtered_db) >= 100:
                break
    return {'messages': filtered_db}


# отправляем форму регистрации
@app.route("/registration", methods=['POST'])
def send_reg_form():
    try:
        login = request.json.get('login')
        password = request.json.get('password')
        confirm_pass = request.json.get('confirm_password')
        if login != '' or password != '' or confirm_pass != '':
            if password == confirm_pass:
                users.append({
                    'login': login,
                    'password': password
                })
    except:
        return abort(400)


# отправляем логин и пароль
@app.route("/auth", methods=['POST'])
def send_auth():
    try:
        # получение токенов из окна авторизации (логин и пароль)
        login = request.json.get('login')
        password = request.json.get('password')
        # проверка формата
        if not isinstance(login, str) or not isinstance(password, str):
            return abort(400)
        if login == '' or password == '':
            return abort(400)

        # добавление в отдельную базу данных пользователей
        users.append(
            {
                'login': login,
                'password': password,
            })
        return {'login': login, 'password': password}
    except:
        print('что-то пошло не так')


# получаем базу участников
@app.route("/auth_logs")
def get_auth():
    return {'auth': users}


app.run()
