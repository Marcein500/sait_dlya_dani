from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def home():
    # Открываем созданную HTML страницу
    return render_template("index.html")


if __name__ == "__main__":
    print("=== ВЕБ-СЕРВЕР BANZAI OS УСПЕШНО ЗАПУЩЕН ===")
    print("Ссылка для теста на своем ПК: http://127.0.0.1:5000")
    # Запускаем сайт на порту 5000
    app.run(host="0.0.0.0", port=5000, debug=True)
