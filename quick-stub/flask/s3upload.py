import boto3
from botocore.exceptions import NoCredentialsError
from flask import Flask, jsonify
from flask import request
import json
import app_config as config
from flask_cors import CORS
import os
from werkzeug.utils import secure_filename
# cfg = config.getConfig()

app = Flask(__name__)
CORS(app)

ACCESS_KEY = 'XXXXXXXXXXXXXX'
SECRET_KEY = 'XXXXXXXXXXXXXXX'
BUCKET = 'bucket'

UPLOAD_FOLDER = 'path/to/upload/folder'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


def upload_to_s3(filename):
    s3 = boto3.client('s3', aws_access_key_id=ACCESS_KEY,
                      aws_secret_access_key=SECRET_KEY)

    try:
        s3.upload_file(UPLOAD_FOLDER+"/"+filename, BUCKET, filename)    
    except Exception as e:
        print e

@app.route('/s3/upload', methods=['POST'])
def saveFile():
    # print request.json
    file = request.files['file']
    print file.filename
    print "---------------"
    try:

        filename = secure_filename(file.filename)
        print filename
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        print("Upload Successful")
        upload_to_s3(file.filename)
        return "", 200
    except Exception as e:
        print e
        print("The file was not found")


# uploaded = upload_to_aws('test.txt', 'video-upload-sing-es', 'test.txt')

if __name__ == "__main__":
    app.run(host="0.0.0.0", threaded=True,port=5014)