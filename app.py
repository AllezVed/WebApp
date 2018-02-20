from flask import *
app = Flask (__name__)

@app.route('/')
def index():

    return render_template('index.html')

@app.route('/<path:path>')
def static_proxy(path):
  # send_static_file will guess the correct MIME type
  return app.send_static_file(path)

if __name__ == '__main__':
    app.run(host = '0.0.0.0' )