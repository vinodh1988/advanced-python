from config import db,app
from filestore import addData,readData
from constants import configdir
from flask import jsonify,request,abort
import logging


@app.route("/fpeople")
def getFilePeople():
    listp=readData(configdir)
    print(listp)
    return jsonify({'result':"success",'data':listp}), 200


@app.route('/fpeople',methods=['POST'])
def addFilePeople():
    try:
        input=request.get_json()
        sno=input['sno']
        name=input['name']
        city=input['city']
        addData(configdir,{'sno':sno,'name':name,city:'city'})
        logging.info('New Record added with sno '+str(sno))
        return {"status":"success"}, 201
    
    except:
        logging.error('problem occured')
        abort ({"status":"server error"},500)