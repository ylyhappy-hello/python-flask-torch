from flask import Flask
from flask_cors import cross_origin

from yolov5.detect_product import run
import os
from minio_upload.file_uploader import upload_file

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


@app.route("/api/ai/video-helmet-detect/<path:video_url>")
@cross_origin()
def video_helmet_detect(video_url):
    try:
        file_path = run(weights="/home/yly/evm/python-flask/yolov5/5-epoch-yolov5s-best-91000.pt", source=video_url)
        save_path = os.getcwd() + "/" + file_path
        print(save_path)
        try:
            video_detect_url = upload_file("ruoyi", file_path, save_path)
            return {
                "msg": "ok",
                "data": video_detect_url,
            }
        except IOError:
            print(IOError)
    except IOError:
        print(IOError)

# @app.route("/api/ai/video-helmet-detect", methods=['POST'])
# def video_helmet_detect(video_url):
#     return f"<p>{video_url}</p>"
