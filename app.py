import requests
from flask import Flask, render_template, request

app = Flask(__name__)

# НАСТРОЙКИ TELEGRAM
TELEGRAM_TOKEN = '8773383067:AAG1dK0iiijAWO6pDiSWSTXWsSVDwCCBpko'
TELEGRAM_CHAT_ID = '1096704043'

def send_telegram_message(text):
    url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
    payload = {
        'chat_id': TELEGRAM_CHAT_ID,
        'text': text,
        'parse_mode': 'HTML'
    }
    try:
        requests.post(url, data=payload)
    except Exception as e:
        print(f"Ошибка отправки в TG: {e}")

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    name = request.form.get('name')
    phone = request.form.get('phone')
    course = request.form.get('course')

    message = (
        f"<b>🚀 Новая заявка!</b>\n\n"
        f"<b>👤 Имя:</b> {name}\n"
        f"<b>📞 Телефон:</b> {phone}\n"
        f"<b>📚 Курс:</b> {course}"
    )

    send_telegram_message(message)
    # Возвращаем статус 200 (ОК) без текста, чтобы JS показал модалку
    return '', 200

if __name__ == '__main__':
    app.run(debug=True)