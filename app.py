from flask import Flask, render_template_string, redirect, url_for

app = Flask(__name__)

# --- GIAO DIỆN TỔNG THỂ (CSS) ---
COMMON_STYLE = '''
<style>
    body { font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; background-color: #f4f7f6; display: flex; flex-direction: column; align-items: center; justify-content: center; height: 100vh; margin: 0; }
    .card { background: white; padding: 2rem; border-radius: 15px; box-shadow: 0 10px 25px rgba(0,0,0,0.1); text-align: center; width: 350px; }
    .btn { background-color: #28a745; color: white; padding: 12px 24px; text-decoration: none; border-radius: 8px; display: inline-block; margin-top: 20px; transition: 0.3s; border: none; cursor: pointer; font-size: 16px; }
    .btn:hover { background-color: #218838; transform: scale(1.05); }
    .btn-blue { background-color: #007bff; }
    .btn-blue:hover { background-color: #0069d9; }
</style>
'''

# --- LINK CHÍNH (TRANG CAPTCHA) ---
@app.route('/')
def index():
    return COMMON_STYLE + '''
    <div class="card">
        <h2>Xác minh bảo mật</h2>
        <p>Vui lòng xác nhận bạn không phải là Robot để tiếp tục.</p>
        <div style="border: 1px solid #ccc; padding: 15px; background: #fafafa; border-radius: 5px; display: flex; align-items: center; gap: 10px; margin: 20px 0;">
            <input type="checkbox" id="captcha" style="width: 25px; height: 25px; cursor: pointer;" onclick="setTimeout(() => { window.location.href='/home' }, 500)">
            <label for="captcha" style="cursor: pointer;">Tôi không phải là người máy</label>
            <img src="https://upload.wikimedia.org/wikipedia/commons/a/ad/RecaptchaLogo.svg" width="30" style="margin-left: auto;">
        </div>
    </div>
    '''

# --- LINK 2 (TRANG HOME) ---
@app.route('/home')
def home():
    return COMMON_STYLE + '''
    <div class="card" style="width: 500px;">
        <h1>🏠 Trang Chủ Hacker Ninh Hòa</h1>
        <p>Chào mừng bạn đã vượt qua bài kiểm tra Robot! Đây là nơi chứa các thông tin quan trọng nhất.</p>
        <div style="text-align: left; background: #e9ecef; padding: 15px; border-radius: 8px; margin: 20px 0;">
            <li>🔥 Dự án: Học lập trình Python</li>
            <li>🚗 Sở thích: Siêu xe McLaren & Nissan GT-R</li>
            <li>💪 Tập luyện: Calisthenics (Planche)</li>
        </div>
        <a href="/links" class="btn btn-blue">Khám phá các link khác ➔</a>
    </div>
    '''

# --- LINK 3 (DANH SÁCH LINK TỰ GẮN) ---
@app.route('/links')
def other_links():
    return COMMON_STYLE + '''
    <div class="card">
        <h2>🔗 Danh mục liên kết</h2>
        <p>Chọn nơi bạn muốn đến:</p>
        <a href="https://www.roblox.com" class="btn" style="background: #ce1126; width: 80%;">Vào Roblox</a><br>
        <a href="https://google.com" class="btn" style="background: #4285F4; width: 80%;">Tìm kiếm Google</a><br>
        <a href="/" class="btn" style="background: #6c757d; width: 80%;">Quay lại từ đầu</a>
        <a href="https://www.facebook.com/share/1JKumr9zp1/" class="btn" style="background: #1DA1F2; width: 80%;">Facebook</a><br>
    </div>
    '''

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
    
