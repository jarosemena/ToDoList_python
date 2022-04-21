from flask import Flask,request

app = Flask(__name__)


@app.route('/')
def index():
    return 'hola mundo'

@app.route('/post/<post_id>' , methods=['GET','POST'])
def getpost(post_id):
    if request.method == 'GET':
        return 'Post ' + post_id
    else:
        return 'debe utilizar el methodo get'

 
@app.route('/page/<post_id>' , methods=['GET'])
def gpost(post_id):
    return 'Post ' + post_id

@app.route('/page/<post_id>' , methods=['POST'])
def ppost(post_id):
    return 'Post ' + post_id

