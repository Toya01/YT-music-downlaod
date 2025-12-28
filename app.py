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
    if not query:
        return jsonify({"error": "Query required"})

    url = f"https://dns-ruby.vercel.app/search?query={urllib.parse.quote(query)}"
    res = requests.get(url)
    return jsonify(res.json())

@app.route("/ytmp3")
def ytmp3():
    video_url = request.args.get("url", "")
    if not video_url:
        return jsonify({"error": "URL required"})

    url = f"https://dens-audio.vercel.app/api/ytmp3?url={urllib.parse.quote(video_url)}"
    res = requests.get(url)
    return jsonify(res.json())

# 🔽 THIS IS THE IMPORTANT PART 🔽
@app.route("/download")
def download():
    file_url = request.args.get("url")
    if not file_url:
        return "Missing file URL", 400

    r = requests.get(file_url, stream=True)

    def generate():
        for chunk in r.iter_content(chunk_size=8192):
            if chunk:
                yield chunk

    headers = {
        "Content-Disposition": "attachment; filename=song.mp3"
    }

    return Response(generate(), headers=headers, content_type="audio/mpeg")

if __name__ == "__main__":
    app.run(debug=True)
