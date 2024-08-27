from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/', methods=['GET'])
def echo():
    response = {
        'headers': dict(request.headers),
        'query': request.args,
        'body': request.get_data(as_text=True),
    }

    print(response)

    return jsonify(response)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)