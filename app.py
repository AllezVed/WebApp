import sqlite3
from flask import *
app = Flask (__name__)


DATABASE = 'test_db.db'

@app.route('/')
def index():
    # site_list = list_function()
    site_list = [site for site in query_db('SELECT DISTINCT LocationID from meter')]
    select = request.args.get('select_me')
   
    print(site_list)
    # d3_source = query_db('SELECT tstamp, Reading from meter WHERE LocationID = ? ', (str(select),))
    # print(d3_source)
   
    return render_template('index.html', sites = site_list)
# def connect_db():
#     """Connects to the specific database."""
#     rv = sqlite3.connect(DATABASE)
#     rv.row_factory = sqlite3.Row
#     return rv
# def get_db():
#     """Opens a new database connection if there is none yet for the
#     current application context.
#     """
#     if not hasattr(g, 'testdb'):
#         g.testdb = connect_db()
#     return g.testdb

def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)

        db.row_factory = sqlite3.Row
    return db
    

@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

def query_db(query, args=(), one=False):
    cur = get_db().execute(query, args)
    rv = cur.fetchall()
    cur.close()
    return (rv[0] if rv else None) if one else rv

# @app.teardown_appcontext
# def close_db(error):
#     """Closes the database again at the end of the request."""
#     if hasattr(g, 'testdb'):
#         g.testdb.close()

@app.route('/<path:path>')
def static_proxy(path):
  # send_static_file will guess the correct MIME type
  return app.send_static_file(path)


@app.route('/test', methods = ['GET', 'POST'])
def test():
    select = request.form['select_me']
    return(str(select)) # to see value of select


if __name__ == '__main__':
    app.run(debug = True)