import pandas as pd

class EmptyStringError(Exception):
	def __init__(self,str_arg,message="Filename is not provided try again"):
		self.str_arg=str_arg
		self.message = message
		super().__init__(self.message)


def read_data(filename):
	ret=None
	if type(filename) == str:
		ret=pd.read_csv(filename)
	else:
		raise TypeError("Your filename is not a string try again")
	return ret

#ret=read_data("a.csv")
#print(ret)
#ret2=read_data(00)
#print(ret2)
