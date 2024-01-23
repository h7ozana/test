from flask import Flask, render_template, request

app = Flask(__name__)

# 간단한 메시지 리스트를 유지하기 위한 리스트
messages = []


@app.route('/')
def index():
    return render_template('index.html', messages=messages)


@app.route('/post_message', methods=['POST'])
def post_message():
    # POST 요청으로부터 메시지를 받아서 리스트에 추가
    message = request.form.get('message')
    messages.append(message)
    return render_template('index.html', messages=messages)


if __name__ == '__main__':
    app.run(host='0.0.0.0')






#from flask import Flask
#app = Flask(__name__)

#@app.route('/')
#def hello_world():
#    return 'ohcloud 20240121'
