from flask import Flask, render_template
import os

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

# Eğer başka route’lar ekleyeceksen buraya ekleyebilirsin

if __name__ == "__main__":
    # Render deploy sırasında PORT ortam değişkeni veriyor, yoksa local için 5000
    port = int(os.environ.get("PORT", 5000))
    # host=0.0.0.0 ile dış dünyaya açıyoruz
    # debug=True ile geliştirme modunu aktif tutuyoruz
    app.run(host="0.0.0.0", port=port, debug=True)
