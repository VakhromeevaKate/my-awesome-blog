from flask import Flask, jsonify
from flask_cors import CORS
from datetime import date

# configuration
DEBUG = True

# instantiate the app
app = Flask(__name__)
app.config.from_object(__name__)

# enable CORS
CORS(app)

POSTS = [
    {
        'title': 'On the Road',
        'author': 'Jack Kerouac',
        'date': date(2020, 5, 1),
        'text': 'Some awesome text for my post 1'
    },
    {
        'title': 'Harry Potter and the Philosopher\'s Stone',
        'author': 'J. K. Rowling',
        'date': date(2020, 5, 1),
        'text': 'Some awesome text for my post 3'
    },
    {
        'title': 'Green Eggs and Ham',
        'author': 'Dr. Seuss',
        'date': date(2020, 5, 1),
        'text': 'Some awesome text for my post 3'
    }
]


# sanity check route
@app.route('/ping', methods=['GET'])
def ping_pong():
    return jsonify('pong!')


@app.route('/posts', methods=['GET'])
def all_posts():
    return jsonify({
        'status': 'success',
        'posts': POSTS
    })


if __name__ == '__main__':
    app.run()
