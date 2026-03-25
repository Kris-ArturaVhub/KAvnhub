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

@app.route('/home')
def home():
    return "<h1>Chào mừng bạn đã đến với trang HOME!</h1><p>Đây là link con đầu tiên của bạn.</p>"

@app.route('/roblox')
def roblox_page():
    return "<h1>Trang Fan của Roblox</h1><p>Bạn có thích chơi Blox Fruit không?</p>"
    
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)

