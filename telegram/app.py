from flask import Flask, request
import random
from utils import send_msg

app = Flask('hi')

@app.route('/', methods = ['POST']) # /이고 메소드가 post이면 home함수 실행하라
def home():
    # 서버로서 우리가 받은 요청 -> server
    data = request.json
    input_msg = data['message']['text']
    sender_id = data['message']['from']['id']

    # 우리가 보내는 요청 -> client
    if input_msg == '안녕' :
        send_msg("그래 안녕?", sender_id)
    elif input_msg == '로또':
        lotto = random.sample(range(1, 46), 6)
        send_msg(lotto, sender_id)
    else :
        send_msg('똑바로 입력할래?', sender_id)
    return 'Hello Server!'



app.run(port = 80, debug = True)