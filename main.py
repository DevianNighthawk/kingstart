import pytest
import pndora.pndora as pndora
import flax.flax as flax
if __name__=="__main__":
	f2="a.csv"
	r=pndora.read_data("pndora/a.csv")
	print(r)
	ret=flax.to_numpy([12,33,66])
	print(ret)
