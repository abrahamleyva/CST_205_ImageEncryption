import flask
import os

proj2Team230 = flask.Flask(__name__)

@proj2Team230.route('/')
def index():
    #return "hi guys"
    return flask.render_template("index.html")
@proj2Team230.route('/test')
def test():
    #return "hi guys"
    return flask.render_template("test.html")

proj2Team230.run(
    port = int(os.getenv('PORT', 8080)),
    host = os.getenv('IP', '0.0.0.0')
)