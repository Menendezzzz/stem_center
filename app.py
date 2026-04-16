from flask import Flask, render_template, request
import requests

app = Flask(__name__)

BOT_TOKEN = "8773383067:AAG1dK0iiijAWO6pDiSWSTXWsSVDwCCBpko"
CHAT_ID = "1096704043"


def send_to_telegram(name, phone, course):
    text = f"""
📥 Новая заявка

Имя: {name}
Телефон: {phone}
Курс: {course}
"""

    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"

    requests.post(url, data={
        "chat_id": CHAT_ID,
        "text": text
    })


@app.route('/')
def home():
    return render_template('index.html')


# 🔴 ВОТ ЭТО ОБЯЗАТЕЛЬНО ДОЛЖНО БЫТЬ
@app.route('/signup', methods=['POST'])
def signup():
    name = request.form['name']
    phone = request.form['phone']
    course = request.form['course']

    send_to_telegram(name, phone, course)

    return "Заявка отправлена!"


if __name__ == '__main__':
    app.run(debug=True)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)