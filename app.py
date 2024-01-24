from flask import Flask, render_template
from werkzeug.urls import url_quote  # 추가된 부분

app = Flask(__name__)

@app.route('/')
def index():
    messages = ['공지사항']  # 원하는 공지사항 목록으로 변경
    return render_template('index.html', messages=messages)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')





#from flask import Flask
#app = Flask(__name__)

#@app.route('/')
#def hello_world():
#    return 'ohcloud 20240121'
