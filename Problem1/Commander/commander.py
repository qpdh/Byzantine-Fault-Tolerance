from flask import Flask
import requests
from collections import Counter

app = Flask(__name__)


@app.route('/')
def ping_service():
    return '<김동현:Commander_con>'


@app.route('/ping')
def do_ping():
    general_con_list = ['p1_general1_con', 'p1_general2_con', 'p1_general3_con']
    general_con_port = ['5001', '5002', '5003']

    ping = '김동현'

    response_result = []
    for general_con, general_port in zip(general_con_list, general_con_port):
        response = ' '
        try:
            response = requests.get('http://' + general_con + ':' + general_port + '/pong?token=' + ping)
        except requests.exceptions.RequestException as e:
            print('\n Cannot reach the pong service.\n')
            return 'ERROR\n'

        response_result.append(response.text)

    result = str.join('\n', response_result)

    if result.count('홍길동') * 3 + 1 <= len(general_con_list):
        result += '\n합의 가능'
    else:
        result += '\n합의 불가능'

    print(result)

    return result


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
