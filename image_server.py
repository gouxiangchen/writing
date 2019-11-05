# encoding:utf8
__author__ = 'sijiu'

from flask import Response, Flask, request

app = Flask(__name__)

@app.route("/image", methods=['post', 'get'])
def index():
    path = request.args.get('path')
    print(path)
    path = "E:/image_server/%s" % path

    resp = Response(open(path, 'rb'), mimetype="image/png;image/jpeg;image/x-ms-bmp;image/gif")
    return resp

app.run(host='0.0.0.0',port=4949, debug=True)