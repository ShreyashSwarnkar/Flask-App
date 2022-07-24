from flask import Flask,request,jsonify

app = Flask(__name__)

contacts = [{'id':1,'name':'John','contact':9477685000,'done':False},
            {'id':2,'name':'Rohan','contact':9488759221,'done':False}]

@app.route('/adding-data',methods = ["POST"])
def addData():
    if(not request.json):
        return jsonify({"status":"error","message":"Plz provide data"},400)
    else:
        contact = {'id':contacts[-1]['id']+1,'Title':request.json['Title'],'Description':request.json['Description'],'Done':False}
        contacts.append(contact)
        return jsonify({"status":"success","message":"Contact add successfully"},400)

@app.route('/getting-data',methods=['GET'])
def get_data():
    return jsonify({"data":contacts})

app.run(debug=True)
