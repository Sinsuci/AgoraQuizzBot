import pickle
import os

from numpy import character

class DataQuizz :
    def __init__(self, file) :
        self.file_name = file+".pkl"
        if os.path.exists(self.file_name) :
            with open(self.file_name,"rb") as file :
                self.data = pickle.load(file)
        else :
            self.data = {}
    

    def addQuestion(self,question,answer) :
        self.data[question] = answer
        if os.path.exists(self.file_name) == False :
            with open(self.file_name,"wb") as file2 :
                pass
        with open(self.file_name,"wb") as file2 :
            pickle.dump(self.data, file2)
        return True


    def getAnswer(self,question) :
        if question in self.data :
            return self.data[question]
        return False