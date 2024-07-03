from flask import Flask, jsonify
from flask_cors import CORS
import psycopg2

app = Flask(__name__)
CORS(app)

@app.route('/api/data', methods=['GET'])
def get_data():
    conn = psycopg2.connect(
        dbname="mydatabase",
        user="user",
        password="password",
        host="postgres"
    )
    cur = conn.cursor()
    cur.execute("SELECT message FROM data LIMIT 1;")
    message = cur.fetchone()[0]
    cur.close()
    conn.close()
    return jsonify({"message": message})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
