from flask import Flask, request

from utils.private.shunt_of_private import keyword_private


app = Flask(__name__)


@app.route('/', methods=["POST", "GET"])
def post_data():
    if request.get_json().get('message_type') == 'private':
        print(request.get_json())
        uid = request.get_json().get('sender').get('user_id')
        message = request.get_json().get('raw_message')
        keyword_private(message, uid)
    return 'OK'


if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port=9494)
