from flask import Flask,render_template, request
from prediction import print_songs

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/songs', methods=["POST"])
def songs():
    mood = request.form.get("mood")
    # print_songs(mood)
    song_info = print_songs(mood)
    l = []
    for _, row in song_info.iterrows():
        s = []
        s.append(row['song'])
        s.append(row['singer'])
        l.append(s)
    return render_template("song.html", songs=l)


