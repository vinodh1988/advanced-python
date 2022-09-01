import pickle 

def createFile(path):
    data={}
    filePickle=open(path+'/peopledata','wb')
    pickle.dump(data, filePickle)
    filePickle.close()

def addData(path,current):
    filePickle=open(path+"/peopledata",'rb')
    data=pickle.load(filePickle)
    data[current.sno]=current
    filePickle.close()
    filePickle=open(path+"/peopledata",'wb')
    pickle.dump(data, filePickle)
    filePickle.close()

def readData(path):
    filePickle=open(path+"/peopledata",'rb')
    data=pickle.load(filePickle)
    return data

