import numpy as np

def to_numpy(arr):
	ret=None
	param_type=type(arr)
	if (param_type == list):
		ret=np.array(arr)
	else:
		raise TypeError("Invalid type expected list got {} of type {} instead".format(arr,param_type))
	return ret


#ret=to_numpy("33")
#ret2=to_numpy([34,55,66])
#print(ret)
#print(ret2)
