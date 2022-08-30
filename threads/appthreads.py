

import time

def logstore(filepath):
    while(True):
        file1=open(filepath+"/logs.txt","a")
        file1.write("Wrote log @ "+time.ctime(time.time)+" \n")
        file1.close()
        time.sleep(5)

def datestore(filepath):
    while(True):
        file1=open(filepath+"/store.txt","a")
        file1.write("Wrote data @ "+time.ctime(time.time)+" \n")
        file1.close()
        time.sleep(10)
