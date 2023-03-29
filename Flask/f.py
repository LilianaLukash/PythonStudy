import logging
from flask import Flask

app = Flask(__name__)
logging.basicConfig(level=logging.DEBUG)


@app.route('/hello')
def hello():
    app.logger.info('Hello is called')
    return 'Hello world!'


if __name__ == '__main__':
    app.run()
