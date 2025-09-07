from flask import Flask, jsonify

app = Flask(__name__)

traffic_data = {
    "junction1": {"vehicles": 12, "signal": "green"},
    "junction2": {"vehicles": 8, "signal": "red"}
}

@app.route('/traffic')
def traffic():
    return jsonify(traffic_data)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
