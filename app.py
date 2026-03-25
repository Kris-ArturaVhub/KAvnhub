from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def index():
    return '''
        <form action="/login" method="post">
            Username: <input type="text" name="username"><br>
            Password: <input type="password" name="password"><br>
            <input type="submit" value="Đăng nhập">
        </form>
    '''

@app.route('/login', methods=['post'])
def login():
    uname = request.form.get('username')
    # ĐÂY LÀ DÒNG CODE LỖI GIẢ LẬP:
    if uname == "admin' OR '1'='1":
        return "<h1>HACK THÀNH CÔNG! Chào mừng đại ca Admin.</h1>"
    else:
        return "<h1>Đăng nhập thất bại. Thử lại đi 'gà'!</h1>"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)

