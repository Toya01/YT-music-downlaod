from flask import Flask, request, jsonify, render_template, Response
import requests
import urllib.parse

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/search")
def search():
    query = request.args.get("query", "")
    url = f"https://dns-ruby.vercel.app/search?query={urllib.parse.quote(query)}"
    return jsonify(requests.get(url).json())

@app.route("/ytmp3")
def ytmp3():
    video_url = request.args.get("url", "")
    url = f"https://dens-audio.vercel.app/api/ytmp3?url={urllib.parse.quote(video_url)}"
    return jsonify(requests.get(url).json())

@app.route("/download")
def download():
    file_url = request.args.get("url")
    r = requests.get(file_url, stream=True)

    def generate():
        for chunk in r.iter_content(8192):
            if chunk:
                yield chunk

    return Response(
        generate(),
        headers={"Content-Disposition": "attachment; filename=song.mp3"},
        content_type="audio/mpeg"
    )
