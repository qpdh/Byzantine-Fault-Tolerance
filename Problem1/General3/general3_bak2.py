from flask import Flask, request

app = Flask(__name__)


@app.route('/')
def pong_service():
    return '[general3]'


@app.route('/pong')
def do_pong():
    param = request.args.to_dict()

    # 파라미터가 없으면 오류 출력
    if len(param) == 0:
        return 'No param Error'

    return '<general3 : 홍길동>'


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5003, debug=True)
