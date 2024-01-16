from flask import Flask, render_template, request

SECRET_KEY = 'hgbhgvghv'
DEBUG = True


app = Flask(__name__)

@app.route('/')
def index():
    return 'hello world'

@app.route('/index')
def index_hyml():
    name = 'Bill'
    return render_template('index.html', name=name)

@app.route('/path/<order_id>')
def path_funk(order_id):
    return render_template('order_id.html', order_id=order_id)

@app.route('/queri')
def queri_funk():
    data = dict(request.args)
    print("ARDS", data)
    return render_template('queri.html', data=data)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        user = request.form.get('user')
        psw = request.form.get('psw')
        print(f'User: {user}, passw: {psw}')
    return render_template('login.html')

if __name__ == '__main__':
    app.run('0.0.0.0', port=5001)