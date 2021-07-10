from flask import Flask, jsonify, request,json
from flask_cors import CORS
import pymongo
  
connection_url = 'mongodb+srv://testuser:test@cluster0.lky5v.mongodb.net/test?retryWrites=true&w=majority'
app = Flask(__name__)
client = pymongo.MongoClient(connection_url)
  
# Database
Database = client.get_database('test')
# Table
SampleTable = Database.test1

@app.route('/', methods=['GET'])
def findAll():
    query = SampleTable.find()
    output = {}
    i = 0
    for x in query:
        output[i] = x
        output[i].pop('_id')
        i += 1
    # return jsonify(output)

    return {
    'statusCode': 200,
    'headers': {'Content-Type': 'application/json'},
    'body': json.dumps(output)
    }

# if __name__ == '__main__':
#     app.run(debug=True)