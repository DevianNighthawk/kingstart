import pandas as pd
import os

class EmptyStringError(Exception):
	def __init__(self,str_arg,message="Filename is not provided try again"):
		self.str_arg=str_arg
		self.message = message
		super().__init__(self.message)


def read_data(filename):
	ret = None
	#print("==========")
	#print(os.path.isfile(filename))
	isFileExists = os.path.isfile(filename)
	if (type(filename) == str):
		#ret=pd.read_csv(filename)
		ret=None
	else:
		raise TypeError("File name is not str")
	#print("does our file exist? ")
	if ( len(filename) == 0):
		raise EmptyStringError(filename)
	if (isFileExists == False):
		print("file non exist")
		raise FileNotFoundError("File does not exist check file location")
	if ( (isFileExists == True) and (type(filename) == str) and (len(filename)>0) ):
		ret=pd.read_csv(filename)
	#print(isFileExists)
	#print("===========")
	#ret=None
	#print(len(filename))
	return ret

#ret=read_data("a.csv")
#print(ret)
#ret2=read_data(00)
#print(ret2)
#print("file length: ")
#print(len(""))

#ret3=read_data("t.csv")
#print(ret3)
#ret4=read_data("")
#print(ret4)
