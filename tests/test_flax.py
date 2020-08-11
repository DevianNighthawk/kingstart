import sys
import os
#print(sys.path)
sys.path.append("../flax")
#sys.path.append("../")
#myPath = os.path.dirname(os.path.abspath(__file__))

#print("myPath:",myPath)
#parentPath=os.path.abspath(os.path.join(myPath,".."))
#print("parentPath: ",parentPath)
#sys.path.insert(0, myPath + '/../')
#sys.path.insert(0,parentPath)
#print(sys.path)
#print(sys.path)
import flax
import pytest
import unittest
#print("======")
#print(flax.to_numpy("33"))
#print("======")
class TestFlax(unittest.TestCase):
	def test_param_is_str(self):
		self.assertRaises(TypeError,flax.to_numpy,"33")



