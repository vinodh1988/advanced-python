from config import db,app
from models import User
from flask import jsonify,request,abort


@app.route('/users',methods=['POST'])
def addPeople():
    try:
        input=request.get_json()
        username=input['username']
        password=input['password']
        usertype=input['usertype']
        db.session.add(User(username,password,usertype))
        db.session.commit()
        return {"status":"success"}, 201
    
    except:
        abort ({"status":"server error"},500)