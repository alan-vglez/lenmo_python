from flask import Flask
app = flask(_name_)

@app.route('/')

def hello_world():
    return 'Hola Flask'

if _name_ == '_main_':
    app.run()
