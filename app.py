import sqlite3
import csv
from datetime import datetime
import json
import StringIO
from flask import *
app = Flask (__name__)


DATABASE = 'C:/Users/hvkumar/Documents/Atlanta/FlaskTest/test_db.db'

@app.route('/', methods = ['GET', 'POST'])
def index():
    # site_list = list_function()
    site_list = [site for site in query_db('SELECT DISTINCT LocationID from meter')]
    # select = str(request.form.get('select_me'))
    if request.method == "POST":
        select = str(request.form.get('select_me'))
        d3_source = [{"Timestamp":row[0], "Reading" : row[1]} for row in query_db('SELECT tstamp, Reading from meter WHERE LocationID = ? ', (select,))]
    # print(str(d3_source))

        with open("./static/"+select+".csv",'w', newline ='') as f:
            #Using Dict Keys as fieldnames for CSV file header
            writer = csv.DictWriter(f,d3_source[0].keys())
            writer.writeheader()
            for d in d3_source:
                writer.writerow(d)
        
        
    # print(site_list)
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
    select = str(request.form.get('select_me'))
    d3_source = [{"Timestamp":row[0], "Reading" : row[1]} for row in query_db('SELECT tstamp, Reading from meter WHERE LocationID = ? ', (select,))]
    # print(str(d3_source))

    with open("./static/"+select+".csv",'w', newline ='') as f:
        #Using Dict Keys as fieldnames for CSV file header
        writer = csv.DictWriter(f,d3_source[0].keys())
        writer.writeheader()
        for d in d3_source:
            writer.writerow(d)
   
    return str(d3_source) # to see value of select

@app.route('/test_one')
def test_one():
    
    q_string = request.args.get('query')
    d3_source = [{"Timestamp":row[0], "Reading" : row[1]} for row in query_db('SELECT tstamp, Reading from meter WHERE LocationID = ? ', (q_string,))]
    d3_source_json = json.dumps(d3_source)
    return d3_source_json

@app.route('/return_csv')
def return_csv():
    

    

if __name__ == '__main__':
    app.run(debug = True)