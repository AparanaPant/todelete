from flask import Flask

app = Flask(__name__)

if __name__ == '__main__':
    app.run(host='0.0.0.0')


@app.route('/test')
def get():
    return "helo"
