from flask import *
app = Flask (__name__)


DATABASE = 'testdb.db'

@app.route('/')
def index():
    
    return render_template('index.html')
def connect_db():
    """Connects to the specific database."""
    rv = sqlite3.connect(DATABASE)
    rv.row_factory = sqlite3.Row
    return rv
def get_db():
    """Opens a new database connection if there is none yet for the
    current application context.
    """
    if not hasattr(g, 'testdb'):
        g.testdb = connect_db()
    return g.testdb

@app.teardown_appcontext
def close_db(error):
    """Closes the database again at the end of the request."""
    if hasattr(g, 'testdb'):
        g.testdb.close()

@app.route('/<path:path>')
def static_proxy(path):
  # send_static_file will guess the correct MIME type
  return app.send_static_file(path)

if __name__ == '__main__':
    app.run(host = '0.0.0.0', port='80')