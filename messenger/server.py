from flask import Flask, request, abort
from datetime import datetime
import time

app = Flask(__name__)
# база данных (условная)
db = []


@app.route("/")
def hello():
    return "Hello, World! <a href='/status'> Статистика <a>"


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
    if not isinstance(request.json, dict):
        return abort(400)

    name = request.json.get('name')
    text = request.json.get('text')

    if not isinstance(text, str) or not isinstance(name, str):
        return abort(400)
    if text == '' or name == '':
        return abort(400)

    db.append({
        'text': request.json['text'],
        'name': request.json['name'],
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
            # pagination - чтобы возвращать сообщения партиями
            if len(filtered_db) >= 100:
                break
    return {'messages': filtered_db}


app.run()
