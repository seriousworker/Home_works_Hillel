from flask import Flask, render_template
import sqlite3

app = Flask(__name__)


def get_connection():
    conn = sqlite3.connect('example.sqlite3')
    conn.row_factory = sqlite3.Row
    return conn


@app.route('/best_selling/<int:lines>')
def get_tracks_data(lines):
    conn = get_connection()
    songs = conn.execute("SELECT tr.TrackId AS 'id', tr.Name AS 'name', COUNT(ii.Quantity) AS 'sold_qu', SUM(ii.UnitPrice) AS 'total_price' "
                         "FROM tracks AS tr "
                         "JOIN invoice_items AS ii ON ii.TrackId = tr.TrackId "
                         "GROUP BY tr.TrackId ORDER BY SUM(ii.UnitPrice) DESC LIMIT ?;", (lines,)).fetchall()
    conn.close()
    return render_template('index.html', songs=songs, lines=lines)


app.run(port=5040)
