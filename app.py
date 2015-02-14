from flask import Flask, render_template
from instagram.client import InstagramAPI

CLIENT_ID = 'change this'
CLIENT_SECRET = 'change this'

api = InstagramAPI(client_id=CLIENT_ID, client_secret=CLIENT_SECRET)
popular_media = api.media_popular(count=52)
images = []

for media in popular_media:
    images.append(media.images['standard_resolution'].url)

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html', media=images)


@app.route('/gram')
def gram():
    return 'ye boi'

if __name__ == '__main__':
    app.run(debug=True)
