from flask import Flask, jsonify, request
app = Flask(__name__)

glucose_record = [
    {
        "glucose_id" : "0001",
        "date" : "October 6, 2022",
        "glucose" : "50mg"
    }
]
@app.route('/insert',methods=['POST','GET'])
def insert():
    if request.method == 'POST':
        data = request.get_json()
        if data:
            glucose_record.append(data)
            return 'Data has been Added!', 200
    elif request.method == 'GET':
        return jsonify(glucose_record)

@app.route('/edit/<int:index>',methods=['POST', 'GET', 'DELETE' ]) 
def edit(index):
    if request.method == 'POST': 
        up_record = request.get_json()
        glucose_record[index] = up_record
        return 'Data has already been Updated!', 200
    elif request.method == 'GET': 
        return jsonify(glucose_record[index])
    elif request.method == 'DELETE': 
        glucose_record.pop(index)
        return 'Data has already been Deleted!', 200

if __name__ == '__main__':
    app.run()