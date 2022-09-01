import os
import logging


configdir =os.path.abspath(os.path.dirname(__file__))+"/config"

logging.basicConfig(filename=configdir+"/app.log",filemode='a',format="%(asctime)s  %(process)d-%(levelname)s-%(message)s")
