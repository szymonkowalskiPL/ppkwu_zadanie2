from flask import Flask, request, jsonify
import re

app = Flask(__name__)

@app.route('/checkstring',  methods=['GET', 'POST'])
def checkString():
    
    string = request.args.get('string')
    print(string)

    upper =len(re.findall(r'[A-Z]',string))
    lower =len(re.findall(r'[a-z]',string))
    print(upper, lower)
    
    return string

app.run()
