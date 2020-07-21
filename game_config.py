import os

imgsize = 128
screensize = 512
numtiles = 4
tilestotal = 16
margin = 4

assetdir = 'assets'
assetfiles = [x for x in os.listdir(assetdir) if x[-3:].lower()== 'png']

assert len(assetfiles) == 8
