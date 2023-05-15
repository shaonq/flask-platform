from flask import Flask, send_file
from gevent import pywsgi
from router.api import router_api
from router.upload import router_upload
from model.database import db


# flask init , set static path
app = Flask(__name__, static_folder='../dist/assets', static_url_path='/assets')

app.config.from_object("config")

# db
db.init_app(app)

# blueprint
app.register_blueprint(router_api)
app.register_blueprint(router_upload)


@app.route('/')
def index():
    return send_file(app.config["VUE_INDEX"])


if __name__ == '__main__':
    # app.run(host='0.0.0.0',port=5000, debug=False)
    server = pywsgi.WSGIServer(('0.0.0.0', 5000), app)
    server.serve_forever()
