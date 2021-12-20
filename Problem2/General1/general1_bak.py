from flask import Flask, request
import requests
from collections import Counter
import time

app = Flask(__name__)
general_token = ''


@app.route('/')
def pong_service():
    return '[receiver_pong] Hello, I am pong container! nice to meet you!'


@app.route('/ping')
def do_ping():
    # 1초 쉬었다가 보내기
    time.sleep(1)
    general_con_list = ['p2_general2_con', 'p2_general3_con', 'p2_general4_con']
    general_con_port = ['5002', '5003', '5004']

    # 현재 컨테이너가 받을 토큰 저장
    response_result = []
    for general_con, general_port in zip(general_con_list, general_con_port):
        response = ' '
        try:
            response = requests.get('http://' + general_con + ':' + general_port + '/pong2')
        except requests.exceptions.RequestException as e:
            print('\n Cannot reach the pong service.\n')
            return 'ERROR\n'

        response_result.append(response.text)

    # 최빈값 찾기
    cnt = Counter(response_result)
    result = cnt.most_common()

    # 최빈값이 2개라면 FAULT 반환
    if len(result) > 1:
        if result[0][1] == result[1][1]:
            result = 'FAULT'
        else:
            result = result[0][0]
    else:
        result = result[0][0]

    result = '<general1 : ' + result + '>'
    return result


@app.route('/pong')
def do_pong():
    global general_token
    param = request.args.to_dict()

    # 파라미터가 없으면 오류 출력
    if len(param) == 0:
        return 'No param Error'

    # 내가 받은 토큰 설정
    general_token = param['token']

    # 다른 general로부터 token 파라미터 결과값 가져오고
    # 비교 출력

    return do_ping()


# pong2 하면 커맨더로 부터 받은 토큰 주기
@app.route('/pong2')
def do_pong2():
    global general_token

    return general_token


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5001, debug=True)
