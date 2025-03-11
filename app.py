from flask import Flask, render_template, request, send_file
from pytube import YouTube
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/download', methods=['POST'])
def download():
    try:
        url = request.form['url']
        yt = YouTube(url)
        video = yt.streams.get_highest_resolution()
        file_path = video.download()

        return send_file(file_path, as_attachment=True)
    except Exception as e:
        return f"Σφάλμα: {str(e)}"

if __name__ == '__main__':
    app.run(debug=True)
