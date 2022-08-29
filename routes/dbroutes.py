from config import db,app
from models import Person
from flask import jsonify,request,abort

@app.route("/people")
def getPeople():
    listp=Person.query.all()
    result=[x.serialize() for x in listp]
    return jsonify(result)


@app.route('/people',methods=['POST'])
def addPeople():
    try:
        input=request.get_json()
        sno=input['sno']
        name=input['name']
        city=input['city']
        db.session.add(Person(sno,name,city))
        db.session.commit()
        return {"status":"success"}, 201
    
    except:
        abort ({"status":"server error"},500)