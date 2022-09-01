from re import A
from config import app
import routes
from threads import logstore,datastore
import threading
import os
from filestore import createFile
from constants import logging

basedir =os.path.abspath(os.path.dirname(__file__))+"/config"

logging.basicConfig(filename=basedir+"/app.log",filemode='a',format="%(asctime)s  %(process)d-%(levelname)s-%(message)s")

t1= threading.Thread(target=logstore,args=(basedir,))
t2= threading.Thread(target=datastore,args=(basedir,))

t1.start() # ready state
t2.start() # ready state

createFile(basedir)

if __name__ == '__main__':
    app.run(host="0.0.0.0",debug=True)