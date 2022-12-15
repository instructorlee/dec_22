from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return "Hello World!"

@app.route('/say-hello/<name>')
def hello_name(name):
    return f'Hello {name}!'

@app.route('/say-hello/<string:name>/<int:age>')
def hello_name_age(age, name=None):
    return f'Hello {name}! You are {age} years old!XXXXXXXXXX'

@app.route('/say-hello/<int:age>/<string:name>')
def hello_age_name(age, name=None):
    return f'Hello {name}! You are {age} years old!'

if __name__=="__main__":   
    app.run(debug=True) 