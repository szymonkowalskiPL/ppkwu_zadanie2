from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/s',  methods=['GET', 'POST'])
def calculateChecksum():
    '''
    string = request.args.get('string')
    
    md5hash = hashlib.md5(string.encode('utf-8')).hexdigest()

    crc32hash = binascii.crc32(string.encode('utf8'))
    
    sha1hash = hashlib.sha1(string.encode('utf-8')).hexdigest()
    
    sha256hash = hashlib.sha256(string.encode('utf-8')).hexdigest()
    
    return jsonify(
        md5=md5hash,
        crc32=crc32hash,
        sha1=sha1hash,
        sha256=sha256hash,
    )
    '''

app.run()
