from flask import Flask, render_template_string, redirect, url_for, request, session
import requests

app = Flask(__name__)
app.secret_key = 'kris_artura_2026'

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

# --- TRANG CHỦ (CÓ PASS + RECAPTCHA) ---
@app.route('/')
def captcha():
    # Anh nhớ thay SITE_KEY của anh vào đây nhé
    SITE_KEY = "6LeA3JksAAAAAKEYSY3MDVtN6YJkdN_-JJiSwNtU"
    return COMMON_STYLE + f'''
    <script src="https://www.google.com/recaptcha/api.js" async defer></script>
    <div class="card">
        <h2>KAVNHUB SECURITY</h2>
        <form action="/verify" method="post">
            <input type="password" name="user_key" placeholder="Nhập mã truy cập..." 
                   style="padding: 12px; width: 80%; border-radius: 8px; border: 1px solid #ddd; margin-bottom: 20px;">
            <div class="g-recaptcha" data-sitekey="{SITE_KEY}" style="margin-bottom: 20px; display: flex; justify-content: center;"></div>
            <button type="submit" class="btn btn-blue" style="width: 100%;">XÁC NHẬN</button>
        </form>
    </div>
    '''

@app.route('/verify', methods=['POST'])
def verify():
    user_pass = request.form.get('user_key')
    captcha_res = request.form.get('g-recaptcha-response')
    
    # Anh nhớ thay SECRET_KEY của anh vào đây
    SECRET_KEY = "6LeA3JksAAAAAG097PtdygLJZGGwVekNckKmixpR"

    if user_pass != "ArturaVhub":
        return 'Sai mã rồi! <a href="/">Quay lại</a>'

    if not captcha_res:
        return 'Vui lòng tick vào ô "Tôi không phải người máy"! <a href="/">Quay lại</a>'

    v = requests.post('https://www.google.com/recaptcha/api/siteverify', data={
        'secret': SECRET_KEY,
        'response': captcha_res
    }).json()

    if v.get('success'):
        session['is_logged_in'] = True
        return redirect(url_for('home'))
    else:
        return 'Xác thực Captcha thất bại! <a href="/">Thử lại</a>'

# --- TRANG HOME (GIỮ NGUYÊN CODE CỦA ANH) ---
@app.route('/home')
def home():
    if not session.get('is_logged_in'):
        return redirect(url_for('captcha'))
        
    return COMMON_STYLE + '''
    <style>
        body { height: auto; padding: 20px 0; display: block; } 
        .container { max-width: 800px; margin: 0 auto; background: white; border-radius: 20px; box-shadow: 0 10px 30px rgba(0,0,0,0.1); overflow: hidden; padding-bottom: 30px; }
        .music-player { background: #f8f9fa; padding: 15px; border-radius: 10px; margin: 20px 0; display: flex; align-items: center; justify-content: center; }
        .info-grid { display: grid; grid-template-columns: 1fr 1fr; gap: 20px; margin-top: 20px; }
        .info-box { background: #eef2f7; padding: 15px; border-radius: 10px; border-left: 5px solid #007bff; }
    </style>

    <div class="container">
         <div style="text-align:center; padding: 20px;">
            <img src="https://github.com/Kris-ArturaVhub/KAvnhub/raw/main/Screenshot_2026-anhnen.jpg" alt="..." style="width: 200px; border-radius: 10px;">
         </div>

        <div style="padding: 30px; text-align: left;">
            <h1>🚀 KAvnhub_space </h1>
            <p style="color: #666;">Chào mừng bạn đến với không gian ảo. Đây là nơi tôi lưu trữ các links.</p>

            <div class="music-player">
                <p style="margin-right: 15px; font-weight: bold;">🎵 Đang phát:</p>
                <audio controls autoplay loop>
                    <source src="https://github.com/Kris-ArturaVhub/KAvnhub/raw/main/livingroomsong.mp3" type="audio/mpeg">
                </audio>
            </div>

            <div class="info-grid">
                <div class="info-box">
                    <h3>👤 Profile</h3>
                    <p>Bí danh: Kris_Artura <br>Genz <br>Vị trí: Khánh Hòa, VN</p>
                </div>
                <div class="info-box" style="border-left-color: #28a745;">
                    <h3>💻 profile</h3>
                    <p>• Python / Flask<br>• SQL Injection (Basic)<br>• sdt: 84+799.269_197</p>
                </div>
            </div>

            <div style="margin-top: 30px;">
                <h3>📜: </h3>
                <p> Version 1.0, đảm bảo an toàn tuyệt đối🛡️.</p>
            </div>

            <div style="text-align: center; margin-top: 40px;">
                <a href="/links" class="btn btn-blue" style="width: 200px;">Khám phá thêm ➔</a><br>
                <a href="https://www.facebook.com/share/1JKumr9zp1/" class="btn" style="background: #1DA1F2; width: 40%;">Facebook</a><br>
                <a href="https://www.tiktok.com/@ka.19920425?_r=1&_t=ZS-950s2mflaGA" class="btn" style="background: #ce1126; width: 40%;">Tiktok</a><br>
            </div>
        </div>
    </div>
    <p style="text-align: center; color: #aaa; margin-top: 20px;">© 2024 10110 Web Project</p>
    '''

@app.route('/links')
def other_links():
    if not session.get('is_logged_in'):
        return redirect(url_for('captcha'))
    return COMMON_STYLE + '''
    <div class="card">
        <h2>🔗 Danh mục liên kết</h2>
        <p>Chọn nơi bạn muốn đến:</p>
        <a href="https://www.roblox.com" class="btn" style="background: #ce1126; width: 80%;">Vào Roblox</a><br>
        <a href="https://google.com" class="btn" style="background: #4285F4; width: 80%;">Tìm kiếm Google</a><br>
        <a href="/home" class="btn" style="background: #6c757d; width: 80%;">Quay lại trang chủ</a>
    </div>
    '''

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
