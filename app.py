from flask import Flask, jsonify, request
from flask_cors import CORS
from datetime import date, datetime

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


@app.route('/posts', methods=['GET', 'POST'])
def all_posts():
    response_object = {'status': 'success'}
    if request.method == 'POST':
        post_data = request.get_json()
        POSTS.append({
            'title': post_data.get('title'),
            'author': post_data.get('author'),
            'date': datetime.now(),
            'text': post_data.get('text')
        })
        response_object['message'] = 'Post added!'
    else:
        response_object['posts'] = POSTS
    return jsonify(response_object)


if __name__ == '__main__':
    app.run()
