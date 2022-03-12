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

@app.route("/username/<name>") # if you do /<path:name>/ it will be a wildcard, you can do /<int:number>/
def greet(name):
    return f"Hello there {name}!"
    # If user goes on site: http://127.0.0.1:5000/username/yawnny they will see "hello yawnny)



# Thie IF statement below makes it so the console will run flask instead of the terminal manually
if __name__ == '__main__':
    app.run(debug=True) # To turn on debug do debug=True, debugging makes changes active
    # Debugger pin is used to open console on the webpage



