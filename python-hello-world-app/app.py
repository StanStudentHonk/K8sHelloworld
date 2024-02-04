from flask import Flask
import logging

app = Flask(__name__)
logging.basicConfig(level=logging.DEBUG)
@app.route("/")
def helloworld():
    app.logger.info('Hallo vanaf deze container')
    return "Hello World!"
if __name__ == "__main__":
    app.run()