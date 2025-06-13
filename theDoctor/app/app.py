import os
import boto3
from flask import Flask, jsonify
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

aws_access_key = os.getenv("AWS_ACCESS_KEY_ID")
aws_secret_key = os.getenv("AWS_SECRET_ACCESS_KEY")
aws_region = os.getenv("AWS_REGION")
table_name = os.getenv("DYNAMODB_TABLE")

app = Flask(__name__)

dynamodb = boto3.resource(
    'dynamodb',
    region_name=aws_region,
    aws_access_key_id=aws_access_key,
    aws_secret_access_key=aws_secret_key
)
table = dynamodb.Table(table_name)

@app.route('/secret', methods=['GET'])
def get_secret():
    try:
        response = table.get_item(Key={'codeName': 'theDoctor'})
        item = response.get('Item')
        if item:
            return jsonify(item), 200
        else:
            return jsonify({'message': "No item found with codeName='theDoctor'"}), 404
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/health', methods=['GET'])
def health_check():
    return jsonify({
        "status": "healthy",
        "container": "https://hub.docker.com/repository/docker/mohamadmas/zenity",
        "project": "https://github.com/mohamad1991/zenityRepo"
    }), 200


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
