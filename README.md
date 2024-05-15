# Python Flask Web Framework 🚀


## VENV
**_macOS_**
- Create venv on MACOS

````
#install virtualenv 
    python3 -m venv ./venv
#Activate venv
    . venv/bin/activate
````

**_Windows_**

````
#Create venv on Windows
**Install virtualenv
    pip install virtualenv
**Create venv
    python -m venv venv
**Activate venv
    source venv/Scripts/activate
**Deactivate venv
    deactivate

````

````
1. pip install flask
2. create templates folder
2. create asset folder
3. app.py
    from flask import Flask
    app = Flask(__name__)
    @app.route('/')
    def hello_world():
        return 'Hello World!'
    if __name__ == '__main__':
        app.run()
````
# ST7_Python_Flask
