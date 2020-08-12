import sys
import os
#print(sys.path)
sys.path.append("../pndora")
#sys.path.append("../")
#myPath = os.path.dirname(os.path.abspath(__file__))
#sys.path.insert(0, myPath + '/../')
#print(sys.path)
import pndora
#import pytest
import unittest
import pytest
#print(pndora.read_data(0))
#@pytest.fixture
class TestPndora(unittest.TestCase):
	#import pndora
	#import pytest
	def test_filename_is_str(self):
		#import pndora
		self.assertRaises(TypeError,pndora.read_data,0)
	def test_file_existence(self):
		self.assertRaises(FileNotFoundError,pndora.read_data,"t.csv")




