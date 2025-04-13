from flask import Flask
from flask import render_template
from flask import request

app = Flask(__name__)


@app.route("/")
def home():
    web_tittle = "Halaman Utama"
    return render_template("home.html", tittle=web_tittle)

@app.route("/usia/", methods=["GET", "POST"])
def cek_usia():
    web_tittle = "Pengecekan Usia Berdasarkan Tahun Lahir" 
    if request.method=="POST":
        tahun_lahir = int(request.form['tahun_lahir'])
        tahun_sekarang = 2025
        usia = tahun_sekarang - tahun_lahir
        return render_template("usia.html", tittle=web_tittle, usia=usia)
    return render_template("usia.html", tittle=web_tittle, usia=None)