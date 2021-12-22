from flask import Flask, request
import requests
from collections import Counter

app = Flask(__name__)


@app.route('/')
def ping_service():
    return '<김동현:Commander_con>'


@app.route('/ping')
def do_ping():
    general_con_list = ['p2_general1_con', 'p2_general2_con', 'p2_general3_con', 'p2_general4_con']
    general_con_port = ['5001', '5002', '5003', '5004']

    ping = '김동현'

    response_result = []
    for general_con, general_port in zip(general_con_list, general_con_port):
        try:
            response = requests.get('http://' + general_con + ':' + general_port + '/pong?token=' + ping)
        except requests.exceptions.RequestException as e:
            print('\n Cannot reach the pong service.\n')
            return 'ERROR\n'

        response_result.append(response.text)

    result = '''<h2>====컨테이터가 가진 토큰====</h2>
<p>p2_general1_con:김동현</p>
<p>p2_general2_con:김동현</p>
<p>p2_general3_con:FAULT // 비잔틴</p>
<h2>====각 컨테이너가 합의 후 판단한 메시지====</h2>
    '''
    result += str.join('\n', response_result)

    result += '<h2>====결과====</h2>'
    if result.count('FAULT') * 3 + 1 <= len(general_con_list):
        result += '\n<p>합의 가능</p>'
    else:
        result += '\n<p>합의 불가능</p>'

    print(result)

    return result


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
