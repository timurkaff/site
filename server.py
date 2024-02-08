from flask import Flask, request, jsonify
from flask_cors import CORS
import json
import os

app = Flask(__name__)
CORS(app)

def check_credentials(login, password):
    credentials_path = os.path.join('user_credentials', f'{login}.json')

    if os.path.exists(credentials_path):
        with open(credentials_path, 'r') as file:
            stored_credentials = json.load(file)
            return stored_credentials.get('password') == password

    return False

def add_user(login, password):
    credentials_path = os.path.join('user_credentials', f'{login}.json')

    # Проверка, существует ли файл с таким логином
    if os.path.exists(credentials_path):
        return jsonify({'status': 'error', 'message': 'Пользователь с таким логином уже существует'})

    credentials = {'login': login, 'password': password}

    if not os.path.exists('user_credentials'):
        os.makedirs('user_credentials')

    with open(credentials_path, 'a') as file:
        json.dump(credentials, file)
        file.write('\n')

    return jsonify({'status': 'success', 'message': 'Пользователь успешно добавлен'})

@app.route('/post', methods=['POST'])
def save_credentials():
    try:
        data = request.get_json()
        login = data.get('login')
        password = data.get('password')

        if login and password:
            return add_user(login, password)
        else:
            return jsonify({'status': 'error', 'message': 'Неверный формат данных'})

    except Exception as e:
        return jsonify({'status': 'error', 'message': str(e)})

@app.route('/check_login', methods=['GET'])
def check_login():
    try:
        login = request.args.get('login')
        password = request.args.get('password')

        if login and password:
            if check_credentials(login, password):
                return jsonify({'status': 'success', 'message': 'Аутентификация успешна'})
            else:
                return jsonify({'status': 'error', 'message': 'Неправильные учетные данные'})
        else:
            return jsonify({'status': 'error', 'message': 'Не правильный формат'})

    except Exception as e:
        return jsonify({'status': 'error', 'message': str(e)})

if __name__ == '__main__':
    app.run(port=5000)