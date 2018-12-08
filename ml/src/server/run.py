import bottle
import psycopg2

from midi_feature_extraction.migrate import make_migrations, migrate
from cheroot.wsgi import Server as WSGIServer

conn = None
app = bottle.Bottle()


@app.route("/<midi:re:[\.0-9a-zA-Z_-]*>/rawfeature/<feature:re:[0-9a-zA-Z_-]*>")
def foo(midi, feature):
    print("lul kek")
    cur = conn.cursor()
    feature = feature.replace(" ", "_")
    feature = feature.replace("-", "_")
    feature = feature.lower()
    query = "SELECT {} FROM midifeatures WHERE filename = '{}';".format(feature, midi)
    cur.execute(query)
    value = cur.fetchone()[0]
    cur.close()
    return str(value)


@app.route("/manage/update_midifeatures")
def bar():
    conn = psycopg2.connect(host="database", user="postgres",
                            password="postgres", dbname="mldata")
    if make_migrations(conn) > 0:
        migrate(conn)
    conn.close()


def main():
    global conn
    conn = psycopg2.connect(host="database", user="postgres",
                            password="postgres", dbname="mldata")
    server = WSGIServer(('0.0.0.0', 9000), app, server_name='ml', numthreads=2)
    server.start()
    conn.close()


if __name__ == "__main__":
    main()