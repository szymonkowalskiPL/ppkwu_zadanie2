from flask import Flask, request, jsonify
import re

app = Flask(__name__)

@app.route('/checkstring',  methods=['GET', 'POST'])
def checkString():
    
    string = request.args.get('string')
    print(string)

    upper = len(re.findall(r'[A-Z]',string))
    lower = len(re.findall(r'[a-z]',string))
    numbers = len(re.findall(r'[0-9]',string))

    stringLen=len(string)

    otherCharacters = stringLen - (upper+lower+numbers)
    print(upper, lower, numbers, otherCharacters)
    
    return string

app.run()
