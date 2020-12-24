from flask import Flask, request, abort
from datetime import datetime
import time

app = Flask(__name__)
# база данных (условная)
db = []

users = []


@app.route("/")
def hello():
    return "<a href='/status'> Статистика <a>  " \
           "<a href='/auth_logs'>Логины и пароли<a> " \
           "<a href='/messages'>Сообщения<a>"


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
    # получение токина (логин и сообщение)
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


# отправляем логин и пароль
@app.route("/auth", methods=['POST'])
def send_auth():
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


# получаем базу участников
@app.route("/auth_logs")
def get_auth():
    return {'auth': users}


app.run()
