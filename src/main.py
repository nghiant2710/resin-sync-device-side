from flask import Flask
app = Flask(__name__)
print 'starting server...'
@app.route('/')
def hello_world():
    return 'Hello resin sync!!!'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
