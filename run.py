from re import A
from config import app
import routes
from threads import logstore,datastore
import threading
import os

basedir =os.path.abspath(os.path.dirname(__file__))+"/config"

t1= threading.Thread(target=logstore,args=(basedir,))
t2= threading.Thread(target=datastore,args=(basedir,))

t1.start()
t2.start()


if __name__ == '__main__':
    app.run(host="0.0.0.0",debug=True)