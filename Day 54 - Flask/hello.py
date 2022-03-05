from flask import Flask
app = Flask(__name__)

# Notes: --------------------------------------------
# When Setting up flask, you need to do the following for windows in pycharm terminal
# set FLASK_APP=(name of the py script)
# set FLASK_APP=test.py
# flask run

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route("/bye")
def say_bye():
    return "Bye"

# Thie IF statement below makes it so the console will run flask instead of the terminal manually
if __name__ == '__main__':
    app.run()



hello_world()
